
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
import string
from qiskit import execute, BasicAer
import math

ALPHABET = list(string.ascii_uppercase) + [' ', '-', '_', '.', ',', '@']
SIZE_REG = int(math.log2(len(ALPHABET)))
CIRCUIT_SIZE = SIZE_REG * 2

def vigenere_qcypher(msg, key):
    msg_indexes = list(range(0, SIZE_REG))
    key_indexes = list(range(SIZE_REG, 2 * SIZE_REG))
    key_slice = slice(SIZE_REG, 2 * SIZE_REG)

    qc = QSCircuit(CIRCUIT_SIZE)

    qc.set_reg(msg, msg_indexes) # a
    qc.set_reg(key, key_indexes) # b

    qc.xor2(msg_indexes, key_indexes)

    qc.measure(key_indexes, key_indexes)

    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)

    counts = job.result().get_counts(qc)
    result_bin = ''.join(list(list(counts.keys())[0][::-1][key_slice][::-1]))
    result_char = ALPHABET[int(result_bin, 2) % len(ALPHABET)]
    return result_char

msg = input('Insert message: ').upper()
key = input('Insert key: ').upper()

assert all(list(map(lambda c: c in ALPHABET, msg)))
assert all(list(map(lambda c: c in ALPHABET, key)))

cypher = ''
for i, msg_char in enumerate(msg):
    key_char = key[i % len(key)]
    a = format(ALPHABET.index(msg_char), f'0{SIZE_REG}b')[::-1]
    b = format(ALPHABET.index(key_char), f'0{SIZE_REG}b')[::-1]

    result_char = vigenere_qcypher(a, b)
    cypher += result_char

print(f'\nMessage: {msg}')
print(f'Key: {key}')
print(f'Cypher text: {cypher}')
