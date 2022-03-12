
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from algorithms.algorithm import Algorithm
from algorithms.qrand import QRand
from algorithms.bernstein_vazirani import BernsteinVazirani

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

if __name__ == '__main__':
  unittest.main()
