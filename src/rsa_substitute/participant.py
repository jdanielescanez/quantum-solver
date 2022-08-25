#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from abc import ABC, abstractmethod
from qiskit import QuantumCircuit

## An abstract class of a participant entity in the RSA substitute protocol implementation
## @see https://journals.aijr.org/index.php/ajgr/article/view/699/168
class Participant(ABC):
  ## Constructor
  @abstractmethod
  def __init__(self, name=''):
    ## The name of the participant
    self.name = name

  @abstractmethod
  def encode(self, message):
    pass
  
  @abstractmethod
  def decode(self, message):
    pass

  def U_power(self, theta, phi, lam, power):
    u_gate = QuantumCircuit(1)
    for _ in range(power):
      u_gate.u(theta, phi, lam, u_gate.qubits[0])
    
    label = 'U_' + str(power) + ' ~ 𝜃:' + str(round(theta, 2))
    label += ' 𝜑:' + str(round(phi, 2)) + ' 𝜆:' + str(round(lam, 2))
    qc = QuantumCircuit(1, 1)
    qc.append(u_gate.to_gate(label=label), [0])
    return qc
