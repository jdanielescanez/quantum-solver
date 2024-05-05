
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
from qiskit import execute, BasicAer

print('AND')
for i in range(2 ** 5):
    a = format(i, '05b')[::-1]
    SIZE_REG = len(a)

    a_indexes = list(range(0, SIZE_REG))
    result_index = SIZE_REG
    aux_index = SIZE_REG + 1
    CIRCUIT_SIZE = len(a_indexes) + 2

    qc = QSCircuit(CIRCUIT_SIZE)

    qc.set_reg(a, a_indexes)

    qc.and_list(a_indexes, result_index, aux_index)

    qc.measure(result_index, 0)

    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts(qc)

    print(i, '-', list(counts.keys())[0][-1])

print('\nOR')
for i in range(2 ** 5):
    a = format(i, '05b')[::-1]
    SIZE_REG = len(a)

    a_indexes = list(range(0, SIZE_REG))
    result_index = SIZE_REG
    aux_index = SIZE_REG + 1
    CIRCUIT_SIZE = len(a_indexes) + 2

    qc = QSCircuit(CIRCUIT_SIZE)

    qc.set_reg(a, a_indexes)

    qc.or_list(a_indexes, result_index, aux_index)

    qc.measure(result_index, 0)

    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts(qc)

    print(i, '-', list(counts.keys())[0][-1])
