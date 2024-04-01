#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from crypto.bb84.participant import Participant
from numpy.random import rand

## The Receiver entity in the BB84 implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Receiver(Participant):
  ## Constructor
  def __init__(self, name='', original_bits_size=0, receiver_id=0):
    super().__init__(name, original_bits_size)
    self.receiver_id = receiver_id

  ## Decode the message measuring the circuit (density-dependent)
  def decode_quantum_message(self, message, density):
    ## The values of the participant
    self.values = []
    for i, qc in enumerate(message):
      qc.barrier()
      if rand() < density:
        if self.axes[i] == 1:
          qc.h(0)
        qc.measure(0, self.receiver_id)
        if self.axes[i] == 1:
          qc.h(0)
        self.values.append(-2)
      else:
        self.values.append(-1)
    return message
