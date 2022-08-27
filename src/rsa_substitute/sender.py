#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import QuantumCircuit
from rsa_substitute.participant import Participant
import numpy as np

## The Sender entity in the E91 implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Sender(Participant):
  ## Constructor
  def __init__(self, name='', r=0, p=[]):
    super().__init__(name)
    self.r = r
    self.p = p

    self.n = len(self.p)
    self.r_numbers = np.random.choice(list(range(self.n)), size=self.r, replace=True)

  def encode(self, message):
    qc = message.copy()
    for r_number in self.r_numbers:
      qc += self.p[r_number]
    qc.barrier()
    return qc

  def decode(self, message):
    qc = message.copy()
    for r_number in self.r_numbers:
      qc += self.p[r_number].inverse()
    qc.barrier()
    return qc
    