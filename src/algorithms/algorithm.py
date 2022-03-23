
from abc import ABC, abstractmethod
from qiskit import QuantumCircuit

class Algorithm(ABC):
  def __init__(self):
    self.name = 'Algorithm'
    self.description = 'Algorithm Description'
    self.parameters = []
    self.parse_result = lambda counts: counts
    self.parse_parameters = lambda parameters: []
    
  @abstractmethod
  def check_parameters(self, parameters):
    pass

  @abstractmethod
  def circuit(self):
    pass
