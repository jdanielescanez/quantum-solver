
from subroutine.qpe.qpe import QPE
from algorithms.qalgorithm_manager import QAlgorithmManager

class SubroutineManager(QAlgorithmManager):
  def __init__(self):
    super().__init__()
    self.algorithms = [
      QPE()
    ]
