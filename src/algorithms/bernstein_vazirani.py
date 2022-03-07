
from qiskit import QuantumCircuit

class BernsteinVazirani:
  def __init__(self):
    self.name = 'Bernstein Vazirani'
    self.description = 'Using an oracle: f(x) = (s * x) % 2. Obtain s (a secret number)'
    self.parameters = [
      {
        'type': 'string',
        'description': 'The secret binary number s, to generate the oracle',
        'constraint': 'The length must be smaller than the number of qubits of the selected backend'
      }
    ]
    self.n_shots = 1
    self.parse_result = lambda counts: list(counts.keys())[0]
    self.parse_parameters = lambda array: [array[0]]

  def circuit(self, secret_number):
    n = len(secret_number)
    n_range = list(range(n))
    # Create a Quantum Circuit acting on the q register
    circuit = QuantumCircuit(n + 1, n)
    
    circuit.x(n)
    circuit.h(n_range + [n])

    circuit.barrier()

    for i, char in enumerate(reversed(secret_number)):
      if char == '1':
        circuit.cx(i, n)

    circuit.barrier()

    circuit.h(n_range)

    # Map the quantum measurement to the classical bits
    circuit.measure(n_range, n_range)

    return circuit
