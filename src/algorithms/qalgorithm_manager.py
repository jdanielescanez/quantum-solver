
from algorithms.qrand import QRand
from algorithms.bernstein_vazirani import BernsteinVazirani
from algorithms.deutsch_jozsa import DeutschJozsa
from algorithms.grover import Grover

class QAlgorithmManager:
  def __init__(self):
    self.current_algorithm = None
    self.parameters = None
    self.algorithms = [QRand(), DeutschJozsa(), BernsteinVazirani(), Grover()]

  def set_current_algorithm(self, i):
    if i < len(self.algorithms):
      self.current_algorithm = self.algorithms[i]

  def print_avaiable_algorithms(self):
    print('\nAvaliable algorithms:')
    for i in range(len(self.algorithms)):
      algorithm = self.algorithms[i]
      print('[' + str(i + 1) + ']\tName:', algorithm.name)
      print('\tDescription:', algorithm.description)
      print('\tParameters:')
      self.__print_parameters(algorithm.parameters)
  
  def __print_parameters(self, parameters):
    for parameter in parameters:
        print('\t    ' + parameter['description'] + ' (' + \
            parameter['type'] + ')\n')

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

  def get_circuit(self):
    if self.current_algorithm == None:
      print('[$] Algorithm not selected')
      return
    if self.parameters == None or len(self.current_algorithm.parameters) != len(self.parameters):
      print('[$] Parameters not selected')
      return
    return self.current_algorithm.circuit(*self.parameters)

  def parse_result(self, result):
    if self.current_algorithm != None:
      return self.current_algorithm.parse_result(result)
