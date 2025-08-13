import spidev
import time

# SPI bus configuration
spi_bus = 0
device = 0

# Initialize SPI
spi = spidev.SpiDev()
spi.open(spi_bus, device)
spi.max_speed_hz = 500000
spi.mode = 0

try:
    while True:
        spi.xfer([0b11111111]*30)  #  All LEDs on
        time.sleep(1)
        spi.xfer([0b00000000]*30)  #  All LEDs off
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")