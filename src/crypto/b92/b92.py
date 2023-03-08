#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from quantum_solver.quantum_solver import QuantumSolver
from b92.b92_algorithm import B92Algorithm
import time
import matplotlib.pyplot as plt
import numpy as np
from halo import Halo
from numpy.random import randint
from random import SystemRandom, randrange
import string
from alive_progress import alive_bar

B92_SIMULATOR = 'B92 SIMULATOR'

## Main class of B92 Simulator
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class B92:
  ## Constructor
  def __init__(self, token):
    ## The implemented protocol
    self.b92_algorithm = B92Algorithm()
    ## The IBMQ Experience token
    self.token = token

  ## Print header, get an QExecute and run main menu
  def run(self):
    ## A QExecute instance to execute the simulation
    self.qexecute = QuantumSolver(self.token).get_qexecute()
    self.__main_menu()

  ## Loop to run the main menu
  def __main_menu(self):
    while True:
      try:
        ## If a current backend has been selected
        self.is_selected_backend = self.qexecute.current_backend != None

        self.__show_options()
        self.__select_option()
      except Exception as e:
        pass

  ## Main menu
  def __show_options(self):
    is_guest_mode = self.qexecute.is_guest_mode()
    guest_mode_string = ' (Guest Mode)' if is_guest_mode else ''
    len_guest_mode_string = len(guest_mode_string)
    print('\n' + B92_SIMULATOR + guest_mode_string)
    print('=' * (len(B92_SIMULATOR) + len_guest_mode_string) + '\n')
    print('[1] See available Backends')
    print('[2] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
    if self.is_selected_backend:
      print('[3] Run Algorithm')
    if self.is_selected_backend:
      print('[4] Experimental mode')
    print('[0] Exit\n')

  ## Run B92 simulation once
  def __run_simulation(self):
    message = str(input('[&] Message (string): '))
    density = float(input('[&] Interception Density (float between 0 and 1): '))
    backend = self.qexecute.current_backend
    N_BITS = 6
    bits_size = len(message) * 5 * N_BITS
    execution_description = str(self.qexecute.current_backend)
    execution_description += ' with message "'
    execution_description += message + '" and density "' + str(density) + '"'
    halo_text = 'Running B92 simulation in ' + execution_description
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      start_time = time.time()
      self.b92_algorithm.run(message, backend, bits_size, density, N_BITS, True)
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  B92 simulation runned in', str(time_ms), 'ms')
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)

  ## Run an experiment of B92 simulation
  def __experimental_mode(self, len_msg_limit=5, density_step=0.05, repetition_instance=10):
    STEP_MSG = 10
    DENSITY_MIN = 0
    DENSITY_MAX = 1
    DENSITY_RANGE = int((DENSITY_MAX - DENSITY_MIN) / density_step)
    backend = self.qexecute.current_backend
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    image = np.zeros((DENSITY_RANGE + 1, len_msg_limit // STEP_MSG))
    x = list(range(STEP_MSG, len_msg_limit + 1, STEP_MSG))
    y = list(np.arange(0, 1 + density_step, density_step))
    start_time = time.time()
    print('\nRunning B92 Simulator Experiment (in ' + str(backend) + '):')

    try:
      with alive_bar(len(x) * len(y) * repetition_instance) as bar:
        for j, density in enumerate(y):
          for i, len_message in enumerate(x):
            for _ in range(repetition_instance):
              message = ''.join(SystemRandom().choice(possible_chars) for _ in range(len_message))
              bits_size = len(message) * 5
              flag = self.b92_algorithm.run(message, backend, bits_size, density, 1, False)
              image[j][i] += 1 if flag else 0
              bar()
          
    except Exception as exception:
      print('Exception:', exception)

    time_m = (time.time() - start_time)
    print('\n[$] Experiment Finished in ' + str(time_m) + ' s!')
    print('\n💡 Output:\n\nx: ' + str(x) + '\n\ny: ' + str(y))
    print('\nImage:\n' + str(image) + '\n')
    plt.figure(num='B92 Simulator - Experimental Mode [' + str(backend) + ']')
    plt.pcolormesh(x, y, image, cmap='inferno', shading='auto')
    plt.colorbar(label='Times the protocol is determined safe')
    plt.xlabel('Message Length (number of bits)')
    plt.ylabel('Interception Density')
    plt.show()

  ## Select the option for main menu
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
      len_msg_limit = int(input('[&] Specify maximum message length (number of bits): '))
      density_step = float(input('[&] Specify density step: '))
      repetition_instance = int(input('[&] Specify number of repetitions for each instance: '))

      if len_msg_limit <= 0:
        raise ValueError('Maximum message length must be positive (> 0)')
      elif repetition_instance <= 0:
        raise ValueError('Number of repetitions for each instance must be positive (> 0)')
      elif density_step < 0 or density_step > 1:
        raise ValueError('Density step must be between 0 and 1 (∈ [0, 1])')
      else:
        if 1.0 % density_step != 0:
          density_step = 1 / round(1 / density_step)
        self.__experimental_mode(len_msg_limit, density_step, repetition_instance)
    else:
      print('[!] Invalid option, try again')
