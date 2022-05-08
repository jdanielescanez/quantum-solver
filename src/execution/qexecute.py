#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Fin de Grado: QuantumSolver

from qiskit import transpile, Aer
from qiskit.providers.ibmq import IBMQFactory
from qiskit.utils import QuantumInstance

## The component that manages the execution of quantum algorithms for QuantumSolver
class QExecute:
  ## Constructor
  def __init__(self, token: str = ''):
    # The token must be a IBM_QUANTUM_EXPERIENCE_TOKEN
    self.token = token
    self.backends = [Aer.get_backend('aer_simulator')]
    if self.token:
      self.provider = IBMQFactory().enable_account(self.token)
      self.backends += self.provider.backends()
    self.current_backend = None

  ## Current backend setter
  def set_current_backend(self, backend_name: str):
    if backend_name == 'aer_simulator':
      self.current_backend = self.backends[0]
    elif self.provider:
      self.current_backend = self.provider.get_backend(backend_name)

  ## Check if the guest mode is activated
  def is_guest_mode(self):
    return self.token == ''

  ## Print the available backends
  def print_avaiable_backends(self):
    print('\nAvaliable backends:')
    for i in range(len(self.backends)):
      backend = self.backends[i]
      status = backend.status()
      config = backend.configuration()
      jobs_in_queue = status.pending_jobs
      q_instance = QuantumInstance(backend)
      is_simulator = q_instance.is_simulator
      is_operational = status.operational

      print('[' + str(i + 1) + ']\tName:', str(backend), \
            '\n\tNumber of qubits:', str(config.n_qubits) + \
            '\n\tMaximum shots:', str(config.max_shots) + \
            '\n\tJobs in queue:', str(jobs_in_queue))
      print('\tIs ' + ('' if is_simulator else 'NOT ') + 'a simulator')
      if is_operational:
        print('\t✅ Is operational')
      else:
        print('\t❌ Is NOT operational')
      print()

  ## Backend selection menu
  def select_backend(self):
    range_backends = '[1 - ' + str(len(self.backends)) + ']'
    index = -2
    while index < 0 or index >= len(self.backends):
      msg = '[&] Select a backend of the list ' + str(range_backends) + ': '
      index = int(input(msg)) - 1
      if index == -1:
        self.current_backend = None
        print('[$] Backend not selected')
        return
      if index < 0 or index >= len(self.backends) or \
          not self.backends[index].status().operational:
        index = -1
        print('[!] The backend must be one of the list', range_backends, \
              'and must be operational')
      else:
        self.current_backend = self.backends[index]
        print('[$]', str(self.current_backend), 'selected')

  ## Run the circuit using the current backend
  def run(self, circuit: 'QuantumCircuit', n_shots: int):
    # Compile the circuit down to low-level QASM instructions
    # supported by the backend
    compiled_circuit = transpile(circuit, self.current_backend)
    # Execute the circuit on the current backend
    job = self.current_backend.run(compiled_circuit, shots=n_shots)

    # Return the counts from the job results
    return job.result().get_counts(compiled_circuit)
