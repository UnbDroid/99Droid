from pybricks.parameters import Port, Stop
from pybricks.ev3devices import Motor
from pybricks.tools import  StopWatch

motor_claw = Motor(Port.D)

time_open_claw = 3000
stopwatch = StopWatch() 

def open_claw():
    global time_claw_open
    motor_claw.run_time(200, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()
    if time_open_claw == 3000 :
        time_open_claw += 2000
    else :
        time_open_claw -= 2000

def close_claw() : 
    global time_claw_open
    time_open_claw = 3000
    motor_claw.run_time(-200, time_open_claw, Stop.HOLD, True)
    motor_claw.hold()
    