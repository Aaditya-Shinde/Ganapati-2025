import time
import actions
import constants
from copy import copy

try:
    actions.setup()
    print("on")
    while True:
        actions.send_pattern(constants.all_on)

except KeyboardInterrupt:
    pass
finally:
    actions.cleanup()