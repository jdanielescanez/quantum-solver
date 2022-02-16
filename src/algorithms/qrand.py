
import numpy as np
from math import floor, ceil, log2
from qiskit import QuantumCircuit, transpile

class QRand:
  def __init__(self):
    self.name = 'QRand'
    self.description = 'Gives a random number between 0 and 2 ^ n_qubits - 1'
    self.parameters = [
      {
        'type': 'int',
        'description': 'Number of qubits to use',
        'constraint': 'Can\'t be bigger than the number of qubits of the selected IBM Hardware'
      }
    ]
    self.n_shots = 1
    self.parse_result = lambda counts: int(list(counts.keys())[0], 2)
    self.parse_parameters = lambda array: int(array[0])

  def circuit(self, n):
    # Create a Quantum Circuit acting on the q register
    circuit = QuantumCircuit(n, n)

    # Add a H gate on every qubit
    for i in range(n):
      circuit.h(i)

    n_range = list(range(n))
    # Map the quantum measurement to the classical bits
    circuit.measure(n_range, n_range)

    return circuit
