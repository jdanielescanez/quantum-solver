#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

import binascii
from math import sqrt
from qiskit import execute, QuantumCircuit, transpile, assemble
from qiskit.quantum_info import Statevector
from qiskit.extensions import Initialize

from rsa_substitute.sender import Sender
from rsa_substitute.receiver import Receiver

RSA_SUBSTITUTE_SIMULATOR = 'RSA SUBSTITUTE SIMULATOR'

## An implementation of the RSA substitute protocol
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class RsaSubstituteAlgorithm:
  ## Run the implementation of RSA substitute protocol
  def run(self, measure_zero_prob, n_shots, backend, verbose):
    bob = Receiver('Bob', 6, 5)
    alice = Sender('Alice', 4, bob.p)

    message = self.generate_message(measure_zero_prob)

    alice_encoded_message = alice.encode(message)
    alice_bob_encoded_message = bob.encode(alice_encoded_message)
    bob_encoded_message = alice.decode(alice_bob_encoded_message)
    decoded_message = bob.decode(bob_encoded_message)
    decoded_message.measure(0, 0)

    test = transpile(decoded_message, backend)
    qobj = assemble(test)
    counts = backend.run(qobj, shots=n_shots).result().get_counts()
    if not '0' in counts.keys():
      counts['0'] = 0
    obtained_prob = counts['0'] / n_shots

    EPSILON = 5
    relative_error = abs(measure_zero_prob - obtained_prob)
    check_probability = relative_error <= 0.01 * EPSILON

    if verbose:
      print('\nOutput: ' + str(counts))

      print('\nInitial Message:')
      print(message)

      print('\nAlice-Encoded Message:')
      print(alice_encoded_message)

      print('\nAlice-and-Bob-Encoded Message:')
      print(alice_bob_encoded_message)

      print('\nBob-Encoded Message:')
      print(bob_encoded_message)

      print('\n💡 Decoded Message:')
      print(decoded_message)

      print('\nInput Probability:')
      print(measure_zero_prob)

      print('\nObtained Probability:')
      print(obtained_prob)

      print('\nRelative Error: ' + str(relative_error) + ' %')

      if check_probability:
        print('\n✅ The expected probability is obtained within an error range of ±' + str(EPSILON) + '%')
      else:
        print('\n❌ The expected probability is obtained with an error greater than ±' + str(EPSILON) + '%')

    return check_probability, relative_error

  def generate_message(self, measure_zero_prob):
    a1 = sqrt(measure_zero_prob)
    a2 = sqrt(1 - measure_zero_prob)
    psi = Statevector([complex(a1, 0), complex(a2, 0)])

    init_gate = Initialize(psi)
    init_gate.label = 'Init'
    qc = QuantumCircuit(1, 1)
    qc.append(init_gate, [0])
    qc.barrier()
    return qc
