#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from quantum_solver.quantum_solver import QuantumSolver
from rsa_substitute.rsa_substitute_algorithm import RsaSubstituteAlgorithm
import time
import matplotlib.pyplot as plt
import numpy as np
from halo import Halo
from numpy.random import randint
from random import SystemRandom, randrange
import string
from alive_progress import alive_bar
from math import ceil

RSA_SUBSTITUTE_SIMULATOR = 'RSA Substitute SIMULATOR'

## Main class of RSA Substitute Simulator
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class RsaSubstitute:
  ## Constructor
  def __init__(self, token):
    ## The implemented protocol
    self.rsaSubstitute_algorithm = RsaSubstituteAlgorithm()
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
      except Exception as exception:
        print('\nException: ' + str(exception))

  ## Main menu
  def __show_options(self):
    is_guest_mode = self.qexecute.is_guest_mode()
    guest_mode_string = ' (Guest Mode)' if is_guest_mode else ''
    len_guest_mode_string = len(guest_mode_string)
    print('\n' + RSA_SUBSTITUTE_SIMULATOR + guest_mode_string)
    print('=' * (len(RSA_SUBSTITUTE_SIMULATOR) + len_guest_mode_string) + '\n')
    print('[1] See available Backends')
    print('[2] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
      print('[3] Run Algorithm')
      print('[4] Experimental mode')
    print('[0] Exit\n')

  ## Run RSA Substitute simulation once
  def __run_simulation(self):
    backend = self.qexecute.current_backend
    measure_zero_prob = float(input('[&] Probability of measure zero: '))
    n_shots = int(input('[&] Number of shots: '))
    if measure_zero_prob < 0 or measure_zero_prob > 1:
      raise ValueError('Probability of measure zero must be between 0 and 1 (0 <= measure_zero_prob <= 1)')
    elif n_shots <= 0:
      raise ValueError('Number of shots must be positive (> 0)')

    execution_description = str(backend)
    execution_description += ' with probability of measure zero '
    execution_description += str(measure_zero_prob)
    execution_description += ' and ' + str(n_shots) + ' shots'
    halo_text = 'Running RSA Substitute simulation in ' + execution_description
    halo = Halo(text=halo_text, spinner="dots")

    try:
      halo.start()
      start_time = time.time()
      self.rsaSubstitute_algorithm.run(measure_zero_prob, n_shots, backend, True)
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  RSA Substitute simulation runned in', str(time_ms), 'ms')
    except Exception as _:
      halo.fail()

  ## Run an experiment of RSA Substitute simulation
  def __experimental_mode(self, prob_values, shots_values):
    backend = self.qexecute.current_backend
    image = np.zeros((len(prob_values), len(shots_values)))
    start_time = time.time()

    print('\nRunning RSA Substitute Simulator Experiment (in ' + str(backend) + '):')
    try:
      with alive_bar(len(prob_values) * len(shots_values)) as bar:
        for i, measure_zero_prob in enumerate(prob_values):
          for j, n_shots in enumerate(shots_values):
            _, relative_error = self.rsaSubstitute_algorithm.run(measure_zero_prob, n_shots, backend, False)
            image[i][j] += relative_error
            bar()
          
    except Exception as exception:
      print('Exception:', exception)

    time_s = (time.time() - start_time)
    print('\n[$] Experiment Finished in ' + str(time_s) + ' s!')
    print('\n💡 Output:\n\nx: ' + str(prob_values) + '\n\ny: ' + str(shots_values))
    print('\nImage:\n' + str(image) + '\n')
    plt.figure(num='RSA Substitute Simulator - Experimental Mode [' + str(backend) + ']')
    plt.pcolormesh(shots_values, prob_values, image, cmap='inferno', shading='auto')
    plt.colorbar(label='Relative Error')
    plt.xlabel('n_shots')
    plt.ylabel('Probability of measure zero')
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
      prob_values = [float(x) for x in input('[&] Specify probability of measure zero values separated by spaces: ').split(' ')]
      shots_values = [int(x) for x in input('[&] Specify shots values separated by spaces: ').split(' ')]

      if len(prob_values) <= 0 or len(shots_values) <= 0:
        raise ValueError('Empty values generated, try again')
      else:
        self.__experimental_mode(prob_values, shots_values)
    else:
      print('[!] Invalid option, try again')
