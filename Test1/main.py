import spidev
import time
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz = 1000000

LATCH_PIN = 25
NUM_CHIPS = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LATCH_PIN, GPIO.OUT)

def shift_out(byte_data):
    GPIO.output(LATCH_PIN, 0)
    spi.writebytes(byte_data)
    GPIO.output(LATCH_PIN, 1)

try:
    while True:
        for i in range(8):
            shift_out([1<<i])
            time.sleep(0.1)

        for i in reversed(range(8)):
            shift_out([1<<i])
            time.sleep(0.1)
            
except KeyboardInterrupt:
    shift_out([0 for i in range(NUM_CHIPS)])
    spi.close()
    GPIO.cleanup()
    print("Cleaned")
