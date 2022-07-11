#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from e91.participant import Participant
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

## The Sender entity in the E91 implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Sender(Participant):
  ## Constructor
  def __init__(self, name='', original_bits_size=0, qr=QuantumRegister(2, name="qr"), cr=ClassicalRegister(4, name="cr")):
    super().__init__(name, original_bits_size, qr, cr)

  def _calculate_measurements(self):
    self.measurements = {}
    # Measure the spin projection of Alice's qubit onto the a_1 direction (X basis)
    self.measurements['a1'] = QuantumCircuit(self.qr, self.cr, name='measureA1')
    self.measurements['a1'].h(self.qr[0])
    self.measurements['a1'].measure(self.qr[0], self.cr[0])

    # Measure the spin projection of Alice's qubit onto the a_2 direction (W basis)
    self.measurements['a2'] = QuantumCircuit(self.qr, self.cr, name='measureA2')
    self.measurements['a2'].s(self.qr[0])
    self.measurements['a2'].h(self.qr[0])
    self.measurements['a2'].t(self.qr[0])
    self.measurements['a2'].h(self.qr[0])
    self.measurements['a2'].measure(self.qr[0], self.cr[0])

    # Measure the spin projection of Alice's qubit onto the a_3 direction (standard Z basis)
    self.measurements['a3'] = QuantumCircuit(self.qr, self.cr, name='measureA3')
    self.measurements['a3'].measure(self.qr[0], self.cr[0])

  # Create the key with the circuit measurement results
  def create_values(self, result, circuits):
    for i in range(self.original_bits_size):
      res = list(result.get_counts(circuits[i]).keys())[0]
      self.values.append(int(res[-2]))

  ## Create the key with the other choices
  def create_key(self, other_choices, result, circuits):
    count = [[0, 0, 0, 0], # XW observable
             [0, 0, 0, 0], # XV observable
             [0, 0, 0, 0], # ZW observable
             [0, 0, 0, 0]] # ZV observable

    self.key = []
    for i in range(self.original_bits_size):
      # If Alice and Bob have measured the spin projections onto the a_2/b_1 or a_3/b_2 directions
      if (self.axes[i] == 'a2' and other_choices[i] == 'b1') or \
         (self.axes[i] == 'a3' and other_choices[i] == 'b2'):
        self.key.append(self.values[i])
      else:
        if (self.axes[i] == 'a1' or self.axes[i] == 'a3') and (other_choices[i] == 'b1' or other_choices[i] == 'b3'):
          res = list(result.get_counts(circuits[i]).keys())[0]
          j = 2 * int(self.axes[i] == 'a3') + int(other_choices[i] == 'b3')
          k = int(res[-2:], base=2)
          count[j][k] += 1
      
    self.set_corr(count)
