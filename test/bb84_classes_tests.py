
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from bb84.participant import Participant
from bb84.sender import Sender
from bb84.reciever import Reciever
from qiskit import Aer

ALICE = 'Alice'
BOB = 'Bob'
EXAMPLE_LIST_1 = [1, 0, 0, 1, 0, 1, 1]
EXAMPLE_LIST_2 = [1, 1, 0, 0, 0, 1, 0]
ORIGINAL_BITS_SIZE = len(EXAMPLE_LIST_1)
INDEX_SHARED_KEY = 2

def is_lambda(x):
  return callable(x) and x.__name__ == '<lambda>'

class ClassesTests(unittest.TestCase):
  def setUp(self):
    self.sender = Sender(ALICE, ORIGINAL_BITS_SIZE)
    self.reciever = Reciever(BOB, ORIGINAL_BITS_SIZE)
    
  @unittest.expectedFailure
  def test_participant():
    participant = Participant('Participant', ORIGINAL_BITS_SIZE)

  def test_name(self):
    self.assertEqual(self.sender.name, ALICE)
    self.assertEqual(self.reciever.name, BOB)

  def test_original_bits_size(self):
    self.assertEqual(self.sender.original_bits_size, ORIGINAL_BITS_SIZE)
    self.assertEqual(self.reciever.original_bits_size, ORIGINAL_BITS_SIZE)

  def test_setter_values(self):
    self.sender.set_values(EXAMPLE_LIST_1)
    self.reciever.set_values(EXAMPLE_LIST_1)

    self.assertEqual(self.sender.values, EXAMPLE_LIST_1)
    self.assertEqual(self.reciever.values, EXAMPLE_LIST_1)

  def test_set_random_values(self):
    self.sender.set_values()
    self.reciever.set_values()

    self.assertTrue(isinstance(self.sender.values, list) and \
                    len(self.sender.values) == ORIGINAL_BITS_SIZE)
    self.assertTrue(isinstance(self.reciever.values, list) and \
                    len(self.reciever.values) == ORIGINAL_BITS_SIZE)

  def test_show_values(self):
    self.assertTrue(self.sender.show_values is not None)
    self.assertTrue(self.reciever.show_values is not None)

  def test_setter_axes(self):
    self.sender.set_axes(EXAMPLE_LIST_1)
    self.reciever.set_axes(EXAMPLE_LIST_1)

    self.assertEqual(self.sender.axes, EXAMPLE_LIST_1)
    self.assertEqual(self.reciever.axes, EXAMPLE_LIST_1)

  def test_set_random_axes(self):
    self.sender.set_axes()
    self.reciever.set_axes()

    self.assertTrue(isinstance(self.sender.axes, list) and \
                    len(self.sender.axes) == ORIGINAL_BITS_SIZE)
    self.assertTrue(isinstance(self.reciever.axes, list) and \
                    len(self.reciever.axes) == ORIGINAL_BITS_SIZE)

  def test_show_axes(self):
    self.assertTrue(self.sender.show_axes is not None)
    self.assertTrue(self.reciever.show_axes is not None)

  def test_remove_garbage(self):
    self.sender.set_values(EXAMPLE_LIST_1)
    self.reciever.set_values(EXAMPLE_LIST_2)
    self.sender.set_axes(EXAMPLE_LIST_1)
    self.reciever.set_axes(EXAMPLE_LIST_2)

    self.sender.remove_garbage(EXAMPLE_LIST_2)
    self.reciever.remove_garbage(EXAMPLE_LIST_1)

  def test_check_key(self):
    self.test_remove_garbage()
    shared_key = self.reciever.key[:INDEX_SHARED_KEY]
    self.assertTrue(self.sender.check_key(shared_key))

  def test_confirm_key(self):
    self.test_check_key()
    shared_key = self.reciever.key[:INDEX_SHARED_KEY]
    self.sender.confirm_key(len(shared_key))

  def test_safe_key(self):
    self.test_confirm_key()
    self.assertTrue(self.sender.safe_key)

  def test_show_key(self):
    self.test_safe_key()
    self.assertTrue(self.sender.show_key is not None)

  def test_generate_otp(self):
    self.test_safe_key()
    self.sender.generate_otp()
    self.assertTrue(isinstance(self.sender.otp, list))

  def test_show_otp(self):
    self.test_generate_otp()
    self.assertTrue(self.sender.show_otp is not None)

  def test_xor_otp_message(self):
    self.test_generate_otp()
    msg = 'qwertyuiopasdfghjklñzxcvbnm012345789QWERTYUIOPASDFGHJKLÑZXCVBNM,._-'
    encoded_msg = self.sender.xor_otp_message(msg)
    decoded_msg = self.sender.xor_otp_message(encoded_msg)
    self.assertEqual(decoded_msg, msg)

  def test_encode_quantum_message(self):
    self.test_set_random_axes()
    self.test_set_random_values()

    self.msg = self.sender.encode_quantum_message()

    for i, qc in enumerate(self.msg):
      for gate in qc.data:
        if gate[0].name == 'x':
          self.assertTrue(self.sender.values[i] == 1)
        if gate[0].name == 'h':
          self.assertTrue(self.sender.axes[i] == 1)

  def test_decode_quantum_message(self):
    self.test_encode_quantum_message()

    backend = Aer.get_backend('aer_simulator')
    self.msg = self.reciever.decode_quantum_message(self.msg, 1, backend)

    for i in self.reciever.axes:
      if self.reciever.axes[i] == self.sender.axes[i]:
        self.assertEqual(self.reciever.values[i], self.sender.values[i])

if __name__ == '__main__':
  unittest.main()
