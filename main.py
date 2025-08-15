import time
import RPi.GPIO as GPIO
from consants import all_groups_pattern_0, all_groups_pattern_1, all_groups_pattern_2, all_groups_pattern_3, all_groups_pattern_4, all_off, DATA_PINS, CLOCK_PINS, LATCH_PIN



GPIO.setmode(GPIO.BCM)
GPIO.setup(LATCH_PIN, GPIO.OUT)

GPIO.setup(DATA_PINS[0], GPIO.OUT)
GPIO.setup(CLOCK_PINS[0], GPIO.OUT)
GPIO.setup(DATA_PINS[1], GPIO.OUT)
GPIO.setup(CLOCK_PINS[1], GPIO.OUT)
GPIO.setup(DATA_PINS[2], GPIO.OUT)
GPIO.setup(CLOCK_PINS[2], GPIO.OUT)

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
                GPIO.output(CLOCK_PINS[group_no], GPIO.LOW)
            board_number += 1
        group_no += 1
    GPIO.output(LATCH_PIN, GPIO.HIGH)

try:
    print("*******All turned OFF********")
    while True:
        send_signal(all_off)
        send_signal(all_groups_pattern_0)
        time.sleep(0.3)
        send_signal(all_off)
        send_signal(all_groups_pattern_1)
        time.sleep(0.3)
        send_signal(all_off)
        send_signal(all_groups_pattern_2)
        time.sleep(0.3)
        send_signal(all_off)
        send_signal(all_groups_pattern_3)
        time.sleep(0.3)
        send_signal(all_off)
        send_signal(all_groups_pattern_4)
        time.sleep(0.3)
        print("***********Shifted***********")
    time.sleep(1000)
except Exception as e:
    print('*'*50)
    print(e)
    print('*'*50)
finally:
    send_signal(all_off)
    GPIO.cleanup()
    print("Cleaned")