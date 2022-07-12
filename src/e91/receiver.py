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

  ## Create the key with the other choices
  def create_key(self, other_choices, result, circuits):
    count = [[0, 0, 0, 0], # XW observable
             [0, 0, 0, 0], # XV observable
             [0, 0, 0, 0], # ZW observable
             [0, 0, 0, 0]] # ZV observable

    self.key = []
    for i in range(self.original_bits_size):
      # If Alice and Bob have measured the spin projections onto the a_2/b_1 or a_3/b_2 directions
      if (other_choices[i] == 'a2' and self.axes[i] == 'b1') or \
        (other_choices[i] == 'a3' and self.axes[i] == 'b2'):
          self.key.append(0 if self.values[i] == 1 else 1)
      else:
        if (other_choices[i] == 'a1' or other_choices[i] == 'a3') and (self.axes[i] == 'b1' or self.axes[i] == 'b3'):
          res = list(result.get_counts(circuits[i]).keys())[0]
          j = 2 * int(other_choices[i] == 'a3') + int(self.axes[i] == 'b3')
          k = int(res[-2:], base=2)
          count[j][k] += 1

    self.set_corr(count)
