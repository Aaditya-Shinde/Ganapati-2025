import time
import actions
import constants

try:
    actions.setup()
    while True:
        base = constants.all_off
        group, board, bit = map(int, input("Group(0-5) Board(0-9) Bit(0-7): ").split())
        base[group][-(board+1)] |= 1 << bit
        print(f"{base[group][-(board+1)]:08b}")
        actions.send_pattern(base)

except KeyboardInterrupt:
    pass
finally:
    actions.cleanup()