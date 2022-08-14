#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from rsa_substitute.participant import Participant
from random import random, sample
from math import pi

## The Sender entity in the E91 implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Sender(Participant):
  ## Constructor
  def __init__(self, name='', r=0, p_a=[]):
    super().__init__(name)
    self.r = r
    self.p_a = p_a

    TURN = 2 * pi
    self.theta = TURN * random()
    self.phi = TURN * random()
    self.lam = TURN * random()

    self.n = len(self.p_a)
    self.r_numbers = sample(list(range(len(self.p_a))), self.r)
    self.U_r = QuantumCircuit()
    for r_number in self.r_numbers:
      self.U_r += self.U_power(self.theta, self.phi, self.lam, self.p_a[r_number])

  def encode(self, message):
    message += self.U_r
    message.barrier()
    return message

  def decode(self, message):
    for r_number in self.r_numbers:
      message += self.U_power(-self.theta, -self.phi, -self.lam, self.p_a[r_number])
    message.barrier()
    return message
    