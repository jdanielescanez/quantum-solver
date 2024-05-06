
from s_aes import QS_SAES_Circuit

from qiskit import execute
from qiskit_aer import AerSimulator

SIZE_REG = 16
CIRCUIT_SIZE = SIZE_REG * 2

msg_indexes = list(range(0, SIZE_REG))
msg_slice = slice(0, SIZE_REG)
key_indexes = list(range(SIZE_REG, 2 * SIZE_REG))

for i in range(2 ** 4):
  msg = '0' * 12 + format(i, f'0{4}b')
  key = '0' * 16

  qc = QS_SAES_Circuit(CIRCUIT_SIZE, msg, key, msg_indexes, key_indexes)
  qc.s_box()
  qc.measure(range(4), range(4))

  backend = AerSimulator(method='matrix_product_state')
  job = execute(qc, backend, shots=1)
  counts = job.result().get_counts(qc)
  result_bin = ''.join(list(list(counts.keys())[0][::-1][:4][::-1]))
  print(msg, '-', result_bin[:4])
