
BB84_SIMULATOR = 'BB84 SIMULATOR'
N_BITS = 6

from quantum_solver.quantum_solver import QuantumSolver
from bb84.bb84_algorithm import BB84Algorithm
import time
import matplotlib.pyplot as plt
import numpy as np
from halo import Halo

class BB84:
  def __init__(self, token):
    self.bb84_algorithm = BB84Algorithm()
    self.token = token

  def run(self):
    self.__show_header()
    self.qexecute = QuantumSolver(self.token).get_qexecute()
    self.__main_menu()

  def __show_header(self):
    print('\n' + BB84_SIMULATOR + '\n' + '=' * len(BB84_SIMULATOR) + '\n')
    print('A BB84 simulator using Qiskit')
    print('WARNING: The BB84 simulator uses your personal IBM Quantum Experience')
    print('token to access to IBM hardware.')
    print('You can access to your API token or generate another one here:')
    print('https://quantum-computing.ibm.com/account\n')

  def __main_menu(self):
    while True:
      self.is_selected_backend = self.qexecute.current_backend != None

      self.__show_options()
      self.__select_option()

  def __show_options(self):
    print('\n' + BB84_SIMULATOR + '\n' + '=' * len(BB84_SIMULATOR) + '\n')
    print('[1] See available Backends')
    print('[2] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
    if self.is_selected_backend:
      print('[3] Run Algorithm')
    if self.is_selected_backend:
      print('[4] Experimental mode')
    print('[0] Exit\n')

  def __run(self):
    message = str(input('[&] Message (string): '))
    density = float(input('[&] Interception Density (float between 0 and 1): '))
    backend = self.qexecute.current_backend
    bits_size = len(message) * 2 ** N_BITS
    halo_text = 'Running BB84 simulation'
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      start_time = time.time()
      self.bb84_algorithm.run(message, backend, bits_size, density, True)
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  BB84 silumation runned in', str(time_ms), 'ms')
    except Exception as exception:
      halo.fail()
      print('Exception: ', exception)

  def __experimental_mode(self):
    backend = self.qexecute.current_backend
    instances = [
      ('Key', 0),
      ('SecretKey', 0.5),
      ('PASSword', 1)
    ]
    for message, density in instances:
      bits_size = len(message) * 2 ** N_BITS
      flag = self.bb84_algorithm.run(message, backend, bits_size, density, False)
      color = 'blue' if flag else 'red'
      plt.scatter(len(message), density, c=color)

    plt.xlabel('Message Length')
    plt.ylabel('Interception Density')
    plt.show()

  def __select_option(self):
    option = int(input('[&] Select an option: '))
    if option == 0:
      print()
      exit(0)
    elif option == 1:
      self.qexecute.print_avaiable_backends()
    elif option == 2:
      self.qexecute.select_backend()
    elif option == 3 and self.is_selected_backend:
      self.__run()
    elif option == 4 and self.is_selected_backend:
      self.__experimental_mode()
    else:
      print('[!] Invalid option, try again')
