import time
import board
import busio
import adafruit_sgp30
import neopixel
from analogio import AnalogIn

from helpers import *

PIXEL_PIN = board.D11
NUM_PIXELS = 8

# pin with battery voltage for checking battery level
VBATPIN = board.D9

DISPLAY_BRIGHTNESS = 1

# number of entries to average to get the displayed value
# the higher this is, the slower and smoother color transitions will be
# 60-80 seems to be good for nice slow transitions while staying responsive
BLUR_AMOUNT = 75

LOWBAT_PULSE_SPEED = 200
LOWBAT_PULSE_DEPTH = 200

VBAT_DESCENT_THRESHOLD = 3.4
VBAT_ASCENT_THRESHOLD = 3.55

# set up pixel array
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=DISPLAY_BRIGHTNESS, auto_write=True) # NOTE: Do I want auto-write here??

VBatAnalogIn = AnalogIn(VBATPIN)
def getBatteryVoltage():
    return getVoltage(VBatAnalogIn) * 2

# Turn off board neopixel
neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)[0] = 0

# Set up I2C for CO2 sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
print("SGP30 serial #", [hex(i) for i in sgp30.serial])
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8aae)

def avg(lst):
    return sum(lst)/BLUR_AMOUNT

# set up list of last values to update and average
vals = [400 for x in range(BLUR_AMOUNT)]

batLow = False
tick = int(time.monotonic())

while True:
    # update which second are we on, and save the last one
    lastTick = [tick][0]
    tick = int(time.monotonic())

    # grab the carbon dioxide and TVOC levels from the sensor
    eCO2, TVOC = sgp30.eCO2, sgp30.TVOC
    # eCO2 = sgp30.eCO2

    # only do the following every 10 seconds (on rising edge of 10th second)
    if tick % 10 == 0 and lastTick %10 != 0:
        # get the battery voltage
        voltage = getBatteryVoltage()
        print(voltage)
        if batLow == False and voltage <= VBAT_DESCENT_THRESHOLD:
            batLow = True
        elif batLow == True and voltage >= VBAT_ASCENT_THRESHOLD:
            batLow = False

    # remove oldest datapoint from our list of values and add the new datapoint
    vals.remove(vals[0])
    vals.append(eCO2)

    # the value we'll work with is the average of our list of values
    blurredVal = avg(vals)

    # print(vals)
    # print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    print(blurredVal)
    # print(voltage)

    displayWheelPos = mapFromTo(blurredVal, 400,1900, 0,255)
    displayColor = wheel(displayWheelPos)
    if batLow == True:
        pixels.fill(pulse(displayColor, LOWBAT_PULSE_SPEED, LOWBAT_PULSE_DEPTH))
    else:
        pixels.fill(displayColor)

#    pixels.show()
