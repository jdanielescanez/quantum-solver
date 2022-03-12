# https://docs.python.org/3/library/unittest.html#organizing-test-code

import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from algorithms.algorithm import Algorithm
from algorithms.qrand import QRand
from algorithms.bernstein_vazirani import BernsteinVazirani

def is_lambda(x):
  return callable(x) and x.__name__ == '<lambda>'

class AlgorithmsTests(unittest.TestCase):
  @unittest.expectedFailure
  def test_algorithm():
      algorithm = Algorithm()

  def setUp(self):
    self.algorithms = [QRand(), BernsteinVazirani()]

  def test_name(self):
    for algorithm in self.algorithms:
      self.assertTrue(isinstance(algorithm.name, str))

  def test_description(self):
    for algorithm in self.algorithms:
      self.assertTrue(isinstance(algorithm.description, str))

  def test_parameters(self):
    for algorithm in self.algorithms:
      for parameter in algorithm.parameters:
        self.assertTrue(isinstance(parameter['type'], str))
        self.assertTrue(isinstance(parameter['description'], str))
        self.assertTrue(isinstance(parameter['constraint'], str))

  def test_n_shots(self):
    for algorithm in self.algorithms:
      self.assertTrue(isinstance(algorithm.n_shots, int))

  def test_parse_result(self):
    for algorithm in self.algorithms:
      self.assertTrue(is_lambda(algorithm.parse_parameters))

  def test_parse_parameters(self):
    for algorithm in self.algorithms:
      self.assertTrue(is_lambda(algorithm.parse_result))

  def test_circuit(self):
    for algorithm in self.algorithms:
      assert algorithm.circuit() is not None

if __name__ == '__main__':
  unittest.main()
