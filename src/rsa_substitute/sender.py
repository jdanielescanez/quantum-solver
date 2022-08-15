#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import QuantumCircuit
from rsa_substitute.participant import Participant
from random import sample

## The Sender entity in the E91 implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Sender(Participant):
  ## Constructor
  def __init__(self, name='', r=0, p_numbers=[]):
    super().__init__(name)
    self.r = r
    self.p_numbers = p_numbers

    self.n = len(self.p_numbers)
    self.r_numbers = sample(list(range(len(self.p_numbers))), self.r)
    self.U_r = QuantumCircuit()
    for r_number in self.r_numbers:
      self.U_r += self.U_power(self.theta, self.phi, self.lam, self.p_numbers[r_number])

  def encode(self, message):
    qc = message.copy()
    qc += self.U_r
    qc.barrier()
    return qc

  def decode(self, message):
    qc = message.copy()
    for r_number in self.r_numbers:
      qc += self.U_power(-self.theta, -self.phi, -self.lam, self.p_numbers[r_number])
    qc.barrier()
    return qc
    