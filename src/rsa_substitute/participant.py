#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from abc import ABC, abstractmethod

## An abstract class of a participant entity in the RSA substitute protocol implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Participant(ABC):
  ## Constructor
  @abstractmethod
  def __init__(self, name=''):
    ## The name of the participant
    self.name = name

  @abstractmethod
  def encode(self, message):
    pass
  
  @abstractmethod
  def decode(self, message):
    pass
