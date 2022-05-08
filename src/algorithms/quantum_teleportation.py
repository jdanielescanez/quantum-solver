#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import QuantumCircuit
from qiskit.extensions import Initialize
from math import sqrt
from numpy import random
from qiskit.quantum_info import Statevector
from algorithms.qalgorithm import QAlgorithm

## A Quantum Teleportation Implemetation for QuantumSolver
## @see https://qiskit.org/textbook/ch-algorithms/teleportation.html
class QuantumTeleportation(QAlgorithm):
  ## Constructor
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

  ## Verify that the parameter is a valid probability of measure 0 (0 <= prob <= 1)
  def check_parameters(self, parameters):
    if len(parameters) == 1:
      try:
        value = float(parameters[0])
        return 0 <= value and value <= 1
      except:
        return False

  ## Append the simplest (and maximal) examples of quantum entanglement
  def get_bell_pair(self, circuit, a, b):
    circuit.h(a)
    circuit.cx(a,b)
    return circuit
  
  ## Alice gates
  def alice_gates(self, circuit, psi_index, a):
    circuit.cx(psi_index, a)
    circuit.h(psi_index)
    return circuit

  ## Bob gates
  def bob_gates(self, circuit, a, b, c):
    circuit.cx(b, c)
    circuit.cz(a, c)
    return circuit

  ## Creates a statevector of a qubit that has the specified probability to measure zero
  def get_statevector(self, measure_zero_prob):
    a1 = sqrt(measure_zero_prob)
    a2 = sqrt(1 - measure_zero_prob)
    return Statevector([complex(a1, 0), complex(a2, 0)])

  ## Create the circuit
  def circuit(self, measure_zero_prob):
    circuit = QuantumCircuit(3, 1)

    # Initialize Alice's q0
    psi = self.get_statevector(measure_zero_prob)
    init_gate = Initialize(psi)
    init_gate.label = 'Init'

    circuit.append(init_gate, [0])
    circuit.barrier()

    # Now begins the teleportation protocol
    circuit = self.get_bell_pair(circuit, 1, 2)
    circuit.barrier()
    # Send q1 to Alice and q2 to Bob
    circuit = self.alice_gates(circuit, 0, 1)
    circuit.barrier()
    # Alice sends classical bits to Bob
    circuit = self.bob_gates(circuit, 0, 1, 2)

    # See the results of q2
    circuit.measure(2, 0)

    return circuit
