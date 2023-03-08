#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from elgamal.participant import Participant
from qiskit import QuantumCircuit

## The Sender entity in the ElGamal implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Sender(Participant):
  ## Constructor
  def __init__(self, name, u1, u2):
    super().__init__(name, u1, u2)

  ## Set message
  def set_message(self, message):
    self.message = message

  ## Compute shared secret
  def compute_shared_secret(self, e_b):
    y1, y2 = self.private_key
    power_1 = self.u1.power(y1)
    power_2 = self.u2.power(y2)
    
    self.shared_secret = QuantumCircuit(1, name='shared_secret')
    self.shared_secret.append(power_2, [0])
    self.shared_secret.append(e_b, [0])
    self.shared_secret.append(power_1, [0])

  ## Encrypts the message and returns it
  def get_encripted_message(self):
    encripted_message = QuantumCircuit(1)
    encripted_message.append(self.message, [0])
    encripted_message.append(self.shared_secret, [0])
    return encripted_message.decompose()
