#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from e91.receiver import Receiver
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from numpy.random import uniform

## The Eveasdropper entity in the E91 implementation
## @see https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
class Eveasdropper(Receiver):
  ## Constructor
  def __init__(self, name='', original_bits_size=0, qr=QuantumRegister(2, name="qr"), cr=ClassicalRegister(4, name="cr")):
    super().__init__(name, original_bits_size, qr, cr)

    ## Chosen measurements setter
  def set_axes(self, axes=None, density=0.0):
    self._calculate_measurements()
    if axes == None:
      self.axes = []
      for _ in range(self.original_bits_size):
        if uniform(0, 1) <= density:
          if uniform(0, 1) <= 0.5: # in 50% of cases perform the WW measurement
            self.axes.append(['ea2', 'eb1'])
          else: # in 50% of cases perform the ZZ measurement
            self.axes.append(['ea3', 'eb2'])
        else:
          self.axes.append(None)
    else:
      self.axes = axes

  def _calculate_measurements(self):
    self.measurements = {}
    qr = self.qr
    cr = self.cr
    # Measurement of the spin projection of Alice's qubit onto the a_2 direction (W basis)
    self.measurements['ea2'] = QuantumCircuit(qr, cr, name='measureEA2')
    self.measurements['ea2'].s(qr[0])
    self.measurements['ea2'].h(qr[0])
    self.measurements['ea2'].t(qr[0])
    self.measurements['ea2'].h(qr[0])
    self.measurements['ea2'].measure(qr[0], cr[2])

    # Measurement of the spin projection of Allice's qubit onto the a_3 direction (standard Z basis)
    self.measurements['ea3'] = QuantumCircuit(qr, cr, name='measureEA3')
    self.measurements['ea3'].measure(qr[0], cr[2])

    # Measurement of the spin projection of Bob's qubit onto the b_1 direction (W basis)
    self.measurements['eb1'] = QuantumCircuit(qr, cr, name='measureEB1')
    self.measurements['eb1'].s(qr[1])
    self.measurements['eb1'].h(qr[1])
    self.measurements['eb1'].t(qr[1])
    self.measurements['eb1'].h(qr[1])
    self.measurements['eb1'].measure(qr[1], cr[3])

    # Measurement of the spin projection of Bob's qubit onto the b_2 direction (standard Z measurement)
    self.measurements['eb2'] = QuantumCircuit(qr, cr, name='measureEB2')
    self.measurements['eb2'].measure(qr[1], cr[3])

  # Create the key with the circuit measurement results
  def create_values(self, result, circuits):
    for i in range(self.original_bits_size):
      if self.axes[i] != None:
        res = list(result.get_counts(circuits[i]).keys())[0]
        self.values.append([int(res[0]), int(res[1])])
      else:
        self.values.append([None, None])
