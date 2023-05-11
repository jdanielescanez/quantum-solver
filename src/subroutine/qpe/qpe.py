#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from subroutine.qsubroutine import QSubroutine
from qiskit import QuantumCircuit
from qiskit.circuit.library import CPhaseGate
from math import pi

class QPE(QSubroutine):
  def __init__(self):
    ## The name of the subroutine
    self.name = 'Quantum Phase Estimation'
    ## A short description of the problem
    self.description = 'Estimates the eigenvalue of an eigenvector of a unitary operator'
    ## The required parameters to problem definition
    self.parameters = [
      {
        'type': 'int',
        'description': 'The number of estimation qubits to be used',
        'constraint': 'Must be a positive number'
      },
      {
        'type': 'float',
        'description': 'The phase of the unitary operator',
        'constraint': 'Must be a float number'
      }
    ]
    ## How to parse the input parameters
    self.parse_parameters = lambda parameters: [
      int(parameters[0]),
      float(parameters[1])
    ]

  ## Verify that the parameter are the number of qubits to use and a valid phase angle
  def check_parameters(self, parameters):
    if len(parameters) == 2:
      try:
        return int(parameters[0]) and float(parameters[1]) > 0
      except:
        return False

  # Function that returns a circuit of n cubits, applying
  # the inverse of the Quantum Fourier Transform
  def qft_dagger(self, n):
    qc = QuantumCircuit(n, name='QFT^-1')
    for i in range(n // 2):
      qc.swap(i, n - i - 1)
    for j in range(n):
      for k in range(j):
          qc.cp(- pi / float(2 ** (j - k)), k, j)
      qc.h(j)
    return qc

  ## Create the circuit
  def circuit(self, n=3, phase=pi):
    range_list = list(range(n))
    qc = QuantumCircuit(n + 1, n)
      
    # Inicialización del circuito con los n primeros cúbits en el estado |+> y el último en estado |1>
    qc.h(range_list)
    qc.x(n)
    qc.barrier()
    
    # Aplicación de las potencias de 2 de la fase de phase controlada,
    # con controles desde 0 hasta n - 1 y objetivos en n 
    cu = CPhaseGate(phase) 
    for i in range_list:
      cu_power = cu.power(2 ** i)
      qc.append(cu_power, [i, n])
      
    # Apply inverse QFT
    qc_qft_dagger = self.qft_dagger(n).to_gate()
    qc.append(qc_qft_dagger, range_list)

    # Measure the first n qubits
    qc.barrier()
    qc.measure(range_list, range_list)

    return qc

  ## A method to prepare the input
  def preprocessing(self, parameters):
    return parameters

  ## A method to process the output
  def postprocessing(self, counts, parameters):
    n = parameters[0]
    max_value = [key for key, value in counts.items() if value == max(counts.values())][0]
    return int(max_value, 2) / 2 ** n
