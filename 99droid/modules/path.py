from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch

from modules.motors import *
from modules.colors import *
from modules.detect import *

def follow_line() :
    global count
    move_forward(140)
    if (saw_black_left() and saw_black_right()) :
        pass
    elif saw_black_left() :
        turn_90_left_and_move_distance(50)
    elif saw_black_right() :
        turn_90_right_and_move_distance(50)

#Funções referentes ao trajeto do robô

def go_to_passengers() :
    global count
    count = 0
    while not (saw_red_left() and saw_red_right()) :
        follow_line()
    count += 1
    print("count + 1")
    turn_90_left_and_move_distance(100)
    if (saw_red_left() or saw_red_right()) :
        move_forward_cm(10)
    while count < 3 :
        if saw_red_right() :
            move_forward_cm(10)
            count += 1
            if (count != 3 and saw_red_right()) : 
                while (saw_red_left() or saw_red_right()) : 
                    move_forward_cm(1)
        follow_line()

def pick_passenger() : 
   
    stopwatch.reset() 
    while (color_front_sensor.reflection() < 1 ): 
     #   print(color_front_sensor.reflection())
        move_right(30) 
    time_spin = stopwatch.time()
    stop() 
    move_forward_cm(10) 
    stop() 
    if (distance_front() < 10) : 
        passenger_size = 15 
    else :
        passenger_size = 10 
    close_claw() 
    move_backward_cm(10) 
    stop()
    stopwatch.reset() 
    while (stopwatch.time() < time_spin) : 
        move_left(30) 
        
def go_to_cinema() : 
    turn180()
    while (saw_red_left() or saw_red_right()) : 
        move_forward(140)
    while (not saw_red_left() and saw_red_right()) : 
        follow_line()
    stop() 
    turn_90_left_and_move_distance(100)
    move_forward_cm(10)
    open_claw() 
    move_forward_cm(10) 
    turn_90_left() 
    while (saw_red_left() or saw_red_right() ): 
        move_forward(150)
    while not saw_red_left() and saw_red_right() : 
        follow_line() 
    move_forward_cm(10) 
    
def go_to_lanchonete() : 
    while (saw_red_left() or saw_red_right()) :
        move_forward(150) 

    while not saw_red_left() and saw_red_right() :
        follow_line() 

    stop() 
    move_forward_cm(10) 
    turn_90_right() 
    move_forward_cm(10) 
    abreGarra()
    move_backward_cm(10)
    turn_90_right()
    while(saw_red_left() or saw_red_right()): 
        move_forward(150)
    while not saw_red_left() and saw_red_right() :
        follow_line() 
    move_forward_cm(10) 
    turn180() 
    
def go_to_school() : 
    while (saw_red_left() or saw_red_right()) : 
        move_forward(150)
    for cont in range(3) :
        follow_line() 
        if (saw_red_left() or saw_red_right()) : 
            cont += 1 
            move_forward_cm(10) 
            if (saw_red_right() and cont != 3 ): 
                move_forward_cm(5)

    stop()
    move_forward_cm(10) 
    turn_90_right() 
    move_forward_cm(10) 
    abreGarra()
    move_backward_cm(10)
    turn_90_right()
    
    while saw_red_left() or saw_red_right() :
        move_forward(180)

    for cont in range(3) : 
        follow_line()
        if saw_red_left() or saw_red_right() :
            cont += 1
            move_forward_cm(10)
            if saw_red_right() and cont != 3 :
                move_forward_cm(5)

    move_forward_cm(10) 
    turn180() 
    
def drop_passenger() :
    global total_of_passengers
    global total_of_passengers_of_15cm
    global total_of_passengers_of_10cm
    global passenger_size

    if total_of_passengers == 1 :
        if passenger_size == 15 :
            go_to_lanchonete()
        else :
            go_to_cinema()
        total_of_passengers += 1
    elif total_of_passengers == 2 :
        if passenger_size == 15 :
            if total_of_passengers_of_15cm == 1 :
                go_to_lanchonete()
            elif total_of_passengers_of_15cm == 2 :
                go_to_school()
        else :
            if total_of_passengers_of_10cm == 1 :
                go_to_cinema()
            elif total_of_passengers_of_10cm == 2 :
                go_to_school()
        total_of_passengers += 1
    elif total_of_passengers >= 3 :
        if passenger_size == 15 :
            if total_of_passengers_of_15cm == 1 :
                go_to_lanchonete()
            elif total_of_passengers_of_15cm == 2 :
                go_to_school()
            elif total_of_passengers_of_15cm == 3 :
                go_to_cinema()
        else :
            if total_of_passengers_of_10cm == 1 :
                go_to_cinema()
            elif total_of_passengers_of_10cm == 2 :
                go_to_school()
            elif total_of_passengers_of_10cm == 3 :
                go_to_lanchonete()
        total_of_passengers += 1

#-------------------------------------------------------------------------------------------------------