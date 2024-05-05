
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
from qiskit import execute, BasicAer
from math import log2

SIZE_INPUT = 2 ** 1
SIZE_SELECTOR = int(log2(SIZE_INPUT))
for i in range(0, 2 ** SIZE_INPUT):
    a = format(i, '0' + str(SIZE_INPUT) + 'b')
    for j in range(0, 2 ** SIZE_SELECTOR):
        selectors = format(j, '0' + str(SIZE_SELECTOR) + 'b')

        a_indexes = list(range(0, SIZE_INPUT))
        selectors_indexes = list(range(SIZE_INPUT, SIZE_INPUT + SIZE_SELECTOR))
        flipped_selectors_indexes = list(range(SIZE_INPUT + SIZE_SELECTOR, SIZE_INPUT + 2 * SIZE_SELECTOR))
        output_index = SIZE_INPUT + 2 * SIZE_SELECTOR
        aux_index = SIZE_INPUT + 2 * SIZE_SELECTOR + 1
        CIRCUIT_SIZE = SIZE_INPUT + 2 * SIZE_SELECTOR + 2

        qc = QSCircuit(CIRCUIT_SIZE)

        qc.set_reg(a[::-1], a_indexes)
        qc.set_reg(selectors[::-1], selectors_indexes)

        qc.multiplexer(a_indexes, selectors_indexes, flipped_selectors_indexes, output_index, aux_index)

        qc.measure(output_index, output_index)

        print(qc)

        backend = BasicAer.get_backend('qasm_simulator')
        job = execute(qc, backend, shots=1)
        counts = job.result().get_counts(qc)

        print(a, '-', selectors, '-', list(counts.keys())[0][::-1][output_index])
