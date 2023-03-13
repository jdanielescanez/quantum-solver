#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from quantum_solver.quantum_solver import QuantumSolver
from crypto.elgamal.elgamal_algorithm import ElGamalAlgorithm
import time
import matplotlib.pyplot as plt
import numpy as np
from halo import Halo
from numpy.random import randint
from random import SystemRandom
import string
from alive_progress import alive_bar

ELGAMAL_SIMULATOR = 'ElGamal SIMULATOR'

## Main class of ElGamal Simulator
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class ElGamal:
  ## Constructor
  def __init__(self, token):
    ## The implemented protocol
    self.elgamal_algorithm = ElGamalAlgorithm()
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
      except Exception as _:
        pass

  ## Main menu
  def __show_options(self):
    is_guest_mode = self.qexecute.is_guest_mode()
    guest_mode_string = ' (Guest Mode)' if is_guest_mode else ''
    len_guest_mode_string = len(guest_mode_string)
    print('\n' + ELGAMAL_SIMULATOR + guest_mode_string)
    print('=' * (len(ELGAMAL_SIMULATOR) + len_guest_mode_string) + '\n')
    print('[1] See available Backends')
    print('[2] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
      print('[3] Run Algorithm')
    print('[0] Exit\n')

  ## Run ElGamal simulation once
  def __run_simulation(self):
    message = str(input('[&] Message (2 complex numbers separated by comma: a+bj, c+dj): '))
    backend = self.qexecute.current_backend
    execution_description = str(self.qexecute.current_backend)
    execution_description += ' with message "' + message + '"'
    halo_text = 'Running ElGamal simulation in ' + execution_description
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      start_time = time.time()
      results = self.elgamal_algorithm.run(message)
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  ElGamal simulation runned in', str(time_ms), 'ms')
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)
    
    self.print_results(results)

  def print_results(self, results):
    np.set_printoptions(formatter={'complex_kind': '{:.3f}'.format})
    message_sv, encrypted_message, decrypted_message, encrypted_message_sv, decrypted_message_sv, alice, bob = results

    print('\n\nInitial Message (Statevector):')
    print(message_sv.data)

    alice.show_dagger_public_key()
    bob.show_public_key()

    print('\nEncrypted Message (Circuit):')
    print(encrypted_message)

    print('\nEncrypted Message (Statevector):')
    print(encrypted_message_sv.data)

    print('\nDecrypted Message (Circuit):')
    print(decrypted_message)

    print('\n💡 Decrypted Message (Statevector):')
    print(decrypted_message_sv.data)

    if message_sv == decrypted_message_sv:
      print('\n✅ The initial message and the decrypted message are identical')
    else:
      print('\n❌ The initial message and the decrypted message are different')

  ## Run an experiment of ElGamal simulation
  def __experimental_mode(self, len_msg_limit=5, density_step=0.05, repetition_instance=10):
    DENSITY_MIN = 0
    DENSITY_MAX = 1
    DENSITY_RANGE = int((DENSITY_MAX - DENSITY_MIN) / density_step)
    backend = self.qexecute.current_backend
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    image = np.zeros((DENSITY_RANGE + 1, len_msg_limit))
    x = list(range(1, len_msg_limit + 1, 1))
    y = list(np.arange(0, 1 + density_step, density_step))
    start_time = time.time()
    print('\nRunning ElGamal Simulator Experiment (in ' + str(backend) + '):')

    try:
      with alive_bar(len(x) * len(y) * repetition_instance) as bar:
        for j, density in enumerate(y):
          for i, len_message in enumerate(x):
            for _ in range(repetition_instance):
              message = ''.join(SystemRandom().choice(possible_chars) for _ in range(len_message))
              bits_size = len(message) * 5
              flag = self.elgamal_algorithm.run(message, backend, bits_size, density, 1, False)
              image[j][i] += 1 if flag else 0
              bar()
          
    except Exception as exception:
      print('Exception:', exception)

    time_m = (time.time() - start_time)
    print('\n[$] Experiment Finished in ' + str(time_m) + ' s!')
    print('\n💡 Output:\n\nx: ' + str(x) + '\n\ny: ' + str(y))
    print('\nImage:\n' + str(image) + '\n')
    plt.figure(num='ElGamal Simulator - Experimental Mode [' + str(backend) + ']')
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
    else:
      print('[!] Invalid option, try again')
