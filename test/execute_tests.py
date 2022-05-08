
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from execution.qexecute import QExecute
from algorithms.qrand import QRand

class ExecuteTests(unittest.TestCase):
  def setUp(self):
    self.qExecute = QExecute()

  def test_is_guest_mode(self):
    self.assertTrue(self.qExecute.is_guest_mode)

  def test_set_current_backend(self):
    expected = 'aer_simulator'
    self.qExecute.set_current_backend(expected)

    self.assertEqual(str(self.qExecute.current_backend), expected)

  def test_run(self):
    self.qExecute.set_current_backend('aer_simulator')
    
    n = 100
    qRand = QRand()
    qRand_circuit = qRand.circuit(n)
    result = self.qExecute.run(qRand_circuit, 1)
    parsed_result = qRand.parse_result(result)

    self.assertTrue(parsed_result in range(2 ** n))


if __name__ == '__main__':
  unittest.main()
