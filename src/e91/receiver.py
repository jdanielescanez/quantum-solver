#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from e91.participant import Participant
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from numpy.random import rand

## The Receiver entity in the E91 implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Receiver(Participant):
  ## Constructor
  def __init__(self, name='', original_bits_size=0, qr=QuantumRegister(2, name="qr"), cr=ClassicalRegister(4, name="cr")):
    super().__init__(name, original_bits_size, qr, cr)

  def _calculate_measurements(self):
    self.measurements = {}
    qr = self.qr
    cr = self.cr
    # Measure the spin projection of Bob's qubit onto the b_1 direction (W basis)
    self.measurements['b1'] = QuantumCircuit(qr, cr, name='measureB1')
    self.measurements['b1'].s(qr[1])
    self.measurements['b1'].h(qr[1])
    self.measurements['b1'].t(qr[1])
    self.measurements['b1'].h(qr[1])
    self.measurements['b1'].measure(qr[1], cr[1])

    # Measure the spin projection of Bob's qubit onto the b_2 direction (standard Z basis)
    self.measurements['b2'] = QuantumCircuit(qr, cr, name='measureB2')
    self.measurements['b2'].measure(qr[1], cr[1])

    # Measure the spin projection of Bob's qubit onto the b_3 direction (V basis)
    self.measurements['b3'] = QuantumCircuit(qr, cr, name='measureB3')
    self.measurements['b3'].s(qr[1])
    self.measurements['b3'].h(qr[1])
    self.measurements['b3'].tdg(qr[1])
    self.measurements['b3'].h(qr[1])
    self.measurements['b3'].measure(qr[1], cr[1])

  # Create the key with the circuit measurement results
  def create_values(self, result, circuits):
    for i in range(self.original_bits_size):
      res = list(result.get_counts(circuits[i]).keys())[0]
      self.values.append(int(res[-1]))
