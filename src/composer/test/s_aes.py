
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
from qiskit import execute, QuantumCircuit
from qiskit_aer import AerSimulator

SIZE_REG = 16
CIRCUIT_SIZE = SIZE_REG * 2
ALPHABET = ['0', '1']

class QS_SAES_Circuit(QSCircuit):
  def __init__(self, CIRCUIT_SIZE, msg, key, msg_indexes, key_indexes):
    super().__init__(CIRCUIT_SIZE)
    self.msg_indexes = msg_indexes
    self.key_indexes = key_indexes
    self.set_bin_reg(msg, self.msg_indexes)
    self.set_bin_reg(key, self.key_indexes)

    self.build()
  
  def build(self):
    self.barrier()
    self.add_roundkey()
    self.barrier()
    self.s_box()
    self.barrier()
    self.shift_rows()
    self.barrier()
    self.mix_columns()
    self.barrier()

    self.key_expansion('10000000'[::-1])
    self.barrier()
    self.add_roundkey()
    self.barrier()
    self.s_box()
    self.barrier()
    self.shift_rows()

    self.barrier()
    self.key_expansion('00110000'[::-1])
    self.barrier()
    self.add_roundkey()
  
  def add_roundkey(self):
    self.xor2(self.key_indexes, self.msg_indexes)

  def s_key(self):
    for limit in range(0, 8, 4):
      x0, x1, x2, x3 = [self.key_indexes[i] for i in list(range(limit, limit + 4))]

      self.swap2(x0, x3)
      self.swap2(x1, x2)

      self.xor2(x2, x1)
      self.ccx(x3, x1, x0)
      self.ccx(x0, x2, x3)
      self.ccx(x0, x3, x1)
      self.mcx([x0, x1, x3], x2)
      self.cx(x3, x0)
      self.not1([x2, x3])
      self.cx(x0, x2)
      self.ccx(x1, x2, x0)
      self.ccx(x0, x3, x1)
      self.ccx(x0, x1, x3)

      self.shift_right([x0, x1, x2, x3])
      self.swap2(x0, x3)
      self.swap2(x1, x2)

  def s_key_inv(self):
    qc = QuantumCircuit(4)
    qc.swap(0, 3)
    qc.swap(1, 2)

    qc.cx(2, 1)
    qc.ccx(3, 1, 0)
    qc.ccx(0, 2, 3)
    qc.ccx(0, 3, 1)
    qc.mcx([0, 1, 3], 2)
    qc.cx(3, 0)
    qc.x([2, 3])
    qc.cx(0, 2)
    qc.ccx(1, 2, 0)
    qc.ccx(0, 3, 1)
    qc.ccx(0, 1, 3)

    indexes = [0, 1, 2, 3]
    indexes.sort(reverse=True)
    qc.swap(indexes[:-1], indexes[1:])
    qc.swap(0, 3)
    qc.swap(1, 2)
    qc_inv = qc.to_gate().inverse()
    
    for limit in range(0, 8, 4):
      self.append(qc_inv, [self.key_indexes[i] for i in list(range(limit, limit + 4))])

  def s_box(self):
    for limit in range(0, 16, 4):
      x0, x1, x2, x3 = [self.msg_indexes[i] for i in list(range(limit, limit + 4))]

      self.swap2(x0, x3)
      self.swap2(x1, x2)

      self.xor2(x2, x1)
      self.ccx(x3, x1, x0)
      self.ccx(x0, x2, x3)
      self.ccx(x0, x3, x1)
      self.mcx([x0, x1, x3], x2)
      self.cx(x3, x0)
      self.not1([x2, x3])
      self.cx(x0, x2)
      self.ccx(x1, x2, x0)
      self.ccx(x0, x3, x1)
      self.ccx(x0, x1, x3)

      self.shift_right([x0, x1, x2, x3])
      self.swap2(x0, x3)
      self.swap2(x1, x2)

  def mix_columns(self):
    for limit in range(0, 16, 8):
      b0, b1, b2, b3, b4, b5, b6, b7 = [self.msg_indexes[i] for i in list(range(limit, limit + 8))[::-1]]
      self.xor2(b0, b6)
      self.xor2(b5, b3)
      self.xor2(b4, b2)
      self.xor2(b1, b7)
      self.xor2(b7, b4)
      self.xor2(b2, b5)
      self.xor2(b3, b0)
      self.xor2(b6, b1)

      self.swap2(b0, b6)
      self.swap2(b1, b4)
      self.swap2(b2, b5)
      self.swap2(b4, b5)
      self.swap2(b5, b6)

  def shift_rows(self):
    x0, x1, x3, x4 = [self.msg_indexes[i] for i in range(0, 4)]
    x8, x9, x10, x11 = [self.msg_indexes[i] for i in range(8, 12)]
    self.swap2(x0, x8)
    self.swap2(x1, x9)
    self.swap2(x3, x10)
    self.swap2(x4, x11)
  
  def key_expansion(self, constant):
    self.swap2(self.key_indexes[:4], self.key_indexes[4:8])
    self.s_key()
    for i, bit in enumerate(constant):
      if bit == '1':
        self.not1(self.key_indexes[i])
    
    self.xor2(self.key_indexes[:8], self.key_indexes[-8:])

    for i, bit in enumerate(constant):
      if bit == '1':
        self.not1(self.key_indexes[i])

    self.s_key_inv()
    self.swap2(self.key_indexes[:4], self.key_indexes[4:8])
    self.xor2(self.key_indexes[-8:], self.key_indexes[:8])

def saes_qcypher(msg, key):
  msg_indexes = list(range(0, SIZE_REG))
  msg_slice = slice(0, SIZE_REG)
  key_indexes = list(range(SIZE_REG, 2 * SIZE_REG))

  qc = QS_SAES_Circuit(CIRCUIT_SIZE, msg, key, msg_indexes, key_indexes)
  qc.measure(msg_indexes, msg_indexes)
  print(qc)

  backend = AerSimulator(method='matrix_product_state')
  job = execute(qc, backend, shots=1)

  counts = job.result().get_counts(qc)
  result_bin = ''.join(list(list(counts.keys())[0][::-1][msg_slice][::-1]))
  return result_bin

if __name__ == "__main__":
  msg = '0110111101101011' # input('Insert message: ')
  key = '1010011100111011' # input('Insert key: ')

  assert all(list(map(lambda c: c in ALPHABET, msg)))
  assert all(list(map(lambda c: c in ALPHABET, key)))
  assert len(msg) == SIZE_REG
  assert len(msg) == len(key)

  cypher = saes_qcypher(msg, key)

  print()
  print(f'Message:     {msg}')
  print(f'Key:         {key}\n')
  print(f'-> Expected: 0000011100111000')
  print(f'Cypher text: {cypher}\n')
