import time
<<<<<<< HEAD
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
=======
import RPi.GPIO as GPIO
from consants import *



GPIO.setmode(GPIO.BCM)
GPIO.setup(LATCH_PIN, GPIO.OUT)

GPIO.setup(DATA_PINS[0], GPIO.OUT)
GPIO.setup(CLOCK_PINS[0], GPIO.OUT)
GPIO.setup(DATA_PINS[1], GPIO.OUT)
GPIO.setup(CLOCK_PINS[1], GPIO.OUT)
GPIO.setup(DATA_PINS[2], GPIO.OUT)
GPIO.setup(CLOCK_PINS[2], GPIO.OUT)
GPIO.setup(DATA_PINS[3], GPIO.OUT)
GPIO.setup(CLOCK_PINS[3], GPIO.OUT)
GPIO.setup(DATA_PINS[4], GPIO.OUT)
GPIO.setup(CLOCK_PINS[4], GPIO.OUT)
GPIO.setup(DATA_PINS[5], GPIO.OUT)
GPIO.setup(CLOCK_PINS[5], GPIO.OUT)

states = [GPIO.LOW, GPIO.HIGH]

def send_signal(groups):
    GPIO.output(LATCH_PIN, GPIO.LOW) 
    group_no = 0
    for group in groups:
        board_number = 1
        for byte in group:
            print(f"group={group_no} board={len(group) - board_number} byte= {byte:08b}")
            i = 0
            for i in range(8):
                bit = (byte >> (7-i)) & 1
                GPIO.output(DATA_PINS[group_no], states[bit])
                GPIO.output(CLOCK_PINS[group_no], GPIO.HIGH)
                # time.sleep(0.00001)
                GPIO.output(CLOCK_PINS[group_no], GPIO.LOW)
            board_number += 1
        group_no += 1
    GPIO.output(LATCH_PIN, GPIO.HIGH)

DELAY = 2
try:
    send_signal(all_off)
    print("*******All turned OFF********")
    send_signal(all_on)
    print("all_on")
    time.sleep(DELAY)
    send_signal(all_off)
    print("*******All turned OFF********")
    send_signal(pattern)
    print("pattern")
    time.sleep(1000)
except Exception as e:
    print('*'*50)
    print(e)
    print('*'*50)
finally:
    send_signal(all_off)
    GPIO.cleanup()
    print("Cleaned")
>>>>>>> aaditya
