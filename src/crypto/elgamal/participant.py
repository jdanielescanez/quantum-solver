#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from abc import ABC, abstractmethod

from qiskit import QuantumCircuit
from numpy.random import randint
from math import ceil
from random import randrange
import sys

## An abstract class of a participant entity in the ElGamal implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Participant(ABC):
  ## Constructor
  @abstractmethod
  def __init__(self, name, u1, u2):
    ## The name of the participant
    self.name = name
    ## The first shared public parameter 
    self.u1 = u1
    ## The second shared public parameter 
    self.u2 = u2
    ## The private key of the participant
    self.private_key = None
    ## The public key of the participant
    self.public_key = None
    ## The shared key
    self.shared_secret = None
    ## The size limit
    self.SIZE_LIMIT = 10 ** 3

  ## Generate private and public key
  def generate_keys(self):
    x1 = randrange(1, self.SIZE_LIMIT)
    x2 = randrange(1, self.SIZE_LIMIT)
    self.private_key = (x1, x2)

    self.public_key = QuantumCircuit(1, name=(self.name + '_public_key'))
    self.public_key.append(self.u2.power(x2), [0])
    self.public_key.append(self.u1.power(x1), [0])

  ## Print private key
  def show_private_key(self):
    print('\n' + self.name, 'Private Key:')
    print(self.private_key)

  ## Print public key
  def show_public_key(self):
    print('\n' + self.name, 'Public Key:')
    print(self.public_key)

  ## Print dagger public key
  def show_dagger_public_key(self):
    print('\n' + self.name, 'Dagger Public Key:')
    print(self.public_key.inverse())
