from helpers import *

import time
import board
import busio
import adafruit_sgp30
import neopixel

DISPLAY_BRIGHTNESS = 1
# number of entries to average to get the displayed value
BLUR_AMOUNT = 10

# set up pixel array
pixel_pin = board.D11
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=DISPLAY_BRIGHTNESS, auto_write=True) # NOTE: Do I want auto-write here??

# Turn off board neopixel
neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)[0] = 0

# Set up I2C for CO2 sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
print("SGP30 serial #", [hex(i) for i in sgp30.serial])
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

# set up list of last values to update and average
vals = [400 for x in range(BLUR_AMOUNT)]

def avg(lst):
    return sum(lst)/BLUR_AMOUNT

while True:

    # grab the carbon dioxide and TVOC levels from the sensor
    eCO2, TVOC = sgp30.eCO2, sgp30.TVOC

    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))

    # remove oldest datapoint from our list of values and add the new datapoint
    vals.remove(vals[0])
    vals.append(eCO2)

    print(vals)

    # the value we'll work with is the average of our list of values
    blurredVal = avg(vals)

    displayWheelPos = mapFromTo(blurredVal, 400,1900, 0,255)
    displayColor = wheel(displayWheelPos)
    pixels.fill(displayColor)

#    pixels.show()
