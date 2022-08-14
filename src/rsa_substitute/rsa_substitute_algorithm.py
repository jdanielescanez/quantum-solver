#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

import binascii
from math import sqrt
from qiskit import execute, QuantumCircuit
from qiskit.quantum_info import Statevector

from rsa_substitute.sender import Sender
from rsa_substitute.receiver import Receiver

RSA_SUBSTITUTE_SIMULATOR = 'RSA SUBSTITUTE SIMULATOR'

## An implementation of the RSA substitute protocol
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class RsaSubstituteAlgorithm:
  ## Run the implementation of RSA substitute protocol
  def run(self, measure_zero_prob, n_shots, backend, verbose):
    alice = Receiver('Alice', 8, 4)
    bob = Sender('Bob', 8, alice.p)

    message = self.generate_message(measure_zero_prob)

    bob_encoded_message = bob.encode(message)
    alice_bob_encoded_message = alice.encode(bob_encoded_message)
    alice_encoded_message = bob.decode(alice_bob_encoded_message)
    decoded_message = alice.decode(alice_encoded_message)

    counts = backend.run(decoded_message, n_shots).result().get_counts()
    obtained_prob = counts['0'] / n_shots

    check_probability = measure_zero_prob * 0.9 < obtained_prob and \
                        obtained_prob < measure_zero_prob * 1.1

    if verbose:
      print('\nInitial Message:')
      print(message)

      print('\nBob-Encoded Message:')
      print(bob_encoded_message)

      print('Alice-and-Bob-Encoded Message:')
      print(alice_bob_encoded_message)

      print('Alice-Encoded Message:')
      print(alice_encoded_message)

      print('💡 Decoded Message:')
      print(decoded_message)

      print('\nInput Probability:')
      print(measure_zero_prob)

      print('\nObtained Probability:')
      print(obtained_prob)

      if check_probability:
        print('\n✅ The expected probability is obtained within an error range of ±10%')
      else:
        print('\n❌ The expected probability is obtained with an error greater than ±10%')

    return check_probability

  def generate_message(self, measure_zero_prob):
    a1 = sqrt(measure_zero_prob)
    a2 = sqrt(1 - measure_zero_prob)
    psi = Statevector([complex(a1, 0), complex(a2, 0)])

    init_gate = Initialize(psi)
    init_gate.label = 'Init'
    qc = QuantumCircuit()
    qc.append(init_gate, [0])
    qc.barrier()
    return qc
