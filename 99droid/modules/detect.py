from pybricks.ev3devices import (ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port


color_front_sensor = ColorSensor(Port.S4) 
ultrasonic_front_sensor = UltrasonicSensor(Port.S3)

def distance_front() : 
    return ultrasonic_front_sensor.distance()/10 