import time
import actions
import constants
from copy import copy
import os

try:
    actions.setup()
    while True:
        base = [
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
]
        group, board, bit = map(int, input("Group(0-5) Board(0-9) Bit(0-7): ").split())
        os.system("clear")
        base[group][-(board+1)] |= 1 << bit
        for i in range(6):
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
        actions.send_pattern(base)

except KeyboardInterrupt:
    pass
finally:
    actions.cleanup()