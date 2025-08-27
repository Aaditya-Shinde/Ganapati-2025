import time
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

# = 2
DELAY = 0.2
try:
   send_signal(all_off)
   print("*******All turned OFF********")
   send_signal(all_on)
   print("all_on")
   send_signal(all_off)
   print("*******All turned OFF********")
   send_signal(pattern)
   print("pattern")
   time.sleep(1000)
    # time.sleep(5)
    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l1)
    # print("l1")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l2)
    # print("l2")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l3)
    # print("l3")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l4)
    # print("l4")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l5)
    # print("l5")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l6)
    # print("l6")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l7)
    # print("l7")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l8)
    # print("l8")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l9)
    # print("l9")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l9)
    # print("l9")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l9)
    # print("l9")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l9)
    # print("l9")
    # time.sleep(DELAY)

    # send_signal(all_off)
    # print("*******All turned OFF********")
    # send_signal(l9)
    # print("l9")

    # time.sleep(1000)
   
except Exception as e:
    print('*'*50)
    print(e)
    print('*'*50)
finally:
    send_signal(all_off)
    GPIO.cleanup()
    print("Cleaned")
