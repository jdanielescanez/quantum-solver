
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../composer')

from composer.qs_circuit import QSCircuit
import string
from qiskit import execute, BasicAer, QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit.visualization import plot_distribution
# import nltk
# nltk.download('words')
from nltk.corpus import words
import math

alphabet = list(string.ascii_uppercase) + [' ', '-', '.', ',', '@']
wordlist_lowercased = filter(lambda x: all([char in alphabet for char in x]), list(set(i.upper() for i in words.words())))

a = format(alphabet.index('K'), '05b')[::-1]
b = format(alphabet.index('N'), '05b')[::-1]
# a = '001011'[::-1]
# b = '111010'[::-1]

assert len(a) == len(b)

SIZE_REG = len(a)
N_AUXS = 4
CIRCUIT_SIZE = SIZE_REG * 2 + N_AUXS

a_indexes = list(range(0, SIZE_REG))
b_indexes = list(range(SIZE_REG, 2 * SIZE_REG))
carry_index = 2 * SIZE_REG
aux_indexes = list(range(2 * SIZE_REG + 1, 2 * SIZE_REG + N_AUXS))
measure_indexes = range(len(aux_indexes), SIZE_REG + len(aux_indexes) + 1)

qc = QSCircuit(CIRCUIT_SIZE)

qc.set_reg(a, a_indexes) # a
qc.set_reg(b, b_indexes) # b

qc.add_regs(a_indexes, b_indexes, carry_index, aux_indexes)

# print(qc)

backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1)

string_result = list(job.result().get_counts(qc).keys())[0]
string_result_b = string_result[len(aux_indexes) + 1 : len(aux_indexes) + SIZE_REG + 1]
index = int(string_result_b, 2)

def grover_oracle(marked_states):
    """Build a Grover oracle for multiple marked states

    Here we assume all input marked states have the same number of bits

    Parameters:
        marked_states (str or list): Marked states of oracle

    Returns:
        QuantumCircuit: Quantum circuit representing Grover oracle
    """
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    # Compute the number of qubits in circuit
    num_qubits = len(marked_states[0])

    qc = QuantumCircuit(num_qubits)
    # Mark each target state in the input list
    for target in marked_states:
        # Flip target bit-string to match Qiskit bit-ordering
        rev_target = target[::-1]
        # Find the indices of all the '0' elements in bit-string
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls)
        # where the target bit-string has a '0' entry
        qc.x(zero_inds)
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        qc.x(zero_inds)
    return qc

marked_states = [format(alphabet.index('N'), '05b')[::-1]]
oracle = grover_oracle(marked_states)
grover_op = GroverOperator(oracle)
optimal_num_iterations = math.floor(
    math.pi / 4 * math.sqrt(2**grover_op.num_qubits / len(marked_states))
)
qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
# Measure all qubits
qc.measure_all()
