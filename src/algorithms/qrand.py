
from qiskit import QuantumCircuit
from algorithms.algorithm import Algorithm

class QRand(Algorithm):
  def __init__(self):
    self.name = 'QRand'
    self.description = 'Gives a random number between 0 and 2 ^ n_qubits - 1'
    self.parameters = [
      {
        'type': 'int',
        'description': 'Number of qubits to use',
        'constraint': 'Can\'t be bigger than the number of qubits of the selected backend'
      }
    ]
    self.n_shots = 1
    self.parse_result = lambda counts: int(list(counts.keys())[0], 2)
    self.parse_parameters = lambda array: [int(array[0])]

  def circuit(self, n=1):
    # Create a Quantum Circuit acting on the q register
    circuit = QuantumCircuit(n, n)
    n_range = list(range(n))

    # Add a H gate on every qubit
    circuit.h(n_range)

    circuit.barrier()

    # Map the quantum measurement to the classical bits
    circuit.measure(n_range, n_range)

    return circuit
