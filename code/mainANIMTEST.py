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

DISPLAY_BRIGHTNESS = 1

# set up pixel array
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=DISPLAY_BRIGHTNESS, auto_write=True)

touch_pad = TOUCH_PIN
touch = touchio.TouchIn(touch_pad)

# VBatAnalogIn = AnalogIn(VBATPIN)
# def getBatteryVoltage():
#     return getVoltage(VBatAnalogIn) * 2

# Turn off board neopixel
neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)[0] = 0

# shows the color, lighting the pixels corresponding to 1s in a binary array
def showColor(color, mapping=[1,1,1,1,1,1,1,1]):
    # crawl the mapping and only light up the pixels which should be activated
    for n,m in enumerate(mapping):
        if m == 1:
            pixels[n] = displayColor
        else:
            pixels[n] = 0

tick = int(time.monotonic())

touched = False
mode = 0

color = 210

mapping = [1,1,1,1,1,1,1,1]
i = 0
toggle = 0

while True:

    # increase color value
    if touch.value:
        if color == 255:
            color = 0
        elif color == 210:
            time.sleep(.4)
            color += 1
        elif color == 120:
            color = 210
        else:
            color += 1

        print(color)
        time.sleep(0.015)

    c = wheel(color)
    displayColor = c # don't dim

    mapping[i] = toggle

    # increment i
    i += 1
    if i == 8:
        i = 0
        # toggle our toggler
        toggle ^= 1
    time.sleep(.01)


    pixelMapping = mapping

    showColor(displayColor, pixelMapping)
