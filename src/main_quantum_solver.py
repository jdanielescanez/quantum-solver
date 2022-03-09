
import sys
from quantum_solver.quantum_solver import QuantumSolver

if __name__ == "__main__":
  token = sys.argv[1] if len(sys.argv) > 1 else None
  quantum_solver = QuantumSolver(token)
  quantum_solver.run()
