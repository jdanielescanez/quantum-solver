import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../src')

from flask import Flask, request
from quantum_solver.quantum_solver import QuantumSolver
from execution.qexecute import QExecute
from flask_cors import CORS
from qiskit.utils import QuantumInstance
from qiskit import IBMQ

app = Flask(__name__)

def format_backends(backends):
  result = {'backends': [], 'current_backend': ''}
  for backend in backends:
    status = backend.status()
    is_operational = status.operational
    if is_operational:
      config = backend.configuration()
      jobs_in_queue = status.pending_jobs
      json_backend = {
        'name': str(backend),
        'n_qubits': config.n_qubits,
        'n_shots': config.max_shots,
        'jobs_in_queue': jobs_in_queue
      }
      result['backends'].append(json_backend)
  result['current_backend'] = result['backends'][0]
  return result

def format_algorithms(algorithms):
  result = {'algorithms': [], 'current_algorithm': ''}
  for i, algorithm in enumerate(algorithms):
    json_algorithm = {
      'id': i,
      'name': algorithm.name,
      'description': algorithm.description,
      'parameters': algorithm.parameters
    }
    result['algorithms'].append(json_algorithm)
  result['current_algorithm'] = result['algorithms'][0]
  return result

# Members API Route
@app.route('/reset-qexecute', methods=['POST'])
def reset_qexecute():
  if IBMQ.active_account():
    IBMQ.disable_account()
  return {'msg': 'Reseted qexecute', 'err': False}

@app.route('/set-token', methods=['POST'])
def set_token():
  token = request.json['token']
  app.config['quantum_solver'] = QuantumSolver(token)
  try:
    print('Loading account')
    app.config['quantum_solver'].qexecute = QExecute(app.config['quantum_solver'].token)
    print('Generating Backends')
    app.config['backends'] = format_backends(app.config['quantum_solver'].qexecute.backends)
    print('Generated Backends')
    return {'msg': 'Authenticated with token: ' + token, 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid token: "' + token + '". Try Again', 'err': True}

@app.route('/get-backends', methods=['GET'])
def get_backends():
  return app.config['backends']

@app.route('/get-algorithms', methods=['GET'])
def get_algorithms():
  return format_algorithms(app.config['quantum_solver'].qalgorithm_manager.algorithms)

@app.route('/are-algorithm-params', methods=['GET'])
def are_algorithm_params():
  json_algorithm_params = {
    'is_algorithm': app.config['quantum_solver'].qalgorithm_manager.current_algorithm != None, 
    'are-params': app.config['quantum_solver'].qalgorithm_manager.parameters != None
  }
  print(str(json_algorithm_params))
  return json_algorithm_params

@app.route('/set-backend', methods=['POST'])
def set_backend():
  backend_name = request.json['name']
  try:
    app.config['quantum_solver'].qexecute.set_current_backend(backend_name)
    return {'msg': 'Selected ' + backend_name, 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid backend: "' + backend_name + '". Try Again', 'err': True}

@app.route('/set-algorithm', methods=['POST'])
def set_algorithm():
  algorithm_id = request.json['id']
  try:
    app.config['quantum_solver'].qalgorithm_manager.set_current_algorithm(int(algorithm_id))
    algorithm_name = app.config['quantum_solver'].qalgorithm_manager.current_algorithm.name
    return {'msg': 'Selected ' + algorithm_name, 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid algorithm with id: "' + algorithm_id + '". Try Again', 'err': True}

CORS(app)

if __name__ == "__main__":
  app.run(debug=True)
