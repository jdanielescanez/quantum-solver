#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import QuantumCircuit
from algorithms.qalgorithm import QAlgorithm
import numpy as np

## Deutsch-Jozsa Algorithm Implementation for QuantumSolver
## @see https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html
class DeutschJozsa(QAlgorithm):
  ## Constructor
  def __init__(self):
    self.name = 'Deutsch-Jozsa'
    self.description = \
        'Given a hidden Boolean function f: f({x_0,x_1,x_2,...}) → 0 or 1, where x_n is 0 or 1;\n\
            determine whether the given function is balanced or constant. A constant function returns \
                all 0\'s or all 1\'s for any input, while a balanced function returns 0\'s for exactly \
                    half of all inputs and 1\'s for the other half.'
    self.parameters = [
      {
        'type': 'string',
        'description': 'The oracle type: "constant" or "balanced"',
        'constraint': 'Can\'t be bigger than the number of qubits of the selected backend'
      },
      {
        'type': 'int',
        'description': 'A positive number of qubits to use',
        'constraint': 'Can\'t be bigger than the number of qubits of the selected backend'
      }
    ]
    self.parse_result = lambda counts: 'Constant' if list(counts.keys())[0][0] == 0 else 'Balanced'
    self.parse_parameters = lambda parameters: [str(parameters[0]), int(parameters[1])]

  ## Verify that the parameters are the oracle type and the number of qubits to use
  def check_parameters(self, parameters):
    if len(parameters) == 2 and all(map(lambda param: type(param) == str, parameters)):
      try:
        is_valid_oracle_type = parameters[0] == 'constant' or parameters[0] == 'balanced'
        return is_valid_oracle_type and int(parameters[1]) > 0
      except:
        return False

  ## Create the oracle circuit
  def create_oracle(self, oracle_type, n):
    oracle_qc = QuantumCircuit(n + 1)
    
    if oracle_type == 'balanced':
      # Generate a random number that indicates which CNOTs to wrap in X-gates
      b = np.random.randint(1, 2 ** n)
      # Format 'b' as a binary string of length 'n', padded with zeros
      b_str = format(b, '0' + str(n) + 'b')

      # Each digit in the binary string corresponds to a qubit, 
      # if it is 1 apply an X-gate to that qubit
      for i, current_char in enumerate(b_str):
        if current_char == '1':
          oracle_qc.x(i)

      # Do the controlled-NOT gates for each qubit,
      # using the output qubit as the target
      for qubit in range(n):
        oracle_qc.cx(qubit, n)

      # Place the final X-gates
      for i, current_char in enumerate(b_str):
        if current_char == '1':
          oracle_qc.x(i)

    elif oracle_type == 'constant':
      # Decide what the fixed output of the oracle will be
      # (either always 0 or always 1)
      if np.random.choice([False, True]):
        oracle_qc.x(n)
    
    oracle_gate = oracle_qc.to_gate(label='Oracle')
    return oracle_gate

  ## Create the circuit
  def circuit(self, oracle_type='constant', n=1):
    circuit = QuantumCircuit(n + 1, n)
    # Initial setup: Input in state |+>, output in state |->
    circuit.x(n)
    for qubit in range(n + 1):
      circuit.h(qubit)

    # Create and append oracle
    circuit.append(self.create_oracle(oracle_type, n), range(n+1))
    
    # Finally, perform the H-gates again and measure
    for qubit in range(n):
      circuit.h(qubit)
      
    circuit.barrier()
    for i in range(n):
      circuit.measure(i, i)
    
    return circuit
