
from bb84.participant import Participant
from qiskit import QuantumCircuit

class Sender(Participant):
  def __init__(self, name='', original_bits_size=0):
    super().__init__(name, original_bits_size)
    
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