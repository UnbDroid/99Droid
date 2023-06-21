from pybricks.parameters import  Color
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor

sensor_color_left = ColorSensor(Port.S1) 
sensor_color_right = ColorSensor(Port.S2) 

def calibration(sensor):
    print(sensor.rgb())

#Declaration of RGB values of color sensors
#left

def red_left() :
    return sensor_color_left.rgb()[0]

def green_left() :
    return sensor_color_left.rgb()[1]

def blue_left() :
    return sensor_color_left.rgb()[2]

#right

def red_right() :
    return sensor_color_right.rgb()[0]

def green_right() :
    return sensor_color_right.rgb()[1]

def blue_right() :
    return sensor_color_right.rgb()[2]

#Declaration of detected colors

def saw_black_left() :
    return red_left() < 18 and green_left() < 18 and blue_left() < 18

def saw_black_right() :
    return red_right() < 18 and green_right() < 18 and blue_right() < 18

def saw_red_left() :
    return red_left() > (green_left() + blue_left())

def saw_red_right() :
    return red_right() > (green_right() + blue_right())