
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
import string
from qiskit import execute, BasicAer
import math

ALPHABET = list(string.ascii_uppercase) + [' ', '-', '_', '.', ',', '@']
SIZE_REG = int(math.log2(len(ALPHABET)))
CIRCUIT_SIZE = SIZE_REG * 2

msg_indexes = list(range(0, SIZE_REG))
key_indexes = list(range(SIZE_REG, 2 * SIZE_REG))
key_slice = slice(SIZE_REG, 2 * SIZE_REG)

def vigenere_qcypher(chunk, sequence):
    for letter in chunk:
      a = format(ALPHABET.index(letter), f'0{SIZE_REG}b')[::-1]
      b = format(ALPHABET.index(key_char), f'0{SIZE_REG}b')[::-1]

      qc = QSCircuit(CIRCUIT_SIZE)

      qc.set_reg(msg, msg_indexes)
      qc.set_reg(key, key_indexes)

      qc.xor2(msg_indexes, key_indexes)

      qc.measure(key_indexes, key_indexes)

      backend = BasicAer.get_backend('qasm_simulator')
      job = execute(qc, backend, shots=1)

      counts = job.result().get_counts(qc)
      result_bin = ''.join(list(list(counts.keys())[0][::-1][key_slice][::-1]))
      result_char = ALPHABET[int(result_bin, 2) % len(ALPHABET)]
      return result_char

msg = input('Insert message: ').upper()
sequence_str = input('Insert transposition sequence: ').upper()

assert all(list(map(lambda c: c in ALPHABET, msg)))
sequence = list(map(int, sequence_str.split(' ')))
assert len(msg) % len(sequence) == 0
assert all(list(map(lambda x: x > 0 and x > len(sequence), sequence)))

cypher = ''
for i in range(0, len(msg), len(sequence)):
    chunks = msg[i:i+len(sequence)]
    for chunk in chunks:
      result_char = transposition_qcypher(chunk, sequence)
      cypher += result_char

print(f'\nMessage: {msg}')
print(f'Key: {sequence_str}')
print(f'Cypher text: {cypher}')
