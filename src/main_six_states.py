#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

## BB84 Simulator Main Program

import signal
import sys
from six_states.six_states import SixStates

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  bb84 = SixStates(token)
  bb84.run()
