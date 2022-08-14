#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from rsa_substitute.participant import Participant
from random import random, sample
from math import pi

## The Receiver entity in the E91 implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Receiver(Participant):
  ## Constructor
  def __init__(self, name='', t=0, n=0):
    super().__init__(name)

    TURN = 2 * pi
    self.theta = TURN * random()
    self.phi = TURN * random()
    self.lam = TURN * random()

    self.p_numbers = sample(list(range(2 ** t)), n)

    self.e = self.U_power(self.theta, self.phi, self.lam, 1) # U_0
    self.p = [] # U_{1..n}
    for p_number in self.p_numbers: 
      self.p.append(self.U_power(self.theta, self.phi, self.lam, p_number))

  def encode(self, message):
    for p_i in self.p:
      message += p_i
    message.barrier()
    return message

  def decode(self, message):
    for p_number in self.p_numbers: 
      message += self.U_power(-self.theta, -self.phi, -self.lam, p_number)
    message.barrier()
    return message
