import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../src')

from flask import Flask, request
from quantum_solver.quantum_solver import QuantumSolver
from execution.qexecute import QExecute
from flask_cors import CORS

app = Flask(__name__)

# Members API Route

@app.route('/get-token', methods=['POST'])
def set_token():
  token = request.json['token']
  app.config['quantum_solver'] = QuantumSolver(token)
  try:
    app.config['quantum_solver'].qexecute = QExecute(app.config['quantum_solver'].token)
  except Exception as exception:
    print('Exception:', exception)
    return {'msg': 'Invalid token: "' + token + '". Try Again', 'err': True}
  return {'msg': 'Authenticated with token: ' + token, 'err': False}

@app.route('/token2')
def set_token2():
  return {"qc": str(app.config['quantum_solver'])}

CORS(app)

if __name__ == "__main__":
  app.run(debug=True)
