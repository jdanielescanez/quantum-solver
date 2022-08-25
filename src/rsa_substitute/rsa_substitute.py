#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

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
## @see https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/awards/teach_me_qiskit_2018/rsaSubstitute_qkd/rsaSubstitute_quantum_key_distribution_protocol.ipynb
class RsaSubstitute:
  ## Constructor
  def __init__(self, token):
    ## The implemented protocol
    self.rsaSubstitute_algorithm = RsaSubstituteAlgorithm()
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
    print('\n' + RSA_SUBSTITUTE_SIMULATOR + '\n' + '=' * len(RSA_SUBSTITUTE_SIMULATOR) + '\n')
    print('A RSA Substitute simulator using Qiskit')
    print('WARNING: The RSA Substitute simulator uses your personal IBM Quantum Experience')
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
    if self.is_selected_backend:
      print('[3] Run Algorithm')
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
    else:
      print('[!] Invalid option, try again')
