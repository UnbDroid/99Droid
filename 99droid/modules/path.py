from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch
from pybricks.hubs import EV3Brick

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.claw import *

ev3 = EV3Brick()

count = 0 
count_turns_left = 0
count_turns_right = 0
passenger_size = 0 
total_of_passengers = 1
total_of_passengers_of_10cm = 1
total_of_passengers_of_15cm = 1
time_forward = 0

def follow_line() :
    global count_turns_left
    global count_turns_right
    move_forward(120)
    if (saw_black_left() and saw_black_right()) :
        pass
    elif saw_black_left() :
        turn_left(30)
        count_turns_left += 1
    elif saw_black_right() :
        turn_right(30)
        count_turns_right += 1

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
    turn_left(20)
    degrees_turned = 0
    initial_distance = distance_front()
    while degrees_turned < 40 :
        print(distance_front())
        if distance_front() < (initial_distance * 0.80) :
            passenger_size = 15
            print("É O JÚLIO!")
        turn_right(1)
        degrees_turned += 1
    if passenger_size != 15 :
        passenger_size = 10
        print("É A JESS!")
    turn_left(20)
    move_forward_cm(7) 
    stop() 
    close_claw()
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
    global count_turns_left
    global count_turns_right
    turn_180()
    while (saw_red_left() or saw_red_right()) : 
        move_forward(140)
    count_turns_left = 0
    count_turns_right = 0
    while not saw_red_left() and not saw_red_right() and (count_turns_left < 2 or count_turns_right < 2) : 
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
    global count_turns_left
    global count_turns_right
    while (saw_red_left() or saw_red_right()) :
        move_forward(150) 

    count_turns_left = 0
    count_turns_right = 0

    while not saw_red_left() and not saw_red_right() and (count_turns_left < 2 or count_turns_right < 2) :
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
    global count_turns_left
    global count_turns_right
    ev3.speaker.beep()
    print("Entrou no go_to_school")
    while (saw_red_left() or saw_red_right()) : 
        move_forward(150)
    print("Saiu do vermelho")
    count_turns_left = 0
    count_turns_right = 0
    ev3.speaker.beep(0)
    cont = 0
    print("Zerou o contador")
    ev3.speaker.beep()
    while cont < 2 :
        follow_line() 
        if (saw_red_left() or saw_red_right()) and (count_turns_left > 2 or count_turns_right > 2) : 
            cont += 1 
            print("Viu vermelho")
            move_forward_cm(10) 
            count_turns_left = 0
            count_turns_right = 0
            if (saw_red_right() and cont != 2 ): 
                move_forward_cm(7.5)
    print("Chegou na escola")
    ev3.speaker.beep()
    stop() 
    turn_90_right() 
    move_forward_cm(10) 
    open_claw()
    move_backward_cm(10)
    turn_90_right()
    
    while (saw_red_left() or saw_red_right()) :
        move_forward(180)

    cont = 0

    while cont < 2 :
        follow_line() 
        if (saw_red_left() or saw_red_right()) and (count_turns_left > 2 or count_turns_right > 2) : 
            cont += 1 
            print("Viu vermelho")
            move_forward_cm(10) 
            count_turns_left = 0
            count_turns_right = 0
            if (saw_red_left() and cont != 2 ): 
                move_forward_cm(7.5)

    move_forward_cm(3.5) 
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