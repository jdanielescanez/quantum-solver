
from qiskit import QuantumCircuit
from algorithms.qalgorithm import QAlgorithm

class QRand(QAlgorithm):
  def __init__(self):
    self.name = 'QRand'
    self.description = 'Gives a random number between 0 and 2 ^ n_qubits - 1'
    self.parameters = [
      {
        'type': 'int',
        'description': 'A positive number of qubits to use',
        'constraint': 'Can\'t be bigger than the number of qubits of the selected backend'
      }
    ]
    self.parse_result = lambda counts: int(list(counts.keys())[0], 2)
    self.parse_parameters = lambda parameters: [int(parameters[0])]

  def check_parameters(self, parameters):
    if len(parameters) == 1 and type(parameters[0]) == str:
      try:
        return int(parameters[0]) > 0
      except:
        return False

  def circuit(self, n=1):
    # Create a Quantum Circuit
    circuit = QuantumCircuit(n, n)
    n_range = list(range(n))

    # Add a H gate on every qubit
    circuit.h(n_range)

    circuit.barrier()

    # Map the quantum measurement to the classical bits
    circuit.measure(n_range, n_range)

    return circuit
