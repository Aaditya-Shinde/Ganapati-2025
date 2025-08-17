import time
import actions
import constants
from copy import copy
import os

def printBase(base):
    for i in range(len(base)):
        for j in range(10):
            byte = ["0"]*8
            for k in range(8):
                if base[i][-(j+1)] >> k:
                    byte[-(k+1)] = "\033[32m1\033[0m"
                else:
                    byte[-(k+1)] = "\033[31m0\033[0m"
            print(f"group:{i} board:{j}     {''.join(byte)}")
        print()
        print()

try:
    actions.setup()
    while True:
        for board in range(10):
            for bit in range(8):
                base = [constants.all_off[0]]
                base[0][-(board+1)] |= 1 << bit
                printBase(base)
                actions.send_pattern(base)
                input("next:")

except KeyboardInterrupt:
    pass
finally:
    actions.cleanup()