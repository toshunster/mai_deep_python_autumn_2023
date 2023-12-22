import os
import sys
import time
import signal

def signal_handler(signal_num, frame):
    print(f"Handle signal {signal_num}")

def exit_(signal_num, frame):
    print(f"Exit signal handler {signal_num}")
    sys.exit(1)

if __name__ == "__main__":
   signal.signal(signal.SIGUSR1, signal_handler)
   signal.signal(signal.SIGUSR2, exit_)
   print(f"pid={os.getpid()}")
   while True:
       time.sleep(0.5)
