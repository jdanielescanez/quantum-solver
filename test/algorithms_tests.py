
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from algorithms.qalgorithm import QAlgorithm
from algorithms.qalgorithm_manager import QAlgorithmManager

def is_lambda(x):
  return callable(x) and x.__name__ == '<lambda>'

class AlgorithmsTests(unittest.TestCase):
  def setUp(self):
    self.qAlgorithmManager = QAlgorithmManager()
    self.algorithms = self.qAlgorithmManager.algorithms

  @unittest.expectedFailure
  def test_algorithm(self):
    _ = QAlgorithm()

  def test_print_avaiable_algorithms(self):
    self.assertTrue(self.qAlgorithmManager.print_avaiable_algorithms is not None)

  def test_select_algorithm(self):
    self.assertTrue(self.qAlgorithmManager.select_algorithm is not None)

  def test_select_parameters(self):
    self.assertTrue(self.qAlgorithmManager.select_parameters is not None)

  def test_get_circuit(self):
    self.qAlgorithmManager.current_algorithm = None
    self.assertTrue(self.qAlgorithmManager.get_circuit() is None)
    self.qAlgorithmManager.current_algorithm = self.qAlgorithmManager.algorithms[0]
    self.assertTrue(self.qAlgorithmManager.get_circuit() is None)
    self.qAlgorithmManager.parameters = [1]
    self.assertTrue(self.qAlgorithmManager.get_circuit() is not None)

  def def_qalgorithm_parse_result(self):
    self.assertTrue(self.qAlgorithmManager.parse_result is not None)

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

  def test_parse_result(self):
    for algorithm in self.algorithms:
      self.assertTrue(is_lambda(algorithm.parse_result))

  def test_parse_parameters(self):
    for algorithm in self.algorithms:
      self.assertTrue(is_lambda(algorithm.parse_parameters))

  def test_circuit(self):
    for algorithm in self.algorithms:
      self.assertTrue(algorithm.circuit is not None)

if __name__ == '__main__':
  unittest.main()
