
from quantum_solver.quantum_solver import QuantumSolver
from bb84.bb84_algorithm import BB84Algorithm
import time
import matplotlib.pyplot as plt
import numpy as np
from halo import Halo
from numpy.random import randint
from random import SystemRandom, randrange
import string
from alive_progress import alive_bar
from bb84.participant import N_BITS

BB84_SIMULATOR = 'BB84 SIMULATOR'

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
      try:
        self.is_selected_backend = self.qexecute.current_backend != None

        self.__show_options()
        self.__select_option()
      except Exception as exception:
        print('Exception:', exception)

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

  def __run_simulation(self):
    message = str(input('[&] Message (string): '))
    density = float(input('[&] Interception Density (float between 0 and 1): '))
    backend = self.qexecute.current_backend
    bits_size = len(message) * 5 * N_BITS
    execution_description = str(self.qexecute.current_backend)
    execution_description += ' with message "'
    execution_description += message + '" and density "' + str(density) + '"'
    halo_text = 'Running BB84 simulation in ' + execution_description
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      start_time = time.time()
      self.bb84_algorithm.run(message, backend, bits_size, density, True)
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  BB84 simulation runned in', str(time_ms), 'ms')
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)

  def __experimental_mode(self):
    DENSITY_MIN = 0
    DENSITY_MAX = 1
    DENSITY_STEP = 0.05
    DENSITY_RANGE = int((DENSITY_MAX - DENSITY_MIN) / DENSITY_STEP)
    LEN_MSG_LIMIT = 5 # 50
    REPETITION_INSTANCE = 10 # 30

    backend = self.qexecute.current_backend
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    image = np.zeros((DENSITY_RANGE + 1, LEN_MSG_LIMIT))
    x = list(range(1, LEN_MSG_LIMIT + 1, 1))
    y = list(np.arange(0, 1 + DENSITY_STEP, DENSITY_STEP))
    start_time = time.time()
    print('\nRunning BB84 Simulator Experiment (in ' + str(backend) + '):')

    try:
      with alive_bar(len(x) * len(y) * REPETITION_INSTANCE) as bar:
        for j, density in enumerate(y):
          for i, len_message in enumerate(x):
            for _ in range(REPETITION_INSTANCE):
              message = ''.join(SystemRandom().choice(possible_chars) for _ in range(len_message))
              bits_size = len(message) * 5 * N_BITS
              flag = self.bb84_algorithm.run(message, backend, bits_size, density, False)
              image[j][i] += 1 if flag else 0
              bar()
    except Exception as exception:
      print('Exception:', exception)

    time_m = (time.time() - start_time)
    print('\n[$] Experiment Finished in ' + str(time_m) + ' s!')
    plt.figure(num='BB84 Simulator - Experimental Mode' + str(backend))
    plt.pcolormesh(x, y, image, cmap='inferno', shading='auto')
    plt.colorbar(label='Times the protocol is determined safe')
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
      self.__run_simulation()
    elif option == 4 and self.is_selected_backend:
      self.__experimental_mode()
    else:
      print('[!] Invalid option, try again')
