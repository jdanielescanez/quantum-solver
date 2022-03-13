
from abc import ABC, abstractmethod
from qiskit import QuantumCircuit

class Algorithm(ABC):
  def __init__(self):
    self.name = 'Algorithm'
    self.description = 'Algorithm Description'
    self.parameters = []
    self.n_shots = 0
    self.parse_result = lambda counts: counts
    self.parse_parameters = lambda array: []

  @abstractmethod
  def circuit(self):
    pass
