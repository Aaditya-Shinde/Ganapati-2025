import spidev
import RPi.GPIO as GPIO
import time

# === CONFIGURATION ===
NUM_CHIPS = 60
CHIPS_PER_GROUP = 10
NUM_GROUPS = NUM_CHIPS // CHIPS_PER_GROUP  # 6 groups of 10 chips

# BCM GPIO pins used for latch pins — change as needed
LATCH_PINS = [8, 25, 24, 23, 18, 15]

SPI_BUS = 0
SPI_DEVICE = 0    # Use CE0 only
SPI_SPEED_HZ = 20000  # 20kHz SPI clock speed

# === SETUP ===
GPIO.setmode(GPIO.BCM)
for pin in LATCH_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = SPI_SPEED_HZ

def latch_group(group_idx):
    """Pulse the latch pin for a specific group."""
    GPIO.output(LATCH_PINS[group_idx], GPIO.LOW)
    time.sleep(0.00001)  # small delay
    GPIO.output(LATCH_PINS[group_idx], GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(LATCH_PINS[group_idx], GPIO.LOW)

def shift_out_group(data, group_idx):
    """
    Shift out data to one group of chips and latch.
    Data must be a list of bytes (length == CHIPS_PER_GROUP).
    """
    if len(data) != CHIPS_PER_GROUP:
        raise ValueError(f"Data length {len(data)} != {CHIPS_PER_GROUP} chips per group")
    
    GPIO.output(LATCH_PINS[group_idx], GPIO.LOW)
    spi.writebytes(data)
    latch_group(group_idx)

try:
    while True:
        # Example pattern: scan a single lit LED across all chips and groups
        for group_idx in range(NUM_GROUPS):
            for bit_idx in range(CHIPS_PER_GROUP * 8):
                data = [0] * CHIPS_PER_GROUP
                chip = bit_idx // 8
                bit_pos = bit_idx % 8
                # Because data shifts out MSB first, index from the end
                data[CHIPS_PER_GROUP - 1 - chip] = 1 << bit_pos
                
                shift_out_group(data, group_idx)
                time.sleep(0.015)  # ~66 FPS per LED update

except KeyboardInterrupt:
    # Clear all LEDs on all groups
    for group_idx in range(NUM_GROUPS):
        shift_out_group([0] * CHIPS_PER_GROUP, group_idx)
    spi.close()
    GPIO.cleanup()
