#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from qiskit import QuantumCircuit
from random import vonmisesvariate as random_angle
from qiskit.circuit.library import UGate
from crypto.elgamal.sender import Sender
from crypto.elgamal.receiver import Receiver
from qiskit.quantum_info import Statevector
import qiskit.quantum_info as qi
import numpy as np

ELGAMAL_SIMULATOR = 'ElGamal SIMULATOR'

## An implementation of the ElGamal protocol
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class ElGamalAlgorithm:
  ## Run the implementation of ElGamal protocol
  def run(self, message):
    msg_qc = QuantumCircuit(1, name='message')
    msg_sv = Statevector([complex(x) for x in message.split(',')])
    msg_qc.initialize(msg_sv)
    
    u1, u2 = self.public_keys_generation()

    # Receiver Bob
    bob = Receiver('Bob', u1, u2)
    bob.generate_keys()

    # Sender Alice
    alice = Sender('Alice', u1, u2)
    alice.set_message(msg_qc)
    alice.generate_keys()
    alice.compute_shared_secret(bob.public_key)

    # Encryption
    c1 = alice.public_key
    c2 = alice.get_encripted_message()

    # Decryption
    bob.compute_shared_secret(c1)
    decrypted_message = bob.decrypt_message(c2)

    encrypted_message = c2
    shared_secret = alice.shared_secret
    decrypted_message_sv = qi.Statevector.from_instruction(decrypted_message)
    encrypted_message_sv = qi.Statevector.from_instruction(encrypted_message)

    return msg_sv, encrypted_message, decrypted_message, encrypted_message_sv, decrypted_message_sv, alice, bob

  ## Gets random public matrices
  def public_keys_generation(self):
    u1 = QuantumCircuit(1, name='U1')
    u1.append(UGate(random_angle(0, 0), random_angle(0, 0), random_angle(0, 0)), [0])

    u2 = QuantumCircuit(1, name='U2')
    u2.append(UGate(random_angle(0, 0), random_angle(0, 0), random_angle(0, 0)), [0])

    return (u1, u2)
