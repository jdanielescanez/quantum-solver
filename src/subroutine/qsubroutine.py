#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from abc import abstractmethod
from algorithms.qalgorithm import QAlgorithm

## An abstract class of Quantum Subroutine, it can be used as template
class QSubroutine(QAlgorithm):
  def __init__(self):
    super.__init__(self)

  ## An abstract method to prepare the input
  @abstractmethod
  def preprocessing(self, parameters):
    pass

  ## An abstract method to process the output
  @abstractmethod
  def postprocessing(self, counts):
    pass
