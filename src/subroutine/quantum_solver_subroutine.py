#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from execution.qexecute import QExecute
from subroutine.subroutine_manager import SubroutineManager
from quantum_solver.quantum_solver import QuantumSolver
from halo import Halo
from pwinput import pwinput
import time
import matplotlib.pyplot as plt
from ascii_graph import Pyasciigraph

QUANTUM_SOLVER_SUBROUTINE = 'QuantumSolver Subroutine'

## Main Class of QuantumSolver
class QuantumSolverSubroutine(QuantumSolver):
  ## Constructor
  def __init__(self, token=None):
    super().__init__(token)
    ## An QSubroutine Manager instance
    self.subroutine_manager = SubroutineManager()

  ## Run main function
  def run(self):
    self.__show_header()
    ## A QExecute instance to execute the simulation
    self.qexecute = self.get_qexecute()
    self.__main_menu()

  ## Print header
  def __show_header(self):
    print('\n' + QUANTUM_SOLVER_SUBROUTINE + '\n' + '=' * len(QUANTUM_SOLVER_SUBROUTINE) + '\n')
    print('A little quantum toolset developed using Qiskit')
    print('WARNING: The toolset uses your personal IBM Quantum Experience')
    print('token to access to the IBM hardware.')
    print('You can access to your API token or generate another one here:')
    print('https://quantum-computing.ibm.com/account\n')
    print('You can also use the Guest Mode which only allows you to run ')
    print('quantum circuits in a local simulator ("aer_simulator").\n')
  
  ## Print options
  def __show_options(self):
    is_guest_mode = self.qexecute.is_guest_mode()
    guest_mode_string = ' (Guest Mode)' if is_guest_mode else ''
    len_guest_mode_string = len(guest_mode_string)
    print('\n' + QUANTUM_SOLVER_SUBROUTINE + guest_mode_string)
    print('=' * (len(QUANTUM_SOLVER_SUBROUTINE) + len_guest_mode_string) + '\n')
    print('[1] See available Backends')
    print('[2] See available Subroutines')
    print('[3] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
    print('[4] Select Subroutine')
    if self.is_selected_algorithm:
      print('\tCurrent Subroutine: ' + \
          self.subroutine_manager.current_algorithm.name)
    if self.is_selected_algorithm:
      print('[5] Select Parameters')
      if self.is_parameter:
        print('\tCurrent Parameters: ' + str(self.subroutine_manager.parameters))
    if self.is_selected_backend and self.is_selected_algorithm and self.is_parameter:
      print('[6] Run Subroutine')
    print('[0] Exit\n')

  ## Main menu
  def __select_option(self):
    option = int(input('[&] Select an option: '))
    if option == 0:
      print()
      exit(0)
    elif option == 1:
      self.qexecute.print_avaiable_backends()
    elif option == 2:
      self.subroutine_manager.print_available_algorithms()
    elif option == 3:
      self.qexecute.select_backend()
    elif option == 4:
      self.subroutine_manager.select_algorithm()
    elif option == 5 and self.is_selected_algorithm:
      self.subroutine_manager.select_parameters()
    elif option == 6 and self.is_selected_backend and \
        self.is_selected_algorithm and self.is_parameter:
      n_shots = int(input('[&] Specify the number of shots: '))
      self.run_subroutine(n_shots)
    else:
      print('[!] Invalid option, try again')
    
  ## Run n_shots times the current algorithm with the current parameters in the current backend
  def run_subroutine(self, n_shots):
    current_algorithm = self.subroutine_manager.current_algorithm
    new_parameters = current_algorithm.preprocessing(self.subroutine_manager.parameters)
    self.subroutine_manager.parameters = new_parameters

    start_time = time.time()
    print('\nRunning Subroutine:')

    execution_description = current_algorithm.name
    execution_description += ' in ' + str(self.qexecute.current_backend)
    execution_description += ' with parameters: '
    execution_description += str(self.subroutine_manager.parameters)
    halo_text = 'Executing ' + execution_description
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()

      circuit = self.subroutine_manager.get_circuit()
      counts = self.qexecute.run(circuit, n_shots)
      
      halo.succeed()
      time_s = (time.time() - start_time)
      print('\n[$] Experiment Finished in ' + str(time_s) + ' s!')
      print('\nRaw Output:', counts, '\n')
      data = [(key, counts[key]) for key in counts.keys()]
      graph = Pyasciigraph(line_length=80)
      for line in graph.graph('QuantumSolver Subroutine', data):
        print(line)
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)
      raise exception
  
    final_result = current_algorithm.postprocessing(counts, new_parameters)
    print('\n💡 Final result:', final_result)
    
    return counts, final_result

  ## Loop for the main menu
  def __main_menu(self):
    while True:
      try:
        ## If a current backend has been selected
        self.is_selected_backend = self.qexecute.current_backend != None
        ## If a current algorithm has been selected
        self.is_selected_algorithm = self.subroutine_manager.current_algorithm != None
        ## If a current parameters have been selected
        self.is_parameter = self.subroutine_manager.parameters != None

        self.__show_options()
        self.__select_option()
      except Exception as _:
        pass
