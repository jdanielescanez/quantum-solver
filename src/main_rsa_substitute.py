#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

## RSA substitute Simulator Main Program

import signal
import sys
from rsa_substitute.rsa_substitute import RsaSubstitute

def signal_handler(sig, frame):
  print('\n\n[$] Exiting successfully\n')
  sys.exit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  token = sys.argv[1] if len(sys.argv) > 1 else None
  RsaSubstitute = RsaSubstitute(token)
  RsaSubstitute.run()
