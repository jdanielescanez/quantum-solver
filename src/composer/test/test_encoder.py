
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../composer')

from composer.qs_circuit import QSCircuit
from qiskit import execute, BasicAer
from math import log2

SIZE = 2 ** 3
for i in range(0, SIZE):
    a = format(2 ** i, '0' + str(SIZE) + 'b')
    SIZE_REG = len(a)
    LOG_SIZE_REG = int(log2(SIZE_REG))

    a_indexes = list(range(0, SIZE_REG))
    output_indexes = list(range(SIZE_REG, SIZE_REG + LOG_SIZE_REG))
    aux_index = SIZE_REG + LOG_SIZE_REG
    CIRCUIT_SIZE = SIZE_REG + LOG_SIZE_REG + 1

    qc = QSCircuit(CIRCUIT_SIZE)

    qc.set_reg(a[::-1], a_indexes)

    qc.encoder(a_indexes, output_indexes, aux_index)

    qc.measure(output_indexes, range(len(output_indexes)))

    # print(qc)

    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts(qc)

    print(i, '-', list(counts.keys())[0][-LOG_SIZE_REG:])
