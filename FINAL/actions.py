import RPi.GPIO as GPIO
from constants import all_off, DATA_PINS, CLOCK_PINS, LATCH_PIN

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LATCH_PIN, GPIO.OUT)

    GPIO.setup(DATA_PINS[0], GPIO.OUT)
    GPIO.setup(DATA_PINS[1], GPIO.OUT)
    GPIO.setup(DATA_PINS[2], GPIO.OUT)
    GPIO.setup(DATA_PINS[3], GPIO.OUT)
    GPIO.setup(DATA_PINS[4], GPIO.OUT)
    GPIO.setup(DATA_PINS[5], GPIO.OUT)
    
    GPIO.setup(CLOCK_PINS[0], GPIO.OUT)
    GPIO.setup(CLOCK_PINS[1], GPIO.OUT)
    GPIO.setup(CLOCK_PINS[2], GPIO.OUT)
    GPIO.setup(CLOCK_PINS[3], GPIO.OUT)
    GPIO.setup(CLOCK_PINS[4], GPIO.OUT)
    GPIO.setup(CLOCK_PINS[5], GPIO.OUT)


def shift_out(groups):
    states = [GPIO.LOW, GPIO.HIGH]
    GPIO.output(LATCH_PIN, GPIO.LOW) 
    group_no = 0
    for group in groups:
        board_number = 1
        for byte in group:
            # print(f"group={group_no} board={len(group) - board_number} byte= {byte:08b}")
            i = 0
            for i in range(8):
                bit = (byte >> (7-i)) & 1
                GPIO.output(DATA_PINS[group_no], states[bit])
                GPIO.output(CLOCK_PINS[group_no], GPIO.HIGH)
                GPIO.output(CLOCK_PINS[group_no], GPIO.LOW)
            board_number += 1
        group_no += 1
    GPIO.output(LATCH_PIN, GPIO.HIGH)

def send_pattern(pattern):
    shift_out(all_off)
    shift_out(pattern)

def cleanup():
    shift_out(all_off)
    GPIO.cleanup()
    print("Cleaned")
