
from abc import ABC, abstractmethod
from qiskit import QuantumCircuit

class QAlgorithm(ABC):
  def __init__(self):
    self.name = 'QAlgorithm'
    self.description = 'QAlgorithm Description'
    self.parameters = [
      {
        'type': '',
        'description': '',
        'constraint': ''
      }
    ]
    self.parse_result = lambda counts: counts
    self.parse_parameters = lambda parameters: []
    
  @abstractmethod
  def check_parameters(self, parameters):
    pass

  @abstractmethod
  def circuit(self):
    pass
