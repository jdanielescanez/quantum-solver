#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Final de Grado: QuantumSolver

from algorithms.qrand import QRand
from algorithms.deutsch_jozsa import DeutschJozsa
from algorithms.bernstein_vazirani import BernsteinVazirani
from algorithms.grover import Grover
from algorithms.quantum_teleportation import QuantumTeleportation
from algorithms.superdense_coding import SuperdenseCoding

## The component that manages the quantum algorithms for QuantumSolver
class QAlgorithmManager:
  ## Constructor
  def __init__(self):
    self.current_algorithm = None
    self.parameters = None
    self.algorithms = [
      QRand(),
      DeutschJozsa(),
      BernsteinVazirani(),
      Grover(),
      QuantumTeleportation(),
      SuperdenseCoding()
    ]

  ## Current algorithm setter
  def set_current_algorithm(self, i):
    if i < len(self.algorithms):
      self.current_algorithm = self.algorithms[i]

  ## Print the available algorithms
  def print_available_algorithms(self):
    print('\nAvaliable algorithms:')
    for i in range(len(self.algorithms)):
      algorithm = self.algorithms[i]
      print('[' + str(i + 1) + ']\tName:', algorithm.name)
      print('\tDescription:', algorithm.description)
      print('\tParameters:')
      self.__print_parameters(algorithm.parameters)
  
  ## Print the needed parameters
  def __print_parameters(self, parameters):
    for parameter in parameters:
        print('\t    ' + parameter['description'] + ' (' + \
            parameter['type'] + ')\n')

  ## Algorithm selection menu
  def select_algorithm(self):
    self.parameters = None
    range_algorithms = '[1 - ' + str(len(self.algorithms)) + ']'
    index = -2
    while index < 0 or index >= len(self.algorithms):
      msg = '[&] Select a algorithm of the list ' + str(range_algorithms) + ': '
      index = int(input(msg)) - 1
      if index == -1:
        self.current_algorithm = None
        print('[$] Algorithm not selected')
        return
      if index < 0 or index >= len(self.algorithms):
        index = -1
        print('[!] The algorithm must be one of the list', range_algorithms)
      else:
        self.current_algorithm = self.algorithms[index]
        print('[$]', self.current_algorithm.name, 'selected')

  ## Parameters selection menu
  def select_parameters(self):
    self.parameters = []
    for parameter in self.current_algorithm.parameters:
      input_parameter = input('[&] Specify parameter: ' + \
          parameter['description'] + ' [' + parameter['type'] + ']\n' +
              ' ' * 4 + '(' + parameter['constraint'] + '): ')
      self.parameters.append(input_parameter)
    if self.current_algorithm.check_parameters(self.parameters):
      self.parameters = self.current_algorithm.parse_parameters(self.parameters)
    else:
      self.parameters = None
      print('\n[!] Error checking parameters: Read carefully the constraints and try again')

  ## Current algorithm circuit getter
  def get_circuit(self):
    if self.current_algorithm == None:
      print('[$] Algorithm not selected')
      return
    if self.parameters == None or len(self.current_algorithm.parameters) != len(self.parameters):
      print('[$] Parameters not selected')
      return
    return self.current_algorithm.circuit(*self.parameters)

  ## Result parser
  def parse_result(self, result):
    if self.current_algorithm != None:
      return self.current_algorithm.parse_result(result)
