#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from subroutine.qpe.qpe import QPE
from subroutine.simon.simon import Simon
from subroutine.shor.shor import Shor
from algorithms.qalgorithm_manager import QAlgorithmManager

class SubroutineManager(QAlgorithmManager):
  def __init__(self):
    super().__init__()
    self.algorithms = [
      QPE(),
      Simon(),
      Shor()
    ]
