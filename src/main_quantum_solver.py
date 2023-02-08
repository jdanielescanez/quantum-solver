#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

## QuantumSolver Main Program

import signal
import sys
from quantum_solver.quantum_solver import QuantumSolver

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  quantum_solver = QuantumSolver(token)
  quantum_solver.run()
