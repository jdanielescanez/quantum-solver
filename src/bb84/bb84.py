
from quantum_solver.quantum_solver import QuantumSolver
from bb84.bb84_algorithm import BB84Algorithm

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
    print('[0] Exit\n')

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
      message = str(input('[&] Message (string): '))
      density = float(input('[&] Interception Density (float between 0 and 1): '))
      backend = self.qexecute.current_backend
      bits_size = len(message) * 2 ** 7
      self.bb84_algorithm.run(message, backend, bits_size, density)
    else:
      print('[!] Invalid option, try again')
