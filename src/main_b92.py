#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

## B92 Simulator Main Program

import signal
import sys
from b92.b92 import B92

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  b92 = B92(token)
  b92.run()
