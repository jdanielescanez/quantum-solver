
from qiskit import QuantumCircuit
from math import log2

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

  def or_list(self, indexes, result, aux):
    self.reset(result)
    for a in indexes:
      self.or3(a, result, aux)
      self.reset(result)
      self.xor2(aux, result)

  def and3(self, a, b, result):
    self.reset(result)
    self.ccx(a, b, result)

  def and_list(self, indexes, result, aux):
    self.reset(result)
    self.not1(result)
    for a in indexes:
      self.and3(a, result, aux)
      self.reset(result)
      self.xor2(aux, result)

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

  def set_bin_reg(self, values, indexes):
    self.set_reg(values[::-1], indexes)

  def set_reg(self, values, indexes):
    for i, value in enumerate(values):
      if value == '1':
        self.set1(indexes[i])
      else:
        self.reset1(indexes[i])

  # output in indexes2
  def add_regs(self, indexes1, indexes2, carry, auxs):
    a_xor_b, a_prod_b, aux = auxs
    self.reset1(carry)
    for a, b in zip(indexes1, indexes2):
      self.reset1([a_xor_b, a_prod_b, aux])
      # a_xor_b = a xor b
      self.xor3(a, b, a_xor_b)
      # a_prod_b = a * b
      self.and3(a, b, a_prod_b)
      # aux = carry_in * (a xor b)
      self.and3(carry, a_xor_b, aux)

      # output = a xor b xor carry_in
      self.xor3(a_xor_b, carry, b)

      # carry_out = (a * b) + (carry_in * (a xor b))
      self.or3(a_prod_b, aux, carry)

  def encoder(self, inputs, outputs, aux):
    n = len(inputs)
    m = int(log2(n))
    assert(m == len(outputs))

    relative_indexes = [[inputs[num] for num in range(2 ** m) if (num >> i) & 1 == 1] for i in range(m)]
    
    for i in range(m):
      self.or_list(relative_indexes[i], outputs[i], aux)

  def decoder(self, inputs, outputs, flipped_inputs, aux):
    n = len(inputs)
    m = int(2 ** n)
    assert(m == len(outputs))

    self.xor2(inputs, flipped_inputs)
    self.not1(flipped_inputs)

    for i in range(m):
      tag = format(i, '0' + str(n) + 'b')[::-1]
      relative_inputs = [flipped_inputs[j] if x == '0' else inputs[j] for j, x in enumerate(tag)]
      self.and_list(relative_inputs, outputs[i], aux)

  ''' Modify inputs to its pruduct by its code '''
  def multiplexer(self, inputs, selectors, flipped_selectors, output, aux):
    n = len(inputs)
    m = int(log2(n))
    assert(m == len(selectors))

    self.xor2(selectors, flipped_selectors)
    self.not1(flipped_selectors)

    for i in range(n):
      tag = format(i, '0' + str(m) + 'b')[::-1]
      relative_selectors = [flipped_selectors[j] if x == '0' else selectors[j] for j, x in enumerate(tag)]
      self.and_list([inputs[i]] + relative_selectors, output, aux)
      self.swap(inputs[i], output)

    self.or_list(inputs, output, aux)
