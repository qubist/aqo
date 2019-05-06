import time
import board
import busio
import adafruit_sgp30
import neopixel
import touchio
from analogio import AnalogIn

from helpers import *

PIXEL_PIN = board.D11
NUM_PIXELS = 8

# pin with touch sensitivity
TOUCH_PIN = board.A0

# pin with battery voltage for checking battery level
VBATPIN = board.D9

DISPLAY_BRIGHTNESS = 1

# number of entries to average to get the displayed value
# the higher this is, the slower and smoother color transitions will be
# 60-80 seems to be good for nice slow transitions while staying responsive
BLUR_AMOUNT = 25

LOWBAT_PULSE_SPEED = 200
LOWBAT_PULSE_DEPTH = 200

# voltages at which low battery mode is turned off or on when battery voltage is
# ascending or descending
VBAT_DESCENT_THRESHOLD = 3.35
VBAT_ASCENT_THRESHOLD = 3.45

# in each mode, how much to dim the pixels and how many of the pixels to light
DEFAULT_DIM_FACTOR = 1 # don't dim in mode 0
DEFAULT_DIM_MAPPING = [1,1,1,1,1,1,1,1]

FIRST_DIM_FACTOR  = 1 # don't dim
FIRST_DIM_MAPPING = [0,1,0,0,1,0,0,1]

SECOND_DIM_FACTOR = 20 # dim a lot mode 2
SECOND_DIM_MAPPING = [1,0,0,0,0,0,0,0]

# set up pixel array
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=DISPLAY_BRIGHTNESS, auto_write=True)

touch_pad = TOUCH_PIN
touch = touchio.TouchIn(touch_pad)

# VBatAnalogIn = AnalogIn(VBATPIN)
# def getBatteryVoltage():
#     return getVoltage(VBatAnalogIn) * 2

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

# returns a value on the color wheel described in the wheel() function
# based a given CO2 level
def getWheelValueFromCO2(CO2):
    if inRange(CO2, 400,450):
        return mapFromTo(CO2, 400,450, 210,255)
    elif inRange(CO2, 450,600):
        return mapFromTo(CO2, 450,600, 0,55)
    elif inRange(CO2, 600,1300):
        return mapFromTo(CO2, 600,1300, 55,85)
    elif inRange(CO2, 1300,2500):
        return mapFromTo(CO2, 1300,2500, 85,95)
    elif inRange(CO2, 2500,5000):
        return mapFromTo(CO2, 2500,5000, 95,120)
    else:
        return 120

# returns a color
def getColorFromCO2(CO2):
    return wheel(getWheelValueFromCO2(CO2))

# shows the color, lighting the pixels corresponding to 1s in a binary array
def showColor(color, mapping=[1,1,1,1,1,1,1,1]):
    # crawl the mapping and only light up the pixels which should be activated
    for n,m in enumerate(mapping):
        if m == 1:
            pixels[n] = displayColor
        else:
            pixels[n] = 0

# set up list of last values to update and average
vals = [400 for x in range(BLUR_AMOUNT)]
# batLow = False
tick = int(time.monotonic())

touched = False
mode = 0

while True:
    # update which second are we on, and save the last one
    lastTick = [tick][0]
    tick = int(time.monotonic())

    # check touches and cycle through brightness modes if a new touch is detected
    if touch.value:
        if touched == False:
            # activate touch functions
            # print("TOUCHED!")
            # increment mode
            mode = increment(mode)

            touched = True
    else:
        touched = False

    # grab the carbon dioxide and TVOC levels from the sensor
    # eCO2, TVOC = sgp30.eCO2, sgp30.TVOC
    eCO2 = sgp30.eCO2

    # only do the following every 10 seconds (on rising edge of 10th second)
    # if tick % 10 == 0 and lastTick %10 != 0:
    #     # get the battery voltage
    #     voltage = getBatteryVoltage()
    #     print(voltage)
    #     if batLow == False and voltage <= VBAT_DESCENT_THRESHOLD:
    #         batLow = True
    #     elif batLow == True and voltage >= VBAT_ASCENT_THRESHOLD:
    #         batLow = False

    # remove oldest datapoint from our list of values and add the new datapoint
    vals.remove(vals[0])
    vals.append(eCO2)

    # the value we'll work with is the average of our list of values
    blurredVal = avg(vals)

    # print(vals)
    print("eCO2 = %d ppm" % (sgp30.eCO2))
    # print(blurredVal)
    # print(voltage)

    c = getColorFromCO2(blurredVal)
    if mode == 0:
        displayColor = c # don't dim
        pixelMapping = DEFAULT_DIM_MAPPING
    elif mode == 1:
        displayColor = dim(c, FIRST_DIM_FACTOR)
        pixelMapping = FIRST_DIM_MAPPING
    elif mode == 2:
        displayColor = dim(c, SECOND_DIM_FACTOR) # SuperDim for nighttime :)
        pixelMapping = SECOND_DIM_MAPPING

    # pulse the display color if in low battery mode
    # if batLow == True:
        # ShowColor(pulse(displayColor, LOWBAT_PULSE_SPEED, LOWBAT_PULSE_DEPTH), pixelMapping)
    # otherwise just display the color
#    else:
    showColor(displayColor, pixelMapping)
