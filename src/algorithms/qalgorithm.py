#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from abc import ABC, abstractmethod

## An abstract class of Quantum Algorithm, it can be used as template
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
