#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

## QuantumSolver AI Main Program

import signal
import sys
from ai.quantum_solver_ai import QuantumSolverAI

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  qs_ai = QuantumSolverAI(token)
  qs_ai.run()
