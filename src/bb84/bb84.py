
from quantum_solver.quantum_solver import get_qexecute

BB84_SIMULATOR = 'BB84 SIMULATOR'

class BB84:
  def __init__(self, argv):
    self.token = None
    if len(argv) > 1:
      self.token = argv[1]

  def run(self):
    self.__show_header()
    self.qexecute = get_qexecute()
    self.__main_menu()

  def __show_header(self):
    print('\n' + BB84_SIMULATOR + '\n' + '=' * len(BB84_SIMULATOR) + '\n')
    print('A BB84 simulator using Qiskit')
    print('WARNING: The BB84 simulator uses your personal IBM Quantum Experience')
    print('token to access to IBM hardware.')
    print('You can access to your API token or generate another one here:')
    print('https://quantum-computing.ibm.com/account\n')
