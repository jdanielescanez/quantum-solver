#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from b92.participant import Participant
from qiskit import QuantumCircuit
from numpy.random import rand

## The Receiver entity in the B92 implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Receiver(Participant):
  ## Constructor
  def __init__(self, name='', original_bits_size=0):
    super().__init__(name, original_bits_size)

  ## Decode the message measuring the circuit (density-dependent)
  def decode_quantum_message(self, message, density, backend):
    ## The values of the participant
    self.values = []
    for i, qc in enumerate(message):
      qc.barrier()
      if rand() < density:
        is_hadamard_base = (self.axes[i] == 1)
        if is_hadamard_base:
          qc.h(0)
        qc.measure(0, 0)
        result = backend.run(qc, shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        if measured_bit == 1:
          self.values.append(int(not is_hadamard_base))
        else:
          self.values.append(-2)
      else:
        self.values.append(-1)
    return message

  def share_positive_readings_indexes(self):
    return list(map(lambda x: x >= 0, self.values))
