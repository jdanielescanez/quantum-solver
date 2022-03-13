
from execution.qexecute import QExecute
from algorithms.qrand import QRand
from algorithms.qalgorithm_manager import QAlgorithmManager
from halo import Halo
from pwinput import pwinput
import time
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

QUANTUM_SOLVER = 'Quantum Solver'

class QuantumSolver:
  def __init__(self, token=None):
    self.qalgorithm_manager = QAlgorithmManager()
    self.token = token

  def run(self):
    self.__show_header()
    self.qexecute = self.get_qexecute()
    self.__main_menu()

  def get_qexecute(self):
    tries = 0
    MAX_TRIES = 3
    while tries < MAX_TRIES:
      tries += 1
      if self.token == None:
        self.token = pwinput(mask='*', \
            prompt='[&] Write your IBM Quantum Experience token: ')
      halo = Halo(text="Authenticating to the IBMQ server", spinner="dots")
      try:
        halo.start()
        qexecute = QExecute(self.token)
        halo.succeed()
        break
      except:
        halo.fail()
        self.token = None
        if tries < 3:
          print('[!] Invalid IBM Quantum Experience token, try again (' + \
                str(tries) + ' / ' + str(MAX_TRIES) + ')\n')
        else:
          link = 'https://quantum-computing.ibm.com/composer/docs/iqx/manage/account/'
          print('\n[#] You have reached the maximum number of attempts (' + \
                str(tries) + ' / ' + str(MAX_TRIES) + ')\nIt ' + \
                'is advisable to try again after consulting this reference:' + \
                '\n' + link, '\n')
          exit(-1)
    return qexecute

  def __show_header(self):
    print('\n' + QUANTUM_SOLVER + '\n' + '=' * len(QUANTUM_SOLVER) + '\n')
    print('A little quantum toolset developed using Qiskit')
    print('WARNING: The toolset uses your personal IBM Quantum Experience')
    print('token to access to IBM hardware.')
    print('You can access to your API token or generate another one here:')
    print('https://quantum-computing.ibm.com/account\n')
  
  def __show_options(self):
    print('\n' + QUANTUM_SOLVER + '\n' + '=' * len(QUANTUM_SOLVER) + '\n')
    print('[1] See available Backends')
    print('[2] See available Algorithms')
    print('[3] Select Backend')
    if self.is_selected_backend:
      print('\tCurrent Backend: ' + str(self.qexecute.current_backend))
    print('[4] Select Algorithm')
    if self.is_selected_algorithm:
      print('\tCurrent Algorithm: ' + \
          self.qalgorithm_manager.current_algorithm.name)
    if self.is_selected_algorithm:
      print('[5] Select Parameters')
      if self.is_parameter:
        print('\tCurrent Parameters: ' + str(self.qalgorithm_manager.parameters))
    if self.is_selected_backend and self.is_selected_algorithm and self.is_parameter:
      print('[6] Run Algorithm')
      print('[7] Experimental mode')
    print('[0] Exit\n')

  def __select_option(self):
    option = int(input('[&] Select an option: '))
    if option == 0:
      print()
      exit(0)
    elif option == 1:
      self.qexecute.print_avaiable_backends()
    elif option == 2:
      self.qalgorithm_manager.print_avaiable_algorithms()
    elif option == 3:
      self.qexecute.select_backend()
    elif option == 4:
      self.qalgorithm_manager.select_algorithm()
    elif option == 5 and self.is_selected_backend and self.is_selected_algorithm:
      self.qalgorithm_manager.select_parameters()
    elif option == 6 and self.is_selected_backend and \
        self.is_selected_algorithm and self.is_parameter:
      self.__run_algorithm()
    elif option == 7 and self.is_selected_backend and \
        self.is_selected_algorithm and self.is_parameter:
      self.__experimental_mode()
    else:
      print('[!] Invalid option, try again')
    
  def __run_algorithm(self):
    print()
    halo_text = 'Creating circuit'
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      start_time = time.time()
      circuit = self.qalgorithm_manager.get_circuit()
      time_ms = (time.time() - start_time) * 1000
      halo.succeed()
      print('  Circuit created in', str(time_ms), 'ms')
    except Exception as exception:
      halo.fail()
      print('Exception: ', exception)

    N_SHOTS = 1
    halo_text = 'Executing '
    halo_text += self.qalgorithm_manager.current_algorithm.name
    halo_text += ' in ' + str(self.qexecute.current_backend)
    halo_text += ' with parameters: '
    halo_text += str(self.qalgorithm_manager.parameters)
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      exec_start_time = time.time()
      result = self.qexecute.run(circuit, N_SHOTS)
      exec_ms = (time.time() - exec_start_time) * 1000
      halo.succeed()
      print('  Execution done in', str(exec_ms), 'ms')
      parsed_result = self.qalgorithm_manager.parse_result(result)
      print('\n💡 Output:', parsed_result, '\n')
    except Exception as exception:
      halo.fail()
      print('Exception: ', exception)

  def __experimental_mode(self):
    n_shots = int(input('[&] Specify number of shots: '))

    start_time = time.time()
    print('\nRunning Experiment:')

    halo_text = 'Executing '
    halo_text += self.qalgorithm_manager.current_algorithm.name
    halo_text += ' ' + str(n_shots) + ' times'
    halo_text += ' in ' + str(self.qexecute.current_backend)
    halo_text += ' with parameters: '
    halo_text += str(self.qalgorithm_manager.parameters)
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()
      circuit = self.qalgorithm_manager.get_circuit()
      result = self.qexecute.run(circuit, n_shots)
      
      halo.succeed()
      time_m = (time.time() - start_time)
      print('\n[$] Experiment Finished in ' + str(time_m) + ' s!')
      print('\n💡 Output:', result, '\n')
      plot_histogram(result, title='QuantumSolver - Experimental Mode')
      plt.show()
    except Exception as exception:
      halo.fail()
      print('Exception: ', exception)

  def __main_menu(self):
    while True:
      self.is_selected_backend = self.qexecute.current_backend != None
      self.is_selected_algorithm = self.qalgorithm_manager.current_algorithm != None
      self.is_parameter = self.qalgorithm_manager.parameters != None

      self.__show_options()
      self.__select_option()
      
