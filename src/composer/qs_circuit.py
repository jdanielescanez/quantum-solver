
from qiskit import QuantumCircuit

class QSCircuit(QuantumCircuit):
  def __init__(self, size):
    self.size = size
    super().__init__(size, size)

  def not1(self, a):
    self.x(a)

  def not2(self, a, result):
    self.reset(result)
    self.cx(a, result)
    self.x(result)

  def or3(self, a, b, result):
    self.reset(result)
    self.x([a, b])
    self.ccx(a, b, result)
    self.x([a, b, result])

  def and3(self, a, b, result):
    self.reset(result)
    self.ccx(a, b, result)

  def nand3(self, a, b, result):
    self.and3(a, b, result)
    self.not1(result)

  # copy the source to the destiny if conditional
  def copy_if(self, conditional, source, destiny):
    for i in range(len(source)):
      self.and3(conditional, source[i], destiny[i])

  def xor2(self, a, result):
    self.cx(a, result)

  def xor3(self, a, b, result):
    self.reset(result)
    self.cx(b, result)
    self.cx(a, result)

  def swap2(self, a, b):
    self.swap(a, b)

  def shift_left(self, indexes):
    indexes.sort()
    self.swap(indexes[:-1], indexes[1:])
    
  def shift_right(self, indexes):
    indexes.sort(reverse=True)
    self.swap(indexes[:-1], indexes[1:])

  def reset1(self, a):
    self.reset(a)

  def set1(self, a):
    self.reset(a)
    self.x(a)

  def set_reg(self, values, indexes):
    for i, value in enumerate(values):
      if value == '1':
        self.set1(indexes[i])
      else:
        self.reset1(indexes[i])

