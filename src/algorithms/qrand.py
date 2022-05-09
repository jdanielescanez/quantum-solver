#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import QuantumCircuit
from algorithms.qalgorithm import QAlgorithm

## A Quantum Algorithm to obtain random numbers for QuantumSolver
class QRand(QAlgorithm):
  ## Constructor
  def __init__(self):
    ## The name of the algorithm
    self.name = 'QRand'
    ## A short description
    self.description = 'Gives a random number between 0 and 2 ^ n_qubits - 1'
    ## The required parameters for the algorithm
    self.parameters = [
      {
        'type': 'int',
        'description': 'A positive number of qubits to use',
        'constraint': 'Can\'t be bigger than the number of qubits of the selected backend'
      }
    ]
    ## How to parse the result of the circuit execution
    self.parse_result = lambda counts: int(list(counts.keys())[0], 2)
    ## How to parse the input parameters
    self.parse_parameters = lambda parameters: [int(parameters[0])]

  ## Verify that the parameter is the number of qubits to use
  def check_parameters(self, parameters):
    if len(parameters) == 1 and type(parameters[0]) == str:
      try:
        return int(parameters[0]) > 0
      except:
        return False

  ## Create the circuit
  def circuit(self, n=1):
    # Create a Quantum Circuit
    circuit = QuantumCircuit(n, n)
    n_range = list(range(n))

    # Add a H gate on every qubit
    circuit.h(n_range)

    circuit.barrier()

    # Map the quantum measurement to the classical bits
    circuit.measure(n_range, n_range)

    return circuit
