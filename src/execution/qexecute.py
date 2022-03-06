
from qiskit import IBMQ, transpile

class QExecute:
  # token must be a IBM_QUANTUM_EXPERIENCE_TOKEN
  def __init__(self, token: str):
    self.token = token
    self.provider = IBMQ.enable_account(self.token)
    self.backends = self.provider.backends()
    self.current_backend = None
    
  def set_current_backend(self, backend_name: str):
    self.current_backend = self.provider.get_backend(backend_name)

  def print_avaiable_backends(self):
    print('\nAvaliable backends:')
    for i in range(len(self.backends)):
      backend = self.backends[i]
      status = backend.status()
      is_operational = status.operational
      jobs_in_queue = status.pending_jobs
      config = backend.configuration()
      print('[' + str(i + 1) + ']\tName:', str(backend), '\n\t'\
            'Is ' + ('' if is_operational else 'NOT ') + 'operational', \
            '\n\tJobs in queue:', str(jobs_in_queue) + \
            '\n\tNumber of qubits:', str(config.n_qubits) + '\n')

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

  def run(self, circuit: 'QuantumCircuit', n_shots: int):
    # Compile the circuit down to low-level QASM instructions
    # supported by the backend
    compiled_circuit = transpile(circuit, self.current_backend)
    # Execute the circuit on the current backend
    job = self.current_backend.run(compiled_circuit, shots=n_shots)

    # Return the counts from the job results
    return job.result().get_counts(compiled_circuit)
