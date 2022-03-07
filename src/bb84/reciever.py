
from qiskit import QuantumCircuit, assemble
from numpy.random import rand, randint
from bb84.bb84 import N_BITS

class Reciever:
  def __init__(self, name, original_bits_size):
    self.name = name
    self.original_bits_size = original_bits_size
    self.values = None
    self.axes = None
    self.key = None
    self.safe_key = False
    self.otp = None

  def set_axes(self, axes=None):
    if axes == None:
      self.axes = randint(2, size=self.original_bits_size)
    else:
      self.axes = axes

  def show_values(self):
    print('\n', self.name, 'Values:')
    print(self.values)

  def show_axes(self):
    print('\n', self.name, 'Axes:')
    print(self.axes)

  def show_key(self):
    print('\n', self.name, 'Key:')
    print(self.key)

  def remove_garbage(self, another_axes):
    self.key = []
    for i in range(self.original_bits_size):
      if self.axes[i] == another_axes[i]:
        self.key.append(self.values[i])
    self.key

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

  def confirm_key(self, shared_size):
    self.key = self.key[shared_size:]
    self.safe_key = True

  def generate_otp(self):
    self.otp = []
    for i in range(len(self.key) // N_BITS):
      bits_string = ''.join(map(str, self.key[i * N_BITS: (i + 1) * N_BITS]))
      self.otp.append(int(bits_string, 2))

  def decode_otp_message(self, encoded_message):
    decoded_message = ''
    CHR_LIMIT = 1114112
    for i, char in enumerate(encoded_message):
      decoded_message += chr((ord(char) - self.otp[i % len(self.otp)]) % CHR_LIMIT)
    return decoded_message
