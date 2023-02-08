#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from qiskit import QuantumCircuit
from algorithms.qalgorithm import QAlgorithm

## A Superdense Coding Implemetation for QuantumSolver
## @see https://qiskit.org/textbook/ch-algorithms/superdense-coding.html
class SuperdenseCoding(QAlgorithm):
  ## Constructor
  def __init__(self):
    ## The name of the algorithm
    self.name = 'Superdense Coding'
    ## A short description
    self.description = 'Transmit two classical bits using one qubit of communication'
    ## The required parameters for the algorithm
    self.parameters = [
      {
        'type': 'string',
        'description': 'The message: two classical bits to transmit',
        'constraint': 'Must be a binary string of length two'
      }
    ]
    ## How to parse the result of the circuit execution
    self.parse_result = lambda counts: list(counts.keys())[0]
    ## How to parse the input parameters
    self.parse_parameters = lambda parameters: [parameters[0]]

  ## Verify that the parameter is a valid message (a binary string of two bits)
  def check_parameters(self, parameters):
    if len(parameters) == 1 and type(parameters[0]) == str and len(parameters[0]) == 2:
      try:
        value = int(parameters[0], 2)
        return value >= 0 and value <= 3
      except:
        return False

  ## Create the simplest (and maximal) example of quantum entanglement
  def create_bell_pair(self):
    bell_state_circuit = QuantumCircuit(2)
    bell_state_circuit.h(1)
    bell_state_circuit.cx(1, 0)
    return bell_state_circuit

  ## Encode a message
  def encode_message(self, circuit, qubit, msg):
    if msg[0] == '1':
      circuit.z(qubit)
    if msg[1] == '1':
      circuit.x(qubit)
    return circuit

  ## Decode a message
  def decode_message(self, circuit):
    circuit.cx(1, 0)
    circuit.h(1)
    return circuit

  ## Create the circuit
  def circuit(self, message):
    # Charlie creates the entangled pair between Alice and Bob
    circuit = self.create_bell_pair()
    circuit.barrier()

    # Alice gets the qubit 1 and bob gets the qubit 0
    alice_qubit = 1
    # Alice encodes her message onto qubit 1
    circuit = self.encode_message(circuit, alice_qubit, message)
    circuit.barrier()

    # Alice sends her qubit to Bob, and he decodes the message
    # using the qubit 1 (qubit of communication) and the qubit 0
    circuit = self.decode_message(circuit)

    # Finally, Bob measures the qubits to read Alice's message
    circuit.measure_all()

    return circuit
