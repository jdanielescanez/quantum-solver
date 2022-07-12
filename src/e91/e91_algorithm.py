#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from e91.sender import Sender
from e91.receiver import Receiver
from e91.eavesdropper import Eveasdropper
import binascii

E91_SIMULATOR = 'E91 SIMULATOR'

## An implementation of the E91 protocol
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class E91Algorithm:
  ## Append the simplest (and maximal) example of quantum entanglement
  def get_bell_pair(self, qr, cr):
    circuit = QuantumCircuit(qr, cr)

    circuit.x([qr[0], qr[1]])
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    return circuit

  ## Generate a key for Alice and Bob
  def __generate_key(self, backend, original_bits_size, verbose):
    qr = QuantumRegister(2, name="qr")
    cr = ClassicalRegister(4, name="cr")
    singlet = self.get_bell_pair(qr, cr)

    alice = Sender('Alice', original_bits_size, qr, cr)
    alice.set_axes()

    eve = Eveasdropper('Eve', original_bits_size, qr, cr)
    eve.set_axes()
    
    bob = Receiver('Bob', original_bits_size, qr, cr)
    bob.set_axes()

    circuits = []
    for i in range(original_bits_size):
      eve_measure = eve.measurements[eve.axes[i][0]] + eve.measurements[eve.axes[i][1]]
      alice_measure = alice.measurements[alice.axes[i]]
      bob_measure = bob.measurements[bob.axes[i]]
      circuit = singlet + eve_measure + alice_measure + bob_measure
      circuit.name = str(i) + ':' + alice.axes[i] + '_' + bob.axes[i] + '_' + eve.axes[i][0] + '-' + eve.axes[i][1]
      circuits.append(circuit)

    result = execute(circuits, backend=backend, shots=1).result()
        
    alice.create_values(result, circuits)
    bob.create_values(result, circuits)
    eve.create_values(result, circuits)

    # Public measurements
    alice.create_key(bob.axes, result, circuits)
    bob.create_key(alice.axes, result, circuits)
    eve.create_key(alice.axes, bob.axes, result, circuits)

    # Bob share some values of the key to check
    SHARED_SIZE = round(0.5 * len(bob.key))
    shared_key = bob.key[:SHARED_SIZE]

    keyLength = len(alice.key)
    # Number of mismatching bits in the keys of Alice and Bob
    abKeyMismatches = 0
    # Number of mismatching bits in the keys of Eve and Alice
    eaKeyMismatches = 0
    # Number of mismatching bits in the keys of Eve and Bob
    ebKeyMismatches = 0

    for j in range(keyLength):
      if alice.key[j] != bob.key[j]: 
        abKeyMismatches += 1
      if eve.key[j][0] != alice.key[j]:
        eaKeyMismatches += 1
      if eve.key[j][1] != bob.key[j]:
        ebKeyMismatches += 1

    print("EY:", keyLength)
    # Eve's knowledge of Bob's key
    eaKnowledge = (keyLength - eaKeyMismatches) / keyLength
    # Eve's knowledge of Alice's key
    ebKnowledge = (keyLength - ebKeyMismatches) / keyLength

    if verbose:
      alice.show_values()
      alice.show_measurements()
      alice.show_axes()

      eve.show_values()
      eve.show_measurements()
      eve.show_axes()

      bob.show_values()
      bob.show_measurements()
      bob.show_axes()

      alice.show_key()
      bob.show_key()

      print('\nNumber of mismatching bits: ' + str(abKeyMismatches) + '\n')

      print('\nShared Bob Key:')
      print(shared_key)

      print('\nEve\'s knowledge of Alice\'s key: ' + str(round(eaKnowledge * 100, 2)) + '%')
      print('Eve\'s knowledge of Bob\'s key: ' + str(round(ebKnowledge * 100, 2)) + '%')

    # Alice check the shared key
    if alice.check_key(shared_key):
      shared_size = len(shared_key)
      alice.confirm_key(shared_size)
      bob.confirm_key(shared_size)
      
      if verbose:
        # CHSH inequality test
        alice.show_corr()
        bob.show_corr()

        # Length key test
        alice.show_len_key()
        bob.show_len_key()

        print('\nCHSH correlation should be close to -2 * √2 ~= -2.8282')
        print('Length key should be close to (2 / 9) *', original_bits_size, \
              '/ 2 =', original_bits_size, '/ 9 =', original_bits_size / 9)

        print('\nFinal Keys')
        alice.show_key()
        bob.show_key()
        print('\nSecure Communication!')
    elif verbose:
      print('\nUnsecure Communication! Eve has been detected intercepting messages\n')
    
    return alice, bob

  ## Run the implementation of E91 protocol
  def run(self, message, backend, original_bits_size, measure_density, n_bits, verbose):
    ## The original size of the message
    self.original_bits_size = original_bits_size
    ## The probability of an interception occurring
    self.measure_density = measure_density

    alice, bob = self.__generate_key(backend, original_bits_size, verbose)
    if not (alice.is_safe_key and bob.is_safe_key):
      if verbose:
        print('❌ Message not send')
      return False

    alice.generate_otp(n_bits)
    bob.generate_otp(n_bits)

    encoded_message = alice.xor_otp_message(message)
    decoded_message = bob.xor_otp_message(encoded_message)

    if verbose:
      alice.show_otp()
      bob.show_otp()

      print('\nInitial Message:')
      print(message)

      print('Encoded Message:')
      print(encoded_message)

      print('💡 Decoded Message:')
      print(decoded_message)

      if message == decoded_message:
        print('\n✅ The initial message and the decoded message are identical')
      else:
        print('\n❌ The initial message and the decoded message are different')

    return True
