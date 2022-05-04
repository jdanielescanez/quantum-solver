
from qiskit import QuantumCircuit
from qiskit.extensions import Initialize
from math import sqrt
from numpy import random
from qiskit.quantum_info import Statevector
from algorithms.qalgorithm import QAlgorithm

class QuantumTeleportation(QAlgorithm):
  def __init__(self):
    self.name = 'Quantum Teleportation'
    self.description = 'Transmit one qubit using two classical bits'
    self.parameters = [
      {
        'type': 'float',
        'description': 'Probability of measure 0',
        'constraint': 'Must be a float number between 0 and 1'
      },
    ]
    self.parse_result = lambda counts: list(counts.keys())[0]
    self.parse_parameters = lambda parameters: [float(parameters[0])]

  def check_parameters(self, parameters):
    if len(parameters) == 1:
      try:
        value = float(parameters[0])
        return 0 <= value and value <= 1
      except:
        return False

  def get_bell_pair(self, circuit, a, b):
    circuit.h(a)
    circuit.cx(a,b)
    return circuit
  
  def alice_gates(self, circuit, psi_index, a):
    circuit.cx(psi_index, a)
    circuit.h(psi_index)
    return circuit

  def bob_gates(self, circuit, a, b, c):
    circuit.cx(b, c)
    circuit.cz(a, c)
    return circuit

  def get_statevector(self, measure_zero_prob):
    a1 = sqrt(measure_zero_prob)
    a2 = sqrt(1 - measure_zero_prob)
    return Statevector([complex(a1, 0), complex(a2, 0)])

  def circuit(self, measure_zero_prob):
    circuit = QuantumCircuit(3, 1)

    # First, let's initialize Alice's q0
    psi_index = 0
    psi = self.get_statevector(measure_zero_prob)

    init_gate = Initialize(psi)
    init_gate.label = 'Init'

    circuit.append(init_gate, [psi_index])
    circuit.barrier()

    # Now begins the teleportation protocol
    circuit = self.get_bell_pair(circuit, 1, 2)
    circuit.barrier()
    # Send q1 to Alice and q2 to Bob
    circuit = self.alice_gates(circuit, psi_index, 1)
    circuit.barrier()
    # Alice sends classical bits to Bob
    circuit = self.bob_gates(circuit, 0, 1, 2)

    # See the results, we only care about the state of qubit 2
    circuit.measure(2, 0)

    return circuit
