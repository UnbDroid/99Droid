﻿from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


motor_left = Motor(Port.A) 
motor_right = Motor(Port.B)


motors = DriveBase(motor_left, motor_right, wheel_diameter = 42.1, axle_track = 111.2)

def move_forward(velocity):
    motors.drive(velocity, 0)
    
def move_forward_cm(cm) :
    motors.straight(cm/10)
    
def move_backward(velocity):
    motors.drive(-velocity, 0)
    
def move_backward_cm(cm) :
    motors.straight(-cm/10)
    
def turn_right(angle):
    motors.turn(angle)
    
def turn_left(angle):
    motors.turn(-angle)
    
def turn_90_left():
    motors.turn(-90)

def turn_90_right():
    motors.turn(90)
    
def turn_90_left_and_move_distance(distance):
    motors.straight(distance)
    motors.turn(-90)
    motors.stop()
    
def turn_90_right_and_move_distance(distance):
    motors.straight(distance)
    motors.turn(90)
    motors.stop()
    
def turn_180():
    motors.turn(180)
    
def stop():
    motors.stop()
