#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

## QuantumSolver Crypto Main Program

import signal
import sys
from crypto.crypto_manager import CryptoManager

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  crypto_manager = CryptoManager(token)
  crypto_manager.run()
