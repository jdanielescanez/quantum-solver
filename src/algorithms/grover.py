
from qiskit import QuantumCircuit
from algorithms.qalgorithm import QAlgorithm

class Grover(QAlgorithm):
  def __init__(self):
    self.name = 'Grover\'s Algorithm (2 Qubits)'
    self.description = 'Performs the search in an unordered sequence of data'
    self.parameters = [
      {
        'type': 'string',
        'description': 'Two bits to create the mark state',
        'constraint': 'Must be a binary string of length two'
      }
    ]
    self.parse_result = lambda counts: list(counts.keys())[0]
    self.parse_parameters = lambda parameters: [parameters[0]]

  def check_parameters(self, parameters):
    if len(parameters) == 1 and type(parameters[0]) == str and len(parameters[0]) == 2:
      try:
        value = int(parameters[0], 2)
        return value >= 0 and value <= 3
      except:
        return False

  def get_oracle(self, n, mark_state):
    diffusor = QuantumCircuit(n, n)

    for i, char in enumerate(mark_state):
      if char == '0':
        diffusor.s(i)

    diffusor.cz(0, 1)

    for i, char in enumerate(mark_state):
      if char == '0':
        diffusor.s(i)

    return diffusor

  def get_diffusor(self, n, n_range):
    diffusor = QuantumCircuit(n, n)

    diffusor.h(n_range)

    diffusor.z(n_range)
    diffusor.cz(0, 1)

    diffusor.h(n_range)

    return diffusor

  def circuit(self, mark_state):
    n = 2
    grover_circuit = QuantumCircuit(n, n)
    n_range = list(range(n))

    # Add a H gate on every qubit
    grover_circuit.h(n_range)
    grover_circuit.barrier()

    # Apply oracle
    oracle = self.get_oracle(n, mark_state)
    grover_circuit += oracle
    grover_circuit.barrier()

    # Apply diffuser
    diffusor = self.get_diffusor(n, n_range)
    grover_circuit += diffusor
    grover_circuit.barrier()

    # Map the quantum measurement to the classical bits
    grover_circuit.measure(n_range, n_range)

    return grover_circuit
