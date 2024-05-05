
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

from composer.qs_circuit import QSCircuit
from qiskit import execute, BasicAer

SIZE = 3
SIZE_OUTPUT = 2 ** SIZE
for i in range(0, 2 ** SIZE):
    a = format(i, '0' + str(SIZE) + 'b')

    a_indexes = list(range(0, SIZE))
    flipped_a_indexes = list(range(SIZE, 2 * SIZE))
    output_indexes = list(range(2 * SIZE, 2 * SIZE + SIZE_OUTPUT))
    aux_index = 2 * SIZE + SIZE_OUTPUT
    CIRCUIT_SIZE = 2 * SIZE + SIZE_OUTPUT + 1

    qc = QSCircuit(CIRCUIT_SIZE)

    qc.set_reg(a[::-1], a_indexes)

    qc.decoder(a_indexes, output_indexes, flipped_a_indexes, aux_index)

    qc.measure(output_indexes, range(len(output_indexes)))

    # print(qc)

    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts(qc)

    print(a, '-', list(counts.keys())[0][-SIZE_OUTPUT:])
