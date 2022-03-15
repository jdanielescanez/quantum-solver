
from bb84.participant import Participant
from qiskit import QuantumCircuit, assemble
from numpy.random import rand, randint
from bb84.participant import N_BITS
from math import ceil

class Reciever(Participant):
  def decode_quantum_message(self, message, density, backend):
    self.values = []
    for i, qc in enumerate(message):
      qc.barrier()
      if rand() < density:
        if self.axes[i] == 1:
          qc.h(0)
        qc.measure(0, 0)
        qobj = assemble(qc, shots=1, memory=True)
        result = backend.run(qobj).result()
        measured_bit = int(result.get_memory()[0])
        self.values.append(measured_bit)
      else:
        self.values.append(-1)
    return message
