
import sys
import os
import matplotlib.pyplot as plt
import base64
import hashlib
from io import BytesIO
import secrets
import time

from flask import Flask, request
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

from qiskit.utils import QuantumInstance
from qiskit.visualization import plot_histogram

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../src')

from quantum_solver.quantum_solver import QuantumSolver
from execution.qexecute import QExecute

app = Flask(__name__)

def timeout_job():
  for session_token in list(app.config['USERS'].keys()):
    time_since_login = time.time() - app.config['USERS'][session_token]['time']
    SECONDS_IN_TWO_HOURS = 60 * 60 * 2
    if time_since_login > SECONDS_IN_TWO_HOURS:
      app.config['USERS'].pop(session_token)

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

def format_parameters(parameters):
  result = {'params': [], 'params_values': []}
  for _, parameter in enumerate(parameters):
    json_parameter = {
      'type': parameter['type'],
      'description': parameter['description'],
      'constraint': parameter['constraint']
    }
    result['params'].append(json_parameter)
  return result

# Members API Route
@app.route('/set-token', methods=['POST'])
def set_token():
  token = request.json['token']
  if request.json['guest_mode_flag']:
    session_token = secrets.token_urlsafe(16)
  else:
    session_token = request.json['token']

  hashed_token = hashlib.md5(session_token.encode()).hexdigest()
  app.config['USERS'][hashed_token] = {}
  app.config['USERS'][hashed_token]['time'] = time.time()
  app.config['USERS'][hashed_token]['quantum_solver'] = QuantumSolver(token)
  try:
    print('Loading account')
    app.config['USERS'][hashed_token]['quantum_solver'].qexecute = QExecute(app.config['USERS'][hashed_token]['quantum_solver'].token)
    print('Generating Backends')
    app.config['USERS'][hashed_token]['backends'] = format_backends(app.config['USERS'][hashed_token]['quantum_solver'].qexecute.backends)
    print('Generated Backends')
    return {'msg': session_token, 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid token: "' + token + '". Try Again', 'err': True}

@app.route('/get-backends', methods=['GET'])
def get_backends():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  return app.config['USERS'][hashed_token]['backends']

@app.route('/get-algorithms', methods=['GET'])
def get_algorithms():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  return format_algorithms(app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.algorithms)

@app.route('/get-params', methods=['GET'])
def get_params():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  return format_parameters(app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.current_algorithm.parameters)

@app.route('/get-backend-algorithm-params', methods=['GET'])
def get_backend_algorithm_params():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  algorithm_name = 'None'
  current_algorithm = app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.current_algorithm
  if current_algorithm != None:
    algorithm_name = current_algorithm.name
  json_algorithm_params = {
    'algorithm': algorithm_name,
    'backend': str(app.config['USERS'][hashed_token]['quantum_solver'].qexecute.current_backend),
    'params': str(app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.parameters)
  }
  print('json_algorithm_params', str(json_algorithm_params))
  return json_algorithm_params

@app.route('/set-backend', methods=['POST'])
def set_backend():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  backend_name = request.json['name']
  try:
    app.config['USERS'][hashed_token]['quantum_solver'].qexecute.set_current_backend(backend_name)
    return {'msg': 'Selected ' + backend_name, 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid backend: "' + str(backend_name) + '". Try Again', 'err': True}

@app.route('/set-algorithm', methods=['POST'])
def set_algorithm():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.parameters = None
  algorithm_id = request.json['id']
  try:
    app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.set_current_algorithm(int(algorithm_id))
    algorithm_name = app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.current_algorithm.name
    return {'msg': 'Selected ' + algorithm_name, 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid algorithm with id: "' + str(algorithm_id) + '". Try Again', 'err': True}

@app.route('/set-params-values', methods=['POST'])
def set_params_values():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  params_values = request.json['params_values']
  try:
    assert app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.current_algorithm.check_parameters(params_values)
    parsed_params = app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.current_algorithm.parse_parameters(params_values)
    app.config['USERS'][hashed_token]['quantum_solver'].qalgorithm_manager.parameters = parsed_params
    return {'msg': 'Setted parameters: ' + str(parsed_params), 'err': False}
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid parameters: "' + str(params_values) + '". Try Again', 'err': True}

@app.route('/run', methods=['POST'])
def run():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  try:
    output, circuit = app.config['USERS'][hashed_token]['quantum_solver'].run_algorithm()

    circuit.draw(output='mpl')
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    image_base64 = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    app.config['USERS'][hashed_token]['output'] = {'output': output, 'image_base64': image_base64, 'err': False}
  except Exception as exception:
    print('Exception:', str(exception))
    app.config['USERS'][hashed_token]['output'] = {'output': str(exception), 'image_base64': '', 'err': True}
  return app.config['USERS'][hashed_token]['output']

@app.route('/run-experimental-mode', methods=['POST'])
def run_experimental_mode():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  try:
    n_shots = request.json['n_shots']
    output = app.config['USERS'][hashed_token]['quantum_solver'].experimental_mode(n_shots)
    info = get_backend_algorithm_params()
    info['n_shots'] = n_shots
    info_string = info['algorithm'] + ', ' + info['backend'] + ', ' + info['params'] + ', n_shots: ' + str(info['n_shots'])

    plot_histogram(output, title='QuantumSolver - Experimental Mode\n' + info_string)
    tmpfile = BytesIO()
    plt.tight_layout()
    plt.savefig(tmpfile, format='png')
    image_base64 = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    app.config['USERS'][hashed_token]['output'] = {'output': str(output), 'image_base64': image_base64, 'err': False}
  except Exception as exception:
    print('Exception:', str(exception))
    app.config['USERS'][hashed_token]['output'] = {'output': str(exception), 'image_base64': '', 'err': True}
  return app.config['USERS'][hashed_token]['output']

@app.route('/get-output', methods=['GET'])
def get_ouput():
  token = request.headers.get('token')
  hashed_token = hashlib.md5(token.encode()).hexdigest()
  return app.config['USERS'][hashed_token]['output']

CORS(app)

scheduler = BackgroundScheduler()
job = scheduler.add_job(timeout_job, 'interval', minutes=1)
scheduler.start()

if __name__ == "__main__":
  app.config['USERS'] = {}
  app.run(debug=True)
