
from abc import ABC

from qiskit import QuantumCircuit
from numpy.random import randint
from math import ceil

class Participant(ABC):
  def __init__(self, name='', original_bits_size=0):
    self.name = name
    self.original_bits_size = original_bits_size
    self.values = None
    self.axes = None
    self.key = None
    self.safe_key = False
    self.otp = None

  def set_values(self, values=None):
    if values == None:
      self.values = list(randint(2, size=self.original_bits_size))
    else:
      self.values = values

  def set_axes(self, axes=None):
    if axes == None:
      self.axes = list(randint(2, size=self.original_bits_size))
    else:
      self.axes = axes

  def show_values(self):
    print('\n' + self.name, 'Values:')
    print(self.values)

  def show_axes(self):
    print('\n' + self.name, 'Axes:')
    print(self.axes)
  
  def show_key(self):
    print('\n' + self.name, 'Key:')
    print(self.key)

  def show_otp(self):
    print('\n' + self.name, 'OTP:')
    print(self.otp)

  def remove_garbage(self, another_axes):
    self.key = []
    for i in range(self.original_bits_size):
      if self.axes[i] == another_axes[i]:
        self.key.append(self.values[i])

  def check_key(self, shared_key):
    return shared_key == self.key[:len(shared_key)]

  def confirm_key(self, shared_size):
    self.key = self.key[shared_size:]
    self.safe_key = True

  def generate_otp(self, n_bits):
    self.otp = []
    for i in range(ceil(len(self.key) / n_bits)):
      bits_string = ''.join(map(str, self.key[i * n_bits: (i + 1) * n_bits]))
      self.otp.append(int(bits_string, 2))

  def xor_otp_message(self, message):
    final_message = ''
    CHR_LIMIT = 1114112
    if len(self.otp) > 0:
      for i, char in enumerate(message):
        final_message += chr((ord(char) ^ self.otp[i % len(self.otp)]) % CHR_LIMIT)
    return final_message
