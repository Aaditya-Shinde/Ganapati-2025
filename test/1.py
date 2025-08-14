import spidev
import time
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz = 10000

LATCH_PIN = 8
DATA_PIN = 10
CLOCK_PIN = 11
NUM_CHIPS = 30
passme = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(LATCH_PIN, GPIO.OUT)
GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)

states = [GPIO.LOW, GPIO.HIGH]
def shift_out(byte_data, disp_seq):
    GPIO.output(LATCH_PIN, GPIO.LOW)
    count = 0
    for byte in byte_data:
        if disp_seq == 1:
            print("board number ")
            print(count)
        count = count+1
        for i in range(8):
            bit = (byte >> (7-i)) & 1
            if disp_seq == 1:
                print(bit)
            GPIO.output(DATA_PIN, states[bit])
            GPIO.output(CLOCK_PIN, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(CLOCK_PIN, GPIO.LOW)
    GPIO.output(LATCH_PIN, GPIO.HIGH)

#c0q7 = [0b00000000]*NUM_CHIPS
# c0q7[-1] = 0b10000000


offall = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]
# on = [0b11111111]*NUM_CHIPS
# on_byte = 0b11111111
custom = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000111, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b01000000, 0b11000000]

#shift_out(off)
try:
    # while True:
        # shift_out(on)#last ele to first chip, last bit to first led
        # time.sleep(1)
        # shift_out(off)
        # time.sleep(1)
        passme = 0
        shift_out(offall, passme)
        print("All turned OFF")
        passme = 1
        shift_out(custom, passme)
        print("SHIFTED")
        time.sleep(100)

except KeyboardInterrupt:
    pass
finally:
    shift_out(offall, passme)
    spi.close()
    GPIO.cleanup()
    print("Cleaned")