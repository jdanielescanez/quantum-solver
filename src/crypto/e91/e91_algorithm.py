#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from qiskit import execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from crypto.e91.sender import Sender
from crypto.e91.receiver import Receiver
from crypto.e91.eavesdropper import Eveasdropper
import binascii

E91_SIMULATOR = 'E91 SIMULATOR'

## An implementation of the E91 protocol
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class E91Algorithm:
  ## Get the simplest (and maximal) example of quantum entanglement * (- 1j)
  def get_bell_pair(self, qr, cr):
    circuit = QuantumCircuit(qr, cr)
    circuit.x([0, 1])
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.s([0, 1])
    return circuit

  ## Generate a key for Alice and Bob
  def generate_key(self, backend, original_bits_size, verbose):
    # Initialize the bell pair, quantum and classical registers
    qr = QuantumRegister(2, name="qr")
    cr = ClassicalRegister(4, name="cr")
    singlet = self.get_bell_pair(qr, cr)

    # Initialize entities Alice, Eve and Bob
    alice = Sender('Alice', original_bits_size, qr, cr)
    alice.set_axes()

    eve = Eveasdropper('Eve', original_bits_size, qr, cr)
    eve.set_axes(density=self.measure_density)
    
    bob = Receiver('Bob', original_bits_size, qr, cr)
    bob.set_axes()

    # Create circuits and get results
    circuits = []
    for i in range(original_bits_size):
      if eve.axes[i] != None:
        eve_measure = eve.measurements[eve.axes[i][0]] + eve.measurements[eve.axes[i][1]]
      else:
        eve_measure = QuantumCircuit(qr, cr)
      alice_measure = alice.measurements[alice.axes[i]]
      bob_measure = bob.measurements[bob.axes[i]]
      circuit = singlet + eve_measure + alice_measure + bob_measure
      eve_measure_name = '_' + eve.axes[i][0] + '-' + eve.axes[i][1] if eve.axes[i] != None else ''
      circuit.name = str(i) + ':' + alice.axes[i] + '_' + bob.axes[i] + eve_measure_name
      circuits.append(circuit)

    result = execute(circuits, backend=backend, shots=1).result()
    
    alice.create_values(result, circuits)
    bob.create_values(result, circuits)
    eve.create_values(result, circuits)

    # Publish the measurements
    # Obtain values from the circuit measurements
    count = [[0, 0, 0, 0], # XW observable
             [0, 0, 0, 0], # XV observable
             [0, 0, 0, 0], # ZW observable
             [0, 0, 0, 0]] # ZV observable

    alice.key = []; eve.key = []; bob.key = []
    for i in range(original_bits_size):
      # If Alice and Bob have measured the spin projections onto the a_2/b_1 or a_3/b_2 directions
      if (alice.axes[i] == 'a2' and bob.axes[i] == 'b1') or \
         (alice.axes[i] == 'a3' and bob.axes[i] == 'b2'):
        alice.key.append(alice.values[i])
        bob.key.append(0 if bob.values[i] == 1 else 1)
        if eve.values[i] != [None, None]:
          eve.key.append([eve.values[i][0], 0 if eve.values[i][1] == 1 else 1])
        else:
          eve.key.append([None, None])
      else:
        eve.key.append([None, None])
        if (alice.axes[i] == 'a1' or alice.axes[i] == 'a3') and (bob.axes[i] == 'b1' or bob.axes[i] == 'b3'):
          res = list(result.get_counts(circuits[i]).keys())[0]
          j = 2 * int(alice.axes[i] == 'a3') + int(bob.axes[i] == 'b3')
          k = int(res[-2:], base=2)
          count[j][k] += 1

    corr = self.compute_corr(count)
    keyLength = len(alice.key)
    info = self.get_mismatches_info(alice, eve, bob)

    if verbose:
      alice.show_values()
      alice.show_measurements()
      alice.show_axes()

      eve.show_values()
      eve.show_measurements()
      eve.show_axes()

      bob.show_values()
      bob.show_measurements()
      bob.show_axes()

      alice.show_key()
      bob.show_key()

      print('\nNumber of mismatching bits: ' + str(info['alice_bob_key_mismatches']))

      print('\nEve\'s knowledge of Alice\'s key: ' + str(round(info['eve_alice_knowledge'] * 100, 2)) + '%')
      print('Eve\'s knowledge of Bob\'s key: ' + str(round(info['eve_bob_knowledge'] * 100, 2)) + '%')

      # CHSH inequality test
      print('CHSH correlation:', corr)
      # Key length test
      print('Key length:', len(alice.key))

      print('\nCHSH correlation should be close to -2 * √2 ~= -2.8282')
      print('Key length should be close to', original_bits_size, '* 2 / 9 =', original_bits_size * 2 / 9)

    if alice.check_corr(corr):
      alice.confirm_key()
      bob.confirm_key()
    
      if verbose:
        print('\nCHSH correlation is in −2√2 · (1 ± 0.1)')
        print('\nFinal Keys')
        alice.show_key()
        bob.show_key()
        print('\nSecure Communication!')
    elif verbose: 
      print('\nCHSH correlation is not in −2√2 · (1 ± 0.1)')
      print('Unsecure Communication! Eve has been detected intercepting messages\n')
    
    return alice, bob, corr

  def get_mismatches_info(self, alice, eve, bob):
    keyLength = len(alice.key)
    info = {
      'alice_bob_key_mismatches': 0,
      'eve_alice_key_mismatches': 0,
      'eve_bob_key_mismatches': 0,
      'eve_alice_knowledge': 0,
      'eve_bob_knowledge': 0
    }

    for j in range(keyLength):
      if alice.key[j] != bob.key[j]: 
        info['alice_bob_key_mismatches'] += 1
      if j < len(eve.key):
        if eve.key[j][0] != alice.key[j]:
          info['eve_alice_key_mismatches'] += 1
        if eve.key[j][1] != bob.key[j]:
          info['eve_bob_key_mismatches'] += 1

    if keyLength > 0 and len(eve.key) > 0:
      # Eve's knowledge of Bob's key
      info['eve_alice_knowledge'] = (keyLength - info['eve_alice_key_mismatches']) / keyLength
      # Eve's knowledge of Alice's key
      info['eve_bob_knowledge'] = (keyLength - info['eve_bob_key_mismatches']) / keyLength

    return info

  ## Calculate correlation
  def compute_corr(self, count):
    # Number of the results obtained from the measurements in a particular basis
    total = [sum(count[0]), sum(count[1]), sum(count[2]), sum(count[3])]
    check_total = list(map(lambda x: x == 0, total))

    if any(check_total):
      return float('-inf')

    # Expectation values of XW, XV, ZW and ZV observables
    expect11 = (count[0][0] - count[0][1] - count[0][2] + count[0][3]) / total[0] # -1 / sqrt(2)
    expect13 = (count[1][0] - count[1][1] - count[1][2] + count[1][3]) / total[1] #  1 / sqrt(2)
    expect31 = (count[2][0] - count[2][1] - count[2][2] + count[2][3]) / total[2] # -1 / sqrt(2)
    expect33 = (count[3][0] - count[3][1] - count[3][2] + count[3][3]) / total[3] # -1 / sqrt(2) 
    
    return expect11 - expect13 + expect31 + expect33 # Calculate the CHSC correlation value

  ## Run the implementation of E91 protocol
  def run(self, message, backend, original_bits_size, measure_density, n_bits, verbose):
    ## The original size of the message
    self.original_bits_size = original_bits_size
    ## The probability of an interception occurring
    self.measure_density = measure_density

    alice, bob, corr = self.generate_key(backend, original_bits_size, verbose)
    if not (alice.is_safe_key and bob.is_safe_key):
      if verbose:
        print('❌ Message not send')
      return False, corr

    alice.generate_otp(n_bits)
    bob.generate_otp(n_bits)

    encoded_message = alice.xor_otp_message(message)
    decoded_message = bob.xor_otp_message(encoded_message)

    if verbose:
      alice.show_otp()
      bob.show_otp()

      print('\nInitial Message:')
      print(message)

      print('Encoded Message:')
      print(encoded_message)

      print('💡 Decoded Message:')
      print(decoded_message)

      if message == decoded_message:
        print('\n✅ The initial message and the decoded message are identical')
      else:
        print('\n❌ The initial message and the decoded message are different')

    return True, corr
