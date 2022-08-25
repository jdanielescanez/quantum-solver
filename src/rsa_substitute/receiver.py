#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from rsa_substitute.participant import Participant
import numpy as np
from math import pi, sqrt

## The Receiver entity in the E91 implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Receiver(Participant):
  ## Constructor
  def __init__(self, name='', t=0, n=0):
    super().__init__(name)

    self.theta = pi / 3
    self.phi = pi / sqrt(2)
    self.lam = pi / sqrt(2)
    self.p_numbers = np.random.choice(list(range(2 ** t)), size=n, replace=True) # TODO comprobar que son n los elegidos (sample no permite repeticion, cambiar)

    self.e = self.U_power(self.theta, self.phi, self.lam, 1) # U_0
    self.p = [] # U_{1..n}
    for p_number in self.p_numbers: 
      self.p.append(self.U_power(self.theta, self.phi, self.lam, p_number))
    
  def encode(self, message):
    qc = message.copy()
    qc += self.e
    for p_i in self.p:
      qc += p_i
    qc.barrier()
    return qc

  def decode(self, message):
    qc = message.copy()
    qc += self.U_power(-self.theta, -self.phi, -self.lam, 1)
    for p_number in self.p_numbers: 
      qc += self.U_power(-self.theta, -self.phi, -self.lam, p_number)
    qc.barrier()
    return qc
