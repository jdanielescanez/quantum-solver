#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from crypto.six_state.participant import Participant
from qiskit import QuantumCircuit
from numpy.random import rand
from qiskit import transpile

## The Receiver entity in the Six-State implementation
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
        if self.axes[i] == 1:
          qc.h(0)
        elif self.axes[i] == 2:
          qc.append(self.hy, [0])
        qc.measure(0, 0)
        transpiled_qc = transpile(qc, backend=backend)
        result = backend.run(transpiled_qc, shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        self.values.append(measured_bit)
      else:
        self.values.append(-1)
    return message
