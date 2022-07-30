#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from abc import ABC, abstractmethod

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from numpy.random import randint, choice
from math import ceil
from math import sqrt
import re

## An abstract class of a participant entity in the BB84 implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Participant(ABC):
  ## Constructor
  @abstractmethod
  def __init__(self, name='', original_bits_size=0, qr=QuantumRegister(2, name="qr"), cr=ClassicalRegister(4, name="cr")):
    ## The name of the participant
    self.name = name
    ## The original size of the message
    self.original_bits_size = original_bits_size
    ## The quantum register
    self.qr = qr
    ## The classical register
    self.cr = cr
    ## The values of the participant
    self.values = []
    ## The axes of the participant (chosen measurements)
    self.axes = None
    ## The key of the participant
    self.key = None
    ## If the key is determined safe
    self.is_safe_key = False
    ## The otp of the participant
    self.otp = None
    ## The associated measurements
    self.measurements = {}

  @abstractmethod
  def _calculate_measurements(self):
    pass

  ## Chosen measurements setter
  def set_axes(self, axes=None):
    self._calculate_measurements()
    if axes == None:
      self.axes = []
      for _ in range(self.original_bits_size):
        random_measurement = str(choice(list(self.measurements.keys())))
        self.axes.append(random_measurement)
    else:
      self.axes = axes

  ## Print values
  def show_values(self):
    print('\n' + self.name, 'Values:')
    print(self.values)

  ## Print chosen measurements
  def show_axes(self):
    print('\n' + self.name, 'Chosen Measurements:')
    print(self.axes)

  def show_measurements(self):
    print('\n' + self.name, 'Measurements:')
    for measurement_tag in self.measurements.keys():
      print(measurement_tag)
      print(str(self.measurements[measurement_tag]), '\n')
  
  ## Print key
  def show_key(self):
    print('\n' + self.name, 'Key:')
    print(self.key)

  ## Print otp
  def show_otp(self):
    print('\n' + self.name, 'OTP:')
    print(self.otp)

  def check_corr(self, corr):
    ideal_corr = - 2 * sqrt(2)
    return 1.1 * ideal_corr <= corr and corr <= 0.9 * ideal_corr

  ## Use the rest of the key and validate it
  def confirm_key(self):
    self.is_safe_key = True

  ## Generate an One-Time Pad
  def generate_otp(self, n_bits):
    self.otp = []
    for i in range(ceil(len(self.key) / n_bits)):
      bits_string = ''.join(map(str, self.key[i * n_bits: (i + 1) * n_bits]))
      self.otp.append(int(bits_string, 2))

  ## Performs an XOR operation between the message and the One-Time Pad
  def xor_otp_message(self, message):
    final_message = ''
    CHR_LIMIT = 1114112
    if len(self.otp) > 0:
      for i, char in enumerate(message):
        final_message += chr((ord(char) ^ self.otp[i % len(self.otp)]) % CHR_LIMIT)
    return final_message
