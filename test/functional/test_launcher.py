#!/usr/bin/env python3

import sys
import os
import signal
from environment import environment

def handle_signals():
     signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == "__main__":
     if len(sys.argv) < 2:
        print("missing build mode (release|debug)", file=sys.stderr)
        exit(1)

     build_mode = sys.argv[1]
     current_module_path = os.path.dirname(os.path.abspath(__file__))
     calculator_exec_path = current_module_path + "/../../bin/" + build_mode \
          + "/calculator"

     if not os.path.exists(calculator_exec_path):
          print("calculator executable doesn't exist to start tests",
                file=sys.stderr)
          exit(1)

     handle_signals()

     print("[START STATUS] initialize functional test environement...")

     try:
          env = environment(calculator_exec_path)

          if env.get_nb_test():
               print("[MIDDLE STATUS] running functional tests...")
               env.execute_all_tests()
          else:
               print("[MIDDLE STATUS] no functional test to execute")
     except Exception as e:
          print("[END STATUS] something wrong during test environment "
                f"execution : {str(e)}",
                file=sys.stderr)
          exit(1)
     except:
          print("[END STATUS] something wrong during test environment "
                "execution",
                file=sys.stderr)
          exit(1)
     else:
          print("[END STATUS] test environment execution has ended correctly")

     exit(0)
