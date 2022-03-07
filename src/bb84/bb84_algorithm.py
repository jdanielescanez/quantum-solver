
from qiskit import QuantumCircuit, assemble
from bb84.sender import Sender
from bb84.reciever import Reciever
import binascii

BB84_SIMULATOR = 'BB84 SIMULATOR'

class BB84Algorithm:
  def __generate_key(self, backend, original_bits_size):
    # Encoder Alice
    alice = Sender('Alice', original_bits_size)
    alice.set_values()
    alice.set_axes()
    message = alice.encode_quantum_message()

    alice.show_values()
    alice.show_axes()

    # Interceptor Eve
    eve = Reciever('Eve', original_bits_size)
    eve.set_axes()
    message = eve.decode_quantum_message(message, self.measure_density, backend)

    eve.show_values()
    eve.show_axes()

    # Decoder Bob
    bob = Reciever('Bob', original_bits_size)
    bob.set_axes()
    message = bob.decode_quantum_message(message, 1, backend)

    bob.show_values()
    bob.show_axes()

    # Alice - Bob Remove Garbage
    alice_axes = alice.axes # Alice share her axes
    bob_axes = bob.axes # Bob share his axes

    # Delete the difference
    alice.remove_garbage(bob_axes)
    bob.remove_garbage(alice_axes)

    alice.show_key()
    bob.show_key()

    # Bob share some values of the key to check
    SHARED_SIZE = round(0.5 * len(bob.key))
    shared_key = bob.key[:SHARED_SIZE]
    print('\nShared Bob Key:')
    print(shared_key, '\n')

    # Alice check the shared key
    if alice.check_key(shared_key):
      shared_size = len(shared_key)
      alice.confirm_key(shared_size)
      bob.confirm_key(shared_size)
      print('Secure!')
    else:
      print('Not secure!')
    
    return alice, bob

  def run(self, message, backend, original_bits_size, measure_density):
    self.original_bits_size = original_bits_size
    self.measure_density = measure_density

    alice, bob = self.__generate_key(backend, original_bits_size)
    if not (alice.safe_key and bob.safe_key):
      print('Message not send')
      return 

    alice.generate_otp()
    bob.generate_otp()

    print('Message:')
    print(message)

    encoded_message = alice.encode_otp_message(message)
    print('Encoded Message:')
    print(encoded_message)

    decoded_message = bob.decode_otp_message(encoded_message)
    print('Decoded Message:')
    print(decoded_message)
