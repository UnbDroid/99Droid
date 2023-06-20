from pybricks.ev3devices import (ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port


color_front_sensor = ColorSensor(Port.S4) 
ultrasonic_front_sensor = UltrasonicSensor(Port.S3)