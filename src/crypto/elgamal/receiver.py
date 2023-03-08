#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from elgamal.participant import Participant
from qiskit import QuantumCircuit

## The Receiver entity in the ElGamal implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Receiver(Participant):
  ## Constructor
  def __init__(self, name, u1, u2):
    super().__init__(name, u1, u2)

  ## Compute shared secret
  def compute_shared_secret(self, c1):
    b1, b2 = self.private_key
    power_1 = self.u1.power(b1)
    power_2 = self.u2.power(b2)

    self.shared_secret = QuantumCircuit(1, name='shared_secret')
    self.shared_secret.append(power_2, [0])
    self.shared_secret.append(c1, [0])
    self.shared_secret.append(power_1, [0])

  ## Decrypts the message and returns it
  def decrypt_message(self, encrypted_message):
    decripted_message = QuantumCircuit(1)
    decripted_message.append(encrypted_message, [0])
    decripted_message.append(self.shared_secret.inverse(), [0])
    return decripted_message.decompose()
