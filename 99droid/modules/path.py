from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *

count = 0 
passenger_size = 0 
total_of_passengers = 1
total_of_passengers_of_10cm = 1
total_of_passengers_of_15cm = 1
time_forward = 0

def follow_line() :
    move_forward(120)
    if (saw_black_left() and saw_black_right()) :
        pass
    elif saw_black_left() :
        turn_left(30)
    elif saw_black_right() :
        turn_right(30)

#Funções referentes ao trajeto do robô

def go_to_passengers() :
    global count
    global time_forward
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
            move_forward_cm(13.5)
            count += 1
            if (count != 3 and saw_red_right()) : 
                while (saw_red_left() or saw_red_right()) : 
                    move_forward_cm(1)
        follow_line()
    turn_90_right()

def pick_passenger() : 
    global passenger_size
    global time_forward
    if total_of_passengers > 1 :
        turn_90_right()
    stopwatch.reset()
    while not saw_blue_left() and not saw_blue_right() :
        move_forward(60)
    stop()
    time_forward = stopwatch.time()
    move_forward_cm(3)
    turn_90_left()
    stopwatch.reset() 
    while (color_front_sensor.reflection() < 1 ): 
        # print(color_front_sensor.reflection())
        move_right(30) 
    turn_right(10)
    time_spin = stopwatch.time()
    stop() 
    
    move_forward_cm(7) 
    stop() 
    close_claw()
    if (distance_front() > 200) : 
        passenger_size = 15
        print("É O JÚLIO!")
    else :
        passenger_size = 10
        print("É A JESS!")
    move_backward_cm(7) 
    stop()
    stopwatch.reset() 
    while (stopwatch.time() < time_spin) : 
        move_left(30)
    turn_90_right() 
    move_backward_cm(3)
    while not saw_blue_left() and not saw_blue_right() :
        move_backward(60)
    stop()
    stopwatch.reset()
    while stopwatch.time() < time_forward :
        move_backward(60)
    stop()
    turn_90_left()
        
def go_to_cinema() : 
    turn_180()
    while (saw_red_left() or saw_red_right()) : 
        move_forward(140)
    while (not saw_red_left() and not saw_red_right()) : 
        follow_line()
    stop() 
    turn_90_left_and_move_distance(100)
    move_forward_cm(10)
    open_claw() 
    move_backward_cm(10) 
    turn_90_left() 
    while (saw_red_left() or saw_red_right() ): 
        move_forward(150)
    while not saw_red_left() and not saw_red_right() : 
        follow_line() 
    move_forward_cm(13.5)
    
def go_to_lanchonete() : 
    while (saw_red_left() or saw_red_right()) :
        move_forward(150) 

    while not saw_red_left() and not saw_red_right() :
        follow_line() 

    stop() 
    move_forward_cm(10) 
    turn_90_right() 
    move_forward_cm(10) 
    open_claw()
    move_backward_cm(10)
    turn_90_right()
    while(saw_red_left() or saw_red_right()): 
        move_forward(150)
    while not saw_red_left() and not saw_red_right() :
        follow_line() 
    move_forward_cm(13.5) 
    turn_180() 
    
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
    open_claw()
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

    move_forward_cm(13.5) 
    turn_180() 
    
def drop_passenger() :
    global total_of_passengers
    global total_of_passengers_of_15cm
    global total_of_passengers_of_10cm
    global passenger_size

    if total_of_passengers == 1 :
        if passenger_size == 15 :
            print("Partiu levar Júlio na Lanchonete")
            go_to_lanchonete()
            total_of_passengers_of_15cm += 1

        else :
            print("Partiu levar Jess no Cinema")
            go_to_cinema()
            total_of_passengers_of_10cm += 1
            
        total_of_passengers += 1

    elif total_of_passengers == 2 :
        if passenger_size == 15 :
            if total_of_passengers_of_15cm == 1 :
                print("Partiu levar Júlio na Lanchonete")
                go_to_lanchonete()
                total_of_passengers_of_15cm += 1
                

            elif total_of_passengers_of_15cm == 2 :
                print("Partiu levar Júlio na Escola")
                go_to_school()
                total_of_passengers_of_15cm += 1
        else :
            if total_of_passengers_of_10cm == 1 :
                print("Partiu levar Jess no Cinema")
                go_to_cinema()
                total_of_passengers_of_10cm += 1
            elif total_of_passengers_of_10cm == 2 :
                print("Partiu levar Jess na Escola")
                go_to_school()
                total_of_passengers_of_10cm += 1
        total_of_passengers += 1
    elif total_of_passengers >= 3 :
        if passenger_size == 15 :
            if total_of_passengers_of_15cm == 1 :
                print("Partiu levar Júlio na Lanchonete")
                go_to_lanchonete()
                total_of_passengers_of_15cm += 1
            elif total_of_passengers_of_15cm == 2 :
                print("Partiu levar Júlio na Escola")
                go_to_school()
                total_of_passengers_of_15cm += 1
            elif total_of_passengers_of_15cm == 3 :
                print("Partiu levar Júlio no Cinema")
                go_to_cinema()
                total_of_passengers_of_15cm += 1
        else :
            if total_of_passengers_of_10cm == 1 :
                print("Partiu levar Jess no Cinema")
                go_to_cinema()
                total_of_passengers_of_10cm += 1
            elif total_of_passengers_of_10cm == 2 :
                print("Partiu levar Jess na Escola")
                go_to_school()
                total_of_passengers_of_10cm += 1
            elif total_of_passengers_of_10cm == 3 :
                print("Partiu levar Jess na Lanchonete")
                go_to_lanchonete()
                total_of_passengers_of_10cm += 1
        total_of_passengers += 1

#-------------------------------------------------------------------------------------------------------