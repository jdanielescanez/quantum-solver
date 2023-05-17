#!/usr/bin/env python3

# Author: Vlatko Marchan-Sekulic

from subroutine.qsubroutine import QSubroutine
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library import CPhaseGate

# Import Numpy
import numpy as np
from scipy.linalg import solve, LinAlgError
from sympy import Matrix

from qiskit.visualization import plot_histogram

class Simon(QSubroutine):
  def __init__(self):
    ## The name of the subroutine
    self.name = 'Simon Algorithm'
    ## A short description of the problem
    self.description = 'Simon algorithm is a quantum algorithm that finds a hidden bit string in a black-box function with exponential speedup over classical algorithms.'
    ## The required parameters to problem definition
    self.parameters = [
      {
        'type': 'string',
        'description': 'Binary string to generate the oracle that simulates the black box function',
        'constraint': 'Must be a binary string of length 3 or more (limit imposed by the backend used number qubits / 2)'
      },
    ]
    ## How to parse the input parameters
    self.parse_parameters = lambda parameters: [
      parameters[0]
    ]

  ## Verify that the parameter are the number of qubits to use and a valid phase angle
  def check_parameters(self, parameters):
    if len(parameters) == 1:
      try:
        if all(char in "01" for char in parameters[0]) and len(parameters[0]) > 2:
          return str(parameters[0]) 
      except:
        return False

  def oracle(self, b, qr, cr):
    size_register = len(b)
    simon_oracle_circuit = QuantumCircuit(qr, cr)

    # Copy the first register in the second
    for i in range(size_register):
      simon_oracle_circuit.cx(i, size_register+i)

    # The first value of b = 1 is obtained starting 
    # from the end of the string, and then the corresponding CNOTs are applied
    pos_first_register = 0
    for i in range (size_register-1, -1, -1):
      if b[i] == '1':
        pos_second_register = size_register
        for j in range(size_register-1, -1, -1):
          if b[j] == '1':
            simon_oracle_circuit.cx(pos_first_register, pos_second_register)
          pos_second_register += 1
        break
      pos_first_register += 1
    
    # Obtain the random permutations of the qubits
    permutations = list(np.random.permutation(size_register))

    # Random permutation of the qbits of the second register
    init = list(range(size_register))
    i = 0
    while i < size_register:
      if init[i] != permutations[i]:
        k = permutations.index(init[i])
        simon_oracle_circuit.swap(size_register+i, size_register+k)
        init[i], init[k] = init[k], init[i] 
      else:
        i += 1
    
    # Randomly flip the qubit
    for i in range(size_register):
      if np.random.random() > 0.5:
        simon_oracle_circuit.x(size_register+i)
    
    return simon_oracle_circuit
  

  ## Create the circuit
  def circuit(self, b):
    size_circuit = len(b)

    # Create Quantum Registers
    qr = QuantumRegister(size_circuit * 2)
    # Create Classical Registers
    cr = ClassicalRegister(size_circuit)

    # Create Quantum Circuit
    simon_circuit = QuantumCircuit(qr, cr)

    # Apply Hadamard gate to the first register
    simon_circuit.h(qr[0:size_circuit])

    # Apply barrier
    simon_circuit.barrier()

    # Apply the oracle
    simon_oracle_circuit = self.oracle(b, qr, cr)
    simon_circuit += simon_oracle_circuit

    # Apply barrier
    simon_circuit.barrier()

    # Apply Hadamard gate to the first register
    simon_circuit.h(qr[0:size_circuit])

    # Measure the first register
    simon_circuit.measure(qr[0:size_circuit], cr[0:size_circuit])

    return simon_circuit

  ## A method to prepare the input
  def preprocessing(self, parameters):
    return parameters


  # Solve equation system
  def get_solution(self, counts):
    equations = []
    for measurement in counts:
      if int(measurement) != 0:
        equations.append([int(c) for c in measurement])
    A = Matrix(equations)
    nullspace = A.nullspace()
    return ''.join([str(int(x)).replace("-","") for x in nullspace[0]]) if nullspace else None

  ## A method to process the output
  def postprocessing(self, counts, parameters):
    result = counts
    shots = int(sum(counts.values()))
    n = len(parameters[0])

    print("\n\nResult equation system:")
    # Show the ecuation system
    for z in result:
      if not all(char in "0" for char in z):
        accum = 0
        equation = f" b * {z} = "
        terms = []
        for i in range(n):
          terms.append(f"b{i} * {z[i]}")
        equation += " + ".join(terms)
        equation += f" =  0  (mod 2) ({result[z]*100/shots:.2f}%)"

        print(equation)
    
    # Solve the system of equations
    # Eliminate the rows with all zeros
    aux = []
    for z in result:
      if not all(char in "0" for char in z) and z not in aux:
        aux.append(z)

    # Check if there is enough data to form a matrix
    num_rows = len(aux)
    num_cols = n
    if num_rows < num_cols:
      print(f"Not enough data to form a matrix (need at least {num_cols} equations)")
      return "error"

    # Create the matrix A and the vector b
    A = np.array([[int(i) for i in z] for z in aux])
    b = np.zeros(len(aux))


    print("\nSolving the system of equations...")
    try:
      b = self.get_solution(result)
    except Exception as e:
      return "Error solving the system of equations:" + str(e)

    # Print the values of b0, b1, ..., bn-1
    return b if (b != None) else "".join([str(int(0)) for x in range(n)])
