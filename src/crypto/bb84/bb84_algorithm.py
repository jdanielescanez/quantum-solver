#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from qiskit import QuantumCircuit
from crypto.bb84.sender import Sender
from crypto.bb84.receiver import Receiver
import binascii

BB84_SIMULATOR = 'BB84 SIMULATOR'

## An implementation of the BB84 protocol
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class BB84Algorithm:
  ## Generate a key for Alice and Bob
  def __generate_key(self, backend, original_bits_size, verbose):
    # Encoder Alice
    alice = Sender('Alice', original_bits_size)
    alice.set_values()
    alice.set_axes()
    message = alice.encode_quantum_message()

    # Interceptor Eve
    eve = Receiver('Eve', original_bits_size)
    eve.set_axes()
    message = eve.decode_quantum_message(message, self.measure_density, backend)

    # Decoder Bob
    bob = Receiver('Bob', original_bits_size)
    bob.set_axes()
    message = bob.decode_quantum_message(message, 1, backend)

    # Alice - Bob Remove Garbage
    alice_axes = alice.axes # Alice share her axes
    bob_axes = bob.axes # Bob share his axes

    # Delete the difference
    alice.remove_garbage(bob_axes)
    bob.remove_garbage(alice_axes)

    # Bob share some values of the key to check
    SHARED_SIZE = round(0.5 * len(bob.key))
    shared_key = bob.key[:SHARED_SIZE]

    if verbose:
      alice.show_values()
      alice.show_axes()

      eve.show_values()
      eve.show_axes()

      bob.show_values()
      bob.show_axes()

      alice.show_key()
      bob.show_key()

      print('\nShared Bob Key:')
      print(shared_key)

    # Alice check the shared key
    if alice.check_key(shared_key):
      shared_size = len(shared_key)
      alice.confirm_key(shared_size)
      bob.confirm_key(shared_size)
      if verbose:
        print('\nFinal Keys')
        alice.show_key()
        bob.show_key()
        print('\nSecure Communication!')
    elif verbose:
      print('\nUnsecure Communication! Eve has been detected intercepting messages\n')
    
    return alice, bob

  ## Run the implementation of BB84 protocol
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
