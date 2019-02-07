import time

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)

def dim(color, factor):
    r, g, b = color
    dimmedColor = int(r/factor), int(g/factor), int(b/factor)
    return dimmedColor

# pulses the input color's brightness according to the device time
# speed: the speed at which the pulse pulses. 100 is medium, 300 is very slow.
# depth: how dim the pulse gets at its dimmest. higher values are less
#        dim. 10 is medium, 2 is very deep, 30 is very shallow.
def pulse(color, speed, depth):
    milliseconds = int(time.monotonic()*100)
    # print("time:",time.monotonic())
    timeValue = abs(milliseconds % speed - speed//2)
    # print(timeValue)
    dimAmount = timeValue/depth + 1
    # print(dimAmount)
    return dim(color, dimAmount)

# x:input value;
# a,b:input range
# c,d:output range
# y:return value
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y
