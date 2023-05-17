#!/usr/bin/env python3

# Author: Vlatko Marchan-Sekulic

from subroutine.qsubroutine import QSubroutine
from qiskit import QuantumCircuit
from qiskit.circuit.library import CPhaseGate
from math import pi
import math
from fractions import Fraction
import random

class Shor(QSubroutine):
  def __init__(self):
    ## The name of the subroutine
    self.name = 'Shor Algorithm'
    ## A short description of the problem
    self.description = 'Shor\'s algorithm is a quantum algorithm that efficiently factors large integers'
    ## The required parameters to problem definition
    self.parameters = [
      {
        'type': 'int',
        'description': 'The number a',
        'constraint': 'Must be 8 or 13'
      },
    ]
    ## How to parse the input parameters
    self.parse_parameters = lambda parameters: [
      int(parameters[0]),
    ]

  ## Verify that the parameter are the number of qubits to use and a valid phase angle
  def check_parameters(self, parameters):
    if len(parameters) == 1 :
      try:
        return int(parameters[0]) == 8 or int(parameters[0]) == 13
      except:
        return False

  # Function that returns a circuit of n cubits, applying
  # the inverse of the Quantum Fourier Transform
  def reverse_rotations(self, qc, n): 
    for j in range(n):
      for m in range(j):
        qc.cp(-pi/float(2**(j-m)), m, j)
      qc.h(j)

  def qft_dagger(self, n):
    # Create a Quantum Circuit
    qft_dagger_circuit = QuantumCircuit(n)

    # Aply the QFT reverse rotations
    self.reverse_rotations(qft_dagger_circuit, n)

    gate = qft_dagger_circuit.to_gate()
    gate.name = "QFT_Dagger(" + str(n) + " qubits)"      
    return gate
  
  def c_amod21(self, circuit):
    n_count = 4
    circuit.barrier()
    circuit.cx(n_count-2, n_count-4)
    circuit.barrier()
    circuit.cx(n_count-1, n_count-4)
    circuit.cx(n_count-4, n_count-3)
    circuit.ccx(n_count-1,n_count-3,n_count-4)
    circuit.cx(n_count-4, n_count-3)
    circuit.barrier()
    circuit.x(n_count-4)
    circuit.ccx(n_count-0, n_count-4, n_count-3)
    circuit.x(n_count-4)
    circuit.cx(n_count-4, n_count-3)
    circuit.ccx(n_count-0,n_count-3,n_count-4)
    circuit.cx(n_count-4, n_count-3)
    circuit.barrier()
    return circuit

  ## Create the circuit
  def circuit(self, parameters):
    n_count = 5
    # Create QuantumCircuit with n_count counting qubits
    shor_circuit = QuantumCircuit(n_count, 3)

    for q in range(n_count-1, n_count-4, -1):
      shor_circuit.h(q)     # Initialize counting qubits in state |+>

    # Do controlled-U operations
    self.c_amod21(shor_circuit)

  
    # Do inverse-QFT Swap
    shor_circuit.append(self.qft_dagger(3), range(n_count-3, n_count, 1)) 
    shor_circuit.measure(range( n_count-1, n_count-4, -1), range(2, -1, -1))

    return shor_circuit


  ## A method to prepare the input
  def preprocessing(self, parameters):
    return parameters

  ## A method to process the output
  def postprocessing(self, counts, parameters):
    n = 21
    n_count = 3
    a = parameters[0]
    
    measured_phases = []
    for output in counts:
      decimal = int(output, 2)  # Convert (base 2) string to decimal
      phase = decimal/(2**n_count)  # Find corresponding eigenvalue
      measured_phases.append(phase)
    
    frac_denominators = list(map(lambda phase: Fraction(phase).limit_denominator(n).denominator, measured_phases))
    unique_denominators = set(frac_denominators)

    r = list(unique_denominators)

    result = []
    for period in r:
      if period % 2 == 1:
        continue
      result.append([math.gcd(pow(a,period//2)+1,n), math.gcd(pow(a,period//2)-1,n)])
    unique_results = list(set(map(tuple, result)))


    return unique_results if len(unique_results) > 0 else 'No result found'
    

    




