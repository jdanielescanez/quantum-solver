
from qiskit import QuantumCircuit
from algorithms.qalgorithm import QAlgorithm

class SuperdenseCoding(QAlgorithm):
  def __init__(self):
    self.name = 'Superdense Coding'
    self.description = 'Transmit two classical bits using one qubit of communication'
    self.parameters = [
      {
        'type': 'string',
        'description': 'The message: two classical bits to transmit',
        'constraint': 'Must be a binary string of length two'
      }
    ]
    self.parse_result = lambda counts: list(counts.keys())[0]
    self.parse_parameters = lambda parameters: [parameters[0]]

  def check_parameters(self, parameters):
    if len(parameters) == 1 and type(parameters[0]) == str and len(parameters[0]) == 2:
      try:
        value = int(parameters[0], 2)
        return value >= 0 and value <= 3
      except:
        return False

  def create_bell_pair(self):
    bell_state_circuit = QuantumCircuit(2)
    bell_state_circuit.h(1)
    bell_state_circuit.cx(1, 0)
    return bell_state_circuit

  def encode_message(self, circuit, qubit, msg):
    if msg[0] == '1':
      circuit.z(qubit)
    if msg[1] == '1':
      circuit.x(qubit)
    return circuit

  def decode_message(self, circuit):
    circuit.cx(1, 0)
    circuit.h(1)
    return circuit

  def circuit(self, message):
    # Charlie creates the entangled pair between Alice and Bob
    circuit = self.create_bell_pair()
    circuit.barrier()

    # Alice gets the qubit 1 and bob gets the qubit 0
    alice_qubit = 1
    # Alice encodes her message onto qubit 1
    circuit = self.encode_message(circuit, alice_qubit, message)
    circuit.barrier()

    # Alice sends her qubit to Bob, and he decodes the message
    # using the qubit 1 (qubit of communication) and the qubit 0
    circuit = self.decode_message(circuit)

    # Finally, Bob measures the qubits to read Alice's message
    circuit.measure_all()

    return circuit
