
from crypto.bb84.bb84 import BB84
from crypto.e91.e91 import E91
from crypto.b92.b92 import B92
from crypto.six_state.six_state import SixState
from crypto.rsa_substitute.rsa_substitute import RsaSubstitute
from crypto.elgamal.elgamal import ElGamal

QUANTUM_SOLVER_CRYPTO = 'QuantumSolver Crypto'

class CryptoManager:
  def __init__(self, token):
    ## The IBMQ Experience token
    self.token = token
    self.protocols = [
      BB84(token),
      E91(token),
      B92(token),
      SixState(token),
      RsaSubstitute(token),
      ElGamal(token)
    ]

  ## Print header and run main menu
  def run(self):
    self.__show_header()
    self.__main_menu()

  ## Print header
  def __show_header(self):
    print('\n' + QUANTUM_SOLVER_CRYPTO + '\n' + '=' * len(QUANTUM_SOLVER_CRYPTO) + '\n')
    print('A simulator of quantum cryptographic protocols using Qiskit')
    print('WARNING: The simulator uses your personal IBM Quantum Experience')
    print('token to access to IBM hardware.')
    print('You can access to your API token or generate another one here:')
    print('https://quantum-computing.ibm.com/account\n')
    print('You can also use the Guest Mode which only allows you to run ')
    print('quantum circuits in a local simulator ("aer_simulator").\n')

  ## Loop to run the main menu
  def __main_menu(self):
    while True:
      try:
        self.__show_options()
        self.__select_option()
      except Exception as e:
        raise e # TODO
        pass

  ## Main menu
  def __show_options(self):
    print('\n' + QUANTUM_SOLVER_CRYPTO)
    print('=' * len(QUANTUM_SOLVER_CRYPTO) + '\n')
    print('[1] BB84')
    print('[2] E91')
    print('[3] B92')
    print('[4] Six-State')
    print('[5] RSA Substitute')
    print('[6] Quantum ElGamal')
    print('[0] Exit\n')

  ## Select the option for main menu
  def __select_option(self):
    option = int(input('[&] Select an option: '))
    if option == 0:
      print()
      exit(0)
    elif option <= len(self.protocols):
      self.protocols[option - 1].run()
    else:
      print('[!] Invalid option, try again')
