#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from quantum_solver.quantum_solver import QuantumSolver
from e91.e91_algorithm import E91Algorithm
import time
import matplotlib.pyplot as plt
import numpy as np
from halo import Halo
from numpy.random import randint
from random import SystemRandom, randrange
import string
from alive_progress import alive_bar
from math import ceil
from e91.sender import Sender

E91_SIMULATOR = 'E91 SIMULATOR'

## Main class of E91 Simulator
## @see https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/awards/teach_me_qiskit_2018/e91_qkd/e91_quantum_key_distribution_protocol.ipynb
class E91:
  ## Constructor
  def __init__(self, token):
    ## The implemented protocol
    self.e91_algorithm = E91Algorithm()
    ## The IBMQ Experience token
    self.token = token

  ## Print header, get an QExecute and run main menu
  def run(self):
    self.__show_header()
    ## A QExecute instance to execute the simulation
    self.qexecute = QuantumSolver(self.token).get_qexecute()
    self.__main_menu()

  ## Print header
  def __show_header(self):
    print('\n' + E91_SIMULATOR + '\n' + '=' * len(E91_SIMULATOR) + '\n')
    print('A E91 simulator using Qiskit')
    print('WARNING: The E91 simulator uses your personal IBM Quantum Experience')
    print('token to access to IBM hardware.')
    print('You can access to your API token or generate another one here:')
    print('https://quantum-computing.ibm.com/account\n')
    print('You can also use the Guest Mode which only allows you to run ')
    print('quantum circuits in a local simulator ("aer_simulator").\n')

  ## Loop to run the main menu
  def __main_menu(self):
    while True:
      try:
        ## If a current backend has been selected
        self.is_selected_backend = self.qexecute.current_backend != None

        self.__show_options()
        self.__select_option()
      except Exception as _:
        pass

  ## Main menu
  def __show_options(self):
    is_guest_mode = self.qexecute.is_guest_mode()
    guest_mode_string = ' (Guest Mode)' if is_guest_mode else ''
    len_guest_mode_string = len(guest_mode_string)
    print('\n' + E91_SIMULATOR + guest_mode_string)
    print('=' * (len(E91_SIMULATOR) + len_guest_mode_string) + '\n')
    print('[1] See available Backends')
    print('[2] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
    if self.is_selected_backend:
      print('[3] Run Algorithm')
    if self.is_selected_backend:
      print('[4] Experimental mode')
    print('[0] Exit\n')

  def __show_options_experimental_mode(self):
    print('\nResults Experimental Mode')
    print('=========================')
    print('[1] See security graph')
    print('[2] See average correlation graph')
    print('[3] See average correlation check graph')
    print('[0] Exit\n')

  ## Run E91 simulation once
  def __run_simulation(self):
    message = str(input('[&] Message (string): '))
    density = float(input('[&] Interception Density (float between 0 and 1): '))
    backend = self.qexecute.current_backend
    N_BITS = 6
    bits_size = ceil(len(message) * 9 / 2 * N_BITS) # 2 / 9 because is the theorical value
    execution_description = str(self.qexecute.current_backend)
    execution_description += ' with message "'
    execution_description += message + '" and density "' + str(density) + '"'
    halo_text = 'Running E91 simulation in ' + execution_description
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      start_time = time.time()
      self.e91_algorithm.run(message, backend, bits_size, density, N_BITS, True)
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  E91 simulation runned in', str(time_ms), 'ms')
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)

  ## Run an experiment of E91 simulation
  def __experimental_mode(self, len_msg_limit=5, density_step=0.05, repetition_instance=10):
    STEP_MSG = 10
    DENSITY_MIN = 0
    DENSITY_MAX = 1
    DENSITY_RANGE = int((DENSITY_MAX - DENSITY_MIN) / density_step)
    backend = self.qexecute.current_backend
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    image_security = np.zeros((DENSITY_RANGE + 1, len_msg_limit // STEP_MSG))
    image_corr = np.zeros((DENSITY_RANGE + 1, len_msg_limit // STEP_MSG))
    image_check = np.zeros((DENSITY_RANGE + 1, len_msg_limit // STEP_MSG))
    x = list(range(STEP_MSG, len_msg_limit + 1, STEP_MSG))
    y = list(np.arange(0, 1 + density_step, density_step))
    checker = Sender()
    start_time = time.time()
    print('\nRunning E91 Simulator Experiment (in ' + str(backend) + '):')

    try:
      with alive_bar(len(x) * len(y) * repetition_instance) as bar:
        for j, density in enumerate(y):
          for i, len_message in enumerate(x):
            for _ in range(repetition_instance):
              message = ''.join(SystemRandom().choice(possible_chars) for _ in range(len_message))
              bits_size = ceil(len(message) * 9 / 2) # 9 / 2 because is the theorical value
              flag, corr = self.e91_algorithm.run(message, backend, bits_size, density, 1, False)
              image_security[j][i] += 1 if flag else 0
              image_corr[j][i] += corr
              bar()
            image_corr[j][i] /= repetition_instance
            if checker.check_corr(image_corr[j][i]):
              image_check[j][i] = 0
            else:
              image_check[j][i] = 1
          
    except Exception as exception:
      print('Exception:', exception)

    time_m = (time.time() - start_time)
    print('\n[$] Experiment Finished in ' + str(time_m) + ' s!')
    print('\n💡 Output:\n\nx: ' + str(x) + '\n\ny: ' + str(y))
    print('\nImage Security:\n' + str(image_security) + '\n')
    print('\nImage Average Correlation:\n' + str(image_corr) + '\n')
    print('\nImage Average correlation check:\n' + str(image_check) + '\n')

    results = {
      'x': x,
      'y': y,
      'backend': backend,
      'image_security': image_security,
      'image_corr': image_corr,
      'image_check': image_check
    }

    while True:
      try:
        self.__show_options_experimental_mode()
        if self.__select_option_experimental_mode(results) == 0:
          return
      except Exception as _:
        pass

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

  ## Select the option for main menu
  def __select_option_experimental_mode(self, results):
    option = int(input('[&] Select an option: '))
    if option == 0:
      pass
    elif option == 1:
      plt.figure(num='E91 Simulator - Experimental Mode (Security) [' + str(results['backend']) + ']')
      plt.pcolormesh(results['x'], results['y'], results['image_security'], cmap='inferno', shading='auto')
      plt.colorbar(label='Times the protocol is determined safe')
      plt.xlabel('Message Length (number of bits)')
      plt.ylabel('Interception Density')
      plt.show()
    elif option == 2:
      plt.figure(num='E91 Simulator - Experimental Mode (Average Correlation) [' + str(results['backend']) + ']')
      plt.pcolormesh(results['x'], results['y'], results['image_corr'], cmap='inferno', shading='auto')
      plt.colorbar(label='Average Correlation')
      plt.xlabel('Message Length (number of bits)')
      plt.ylabel('Interception Density')
      plt.show()
    elif option == 3:
      plt.figure(num='E91 Simulator - Experimental Mode (Average correlation check) [' + str(results['backend']) + ']')
      plt.pcolormesh(results['x'], results['y'], results['image_check'], cmap='bwr', shading='auto')
      plt.colorbar(label='Average correlation check')
      plt.xlabel('Message Length (number of bits)')
      plt.ylabel('Interception Density')
      plt.show()
    else:
      print('[!] Invalid option, try again')
    return option
