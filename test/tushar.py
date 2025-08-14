import time
import RPi.GPIO as GPIO

LATCH_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(LATCH_PIN, GPIO.OUT)

DATA_PINS = [10, 14]
CLOCK_PINS = [11, 15]
GPIO.setup(DATA_PINS[0], GPIO.OUT)
GPIO.setup(CLOCK_PINS[0], GPIO.OUT)
GPIO.setup(DATA_PINS[1], GPIO.OUT)
GPIO.setup(CLOCK_PINS[1], GPIO.OUT)
# GPIO.setup(DATA_PINS[2], GPIO.OUT)
# GPIO.setup(CLOCK_PINS[2], GPIO.OUT)
# GPIO.setup(DATA_PINS[3], GPIO.OUT)
# GPIO.setup(CLOCK_PINS[4], GPIO.OUT)

all_off = [
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
]
all_groups = [
    [0b00000001, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
    [0b10000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000],
]

states = [GPIO.LOW, GPIO.HIGH]

def send_signal(groups, printme):
    GPIO.output(LATCH_PIN, GPIO.LOW) 
    group_no = 0
    for group in groups:
        board_number = 1
        for byte in group:
            if printme:
                print('-'*20)
                print(f"group={group_no} board={len(group) - board_number} byte= {bin(byte)}")
            i = 0
            for i in range(8):
                bit = (byte >> (7-i)) & 1
                if printme:
                    print(bit)
                GPIO.output(DATA_PINS[group_no], states[bit])
                GPIO.output(CLOCK_PINS[group_no], GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(CLOCK_PINS[group_no], GPIO.LOW)
            board_number += 1
        group_no += 1
    GPIO.output(LATCH_PIN, GPIO.HIGH)

try:
    send_signal(all_off, False)
    print("All turned OFF")
    time.sleep(1)
    send_signal(all_groups, True)
    print("SHIFTED")
    time.sleep(100)
except Exception as e:
    print('*'*50)
    print(e)
    print('*'*50)
finally:
    send_signal(all_off, False)
    GPIO.cleanup()
    print("Cleaned")