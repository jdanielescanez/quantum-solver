
from execution.qexecute import QExecute
from algorithms.qrand import QRand
from algorithms.qalgorithm_manager import QAlgorithmManager
from halo import Halo
from pwinput import pwinput
import time

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
      message = Halo(text="Authenticating to the IBMQ server", spinner="dots")
      try:
        message.start()
        qexecute = QExecute(self.token)
        message.succeed()
        break
      except:
        message.fail()
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
    else:
      print('[!] Invalid option, try again')
    
  def __run_algorithm(self):
    print()
    message_text = 'Creating circuit'
    message = Halo(text=message_text, spinner="dots")
    try:
      message.start()
      start_time = time.time()
      circuit = self.qalgorithm_manager.get_circuit()
      time_ms = (time.time() - start_time) * 1000
      message.succeed()
      print('  Circuit created in', str(time_ms), 'ms')
    except Exception as exception:
      message.fail()
      print('Exception: ', exception)

    n_shots = self.qalgorithm_manager.current_algorithm.n_shots
    message_text = 'Executing '
    message_text += self.qalgorithm_manager.current_algorithm.name
    message_text += ' in ' + str(self.qexecute.current_backend)
    message_text += ' with parameters: '
    message_text += str(self.qalgorithm_manager.parameters)
    message = Halo(text=message_text, spinner="dots")
    try:
      message.start()
      exec_start_time = time.time()
      result = self.qexecute.run(circuit, n_shots)
      exec_ms = (time.time() - exec_start_time) * 1000
      message.succeed()
      print('  Execution done in', str(exec_ms), 'ms')
      parsed_result = self.qalgorithm_manager.parse_result(result)
      print('\nOutput:', parsed_result, '\n')
    except Exception as exception:
      message.fail()
      print('Exception: ', exception)

  def __main_menu(self):
    while True:
      self.is_selected_backend = self.qexecute.current_backend != None
      self.is_selected_algorithm = self.qalgorithm_manager.current_algorithm != None
      self.is_parameter = self.qalgorithm_manager.parameters != None

      self.__show_options()
      self.__select_option()
      
