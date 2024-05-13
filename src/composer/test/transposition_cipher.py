
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
import string
from qiskit import execute, BasicAer
import math
from qiskit.circuit.library import SwapGate

# ALPHABET = list(string.ascii_uppercase) + [' ', '-', '_', '.', ',', '@']
ALPHABET = ['A', 'B', 'C', 'D']
SIZE_REG = int(math.log2(len(ALPHABET)))

def transposition_qcypher(chunk, sequence):
    SIZE_SEQ = len(sequence)
    SIZE_CHUNK = len(chunk)
    SIZE_INDEX = math.ceil(math.log2(SIZE_SEQ))
    CIRCUIT_SIZE = 2 * SIZE_CHUNK * SIZE_REG + SIZE_SEQ * SIZE_INDEX

    msg_indexes = list(range(0, SIZE_CHUNK * SIZE_REG))
    key_indexes = list(map(lambda i: list(range(SIZE_CHUNK * SIZE_REG + (i) * SIZE_INDEX, SIZE_CHUNK * SIZE_REG + (i + 1) * SIZE_INDEX)), range(SIZE_SEQ)))
    measure_indexes = list(range(SIZE_CHUNK * SIZE_REG + SIZE_SEQ * SIZE_INDEX, CIRCUIT_SIZE))

    qc = QSCircuit(CIRCUIT_SIZE)
    for i, letter in enumerate(chunk):
      msg = format(ALPHABET.index(letter), f'0{SIZE_REG}b')[::-1]
      qc.set_reg(msg, measure_indexes[i * SIZE_REG: (1 + i) * SIZE_REG])
      qc.set_reg(msg, msg_indexes[i * SIZE_REG: (1 + i) * SIZE_REG])

    for i, index in enumerate(sequence):
      index_key = format(index - 1, f'0{SIZE_INDEX}b')[::-1]
      qc.set_reg(index_key, key_indexes[i])
    qc.barrier()

    for i, index in enumerate(sequence):
      list_aux = sequence[::]
      list_aux.remove(i + 1)
      for index2 in list_aux:
        swap = SwapGate().control(num_ctrl_qubits=SIZE_INDEX, ctrl_state=(index2 - 1))
        for k in range(SIZE_REG):
          qc.append(swap, [*key_indexes[i], msg_indexes[(index2 - 1) * SIZE_REG + k], measure_indexes[i * SIZE_REG + k]])
      qc.barrier()

    qc.measure(measure_indexes, measure_indexes)
    print(qc)
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)

    counts = job.result().get_counts(qc)
    tag = list(counts.keys())[0]
    sep = [tag[i:i+SIZE_REG] for i in range(0, len(tag), SIZE_REG)][:SIZE_CHUNK][::-1]
    return ''.join([ALPHABET[int(result_bin_chunk, 2) % len(ALPHABET)] for result_bin_chunk in sep])

msg = input('Insert message: ').upper()
sequence_str = input('Insert transposition sequence (separated using spaces): ')
sequence = list(map(int, sequence_str.split(' ')))

assert all(list(map(lambda c: c in ALPHABET, msg)))
assert len(msg) % len(sequence) == 0
assert all(list(map(lambda x: x - 1 in range(len(sequence)), sequence)))
assert all(list(map(lambda x: x + 1 in sequence, range(len(sequence)))))

cypher = ''
for i in range(0, len(msg), len(sequence)):
  chunk = msg[i:i+len(sequence)]
  result_char = transposition_qcypher(chunk, sequence)
  cypher += result_char

print(f'\nMessage: {msg}')
print(f'Key: {sequence_str}')
print(f'Cypher text: {cypher}')
