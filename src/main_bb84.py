#!/usr/bin/env python3

# Author: J. Daniel Escánez
# Ingeniería Informática - Universidad de La Laguna
# Trabajo Final de Grado: QuantumSolver

## BB84 Simulator Main Program

import sys
import signal
from bb84.bb84 import BB84

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  bb84 = BB84(token)
  bb84.run()
