#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from abc import ABC, abstractmethod

## An abstract class of Quantum Algorithm, it can be used as template
class QAlgorithm(ABC):
  def __init__(self):
    ## The name of the algorithm
    self.name = 'QAlgorithm'
    ## A short description
    self.description = 'QAlgorithm Description'
    ## The required parameters for the algorithm
    self.parameters = [
      {
        'type': '',
        'description': '',
        'constraint': ''
      }
    ]
    ## How to parse the result of the circuit execution
    self.parse_result = lambda counts: counts
    ## How to parse the input parameters
    self.parse_parameters = lambda parameters: []
    
  ## An abstract method to check the parameters
  @abstractmethod
  def check_parameters(self, parameters):
    pass

  ## An abstract method to generate the circuit
  @abstractmethod
  def circuit(self):
    pass
