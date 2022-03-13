
import sys
import signal
from quantum_solver.quantum_solver import QuantumSolver

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  quantum_solver = QuantumSolver(token)
  quantum_solver.run()
