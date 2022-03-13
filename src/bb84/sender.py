
from bb84.participant import Participant
from qiskit import QuantumCircuit
from numpy.random import randint
from bb84.bb84 import N_BITS
from math import ceil

class Sender(Participant):
  def encode_quantum_message(self):
    encoded_message = []
    for i in range(len(self.axes)):
      qc = QuantumCircuit(1, 1)
      if self.values[i] == 1:
        qc.x(0)
      if self.axes[i] == 1:
        qc.h(0)
      encoded_message.append(qc)
    return encoded_message