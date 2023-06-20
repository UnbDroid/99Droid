from pybricks.parameters import Port
from pybricks.ev3devices import Motor
from pybricks.tools import  StopWatch, Stop

motor_claw = Motor(Port.D)

time_open_claw = 0 
stopwatch = StopWatch() 

def open_claw():
    global time_open_claw
    while stopwatch.time() < time_open_claw : 
        motor_claw.run(200) 
    motor_claw.hold() 

def close_claw() : 
    global time_claw_open 
    stopwatch.reset() 
    time_open_claw.run_target(-200, -90, then=Stop.HOLD, wait=False) 
    time_claw_open = stopwatch.time() 
    time_open_claw.hold() 
    