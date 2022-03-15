
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from bb84.participant import Participant
from bb84.sender import Sender
from bb84.reciever import Reciever

ALICE = 'Alice'
BOB = 'Bob'
ORIGINAL_BITS_SIZE = 20
EXAMPLE_LIST = [1, 0, 0, 1, 0, 1, 1]

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

  def test_values(self):
    self.sender.set_values(EXAMPLE_LIST)
    self.reciever.set_values(EXAMPLE_LIST)

    self.assertEqual(self.sender.values, EXAMPLE_LIST)
    self.assertEqual(self.reciever.values, EXAMPLE_LIST)

    self.sender.set_values()
    self.reciever.set_values()

    self.assertTrue(isinstance(self.sender.values, list) and \
                    len(self.sender.values) == ORIGINAL_BITS_SIZE)
    self.assertTrue(isinstance(self.reciever.values, list) and \
                    len(self.reciever.values) == ORIGINAL_BITS_SIZE)

    assert self.sender.show_values is not None
    assert self.reciever.show_values is not None

  def test_axes(self):
    self.sender.set_axes(EXAMPLE_LIST)
    self.reciever.set_axes(EXAMPLE_LIST)

    self.assertEqual(self.sender.axes, EXAMPLE_LIST)
    self.assertEqual(self.reciever.axes, EXAMPLE_LIST)

    self.sender.set_axes()
    self.reciever.set_axes()

    self.assertTrue(isinstance(self.sender.axes, list) and \
                    len(self.sender.axes) == ORIGINAL_BITS_SIZE)
    self.assertTrue(isinstance(self.reciever.axes, list) and \
                    len(self.reciever.axes) == ORIGINAL_BITS_SIZE)

    assert self.sender.show_axes is not None
    assert self.reciever.show_axes is not None

if __name__ == '__main__':
  unittest.main()
