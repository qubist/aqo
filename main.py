from helpers import *

import time
import board
import busio
import adafruit_sgp30
import neopixel

BRIGHTNESS = 1


# set up pixel array
pixel_pin = board.D11
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=BRIGHTNESS, auto_write=True) # NOTE: Do I want auto-write here??

# Turn off board neopixel
neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)[0] = 0

# Set up I2C for CO2 sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
print("SGP30 serial #", [hex(i) for i in sgp30.serial])
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

elapsed_sec = 0
while True:

    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))

    eCO2, TVOC = sgp30.eCO2, sgp30.TVOC

    displayColor = mapFromTo(eCO2, 400,1900, 0,255)

    for i in range(num_pixels):
        pixels[i] = wheel(displayColor)

#    time.sleep(1)
#    elapsed_sec += 1
#    if elapsed_sec > 10:
#        elapsed_sec = 0
#        print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
#              % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))

#    pixels.show()
