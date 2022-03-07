
import sys
from bb84.bb84 import BB84

if __name__ == "__main__":
  token = sys.argv[1] if len(sys.argv) > 1 else None
  bb84 = BB84(token)
  bb84.run()
