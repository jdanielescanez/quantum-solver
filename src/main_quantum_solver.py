
import sys
from quantum_solver.quantum_solver import QuantumSolver

if __name__ == "__main__":
  quantum_solver = QuantumSolver(sys.argv)
  quantum_solver.run()
