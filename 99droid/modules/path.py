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
    move_forward(150)
    if (saw_black_left() and saw_black_right()) :
        pass
    elif saw_black_left() :
        turn_left(15)
        count_turns_left += 1
    elif saw_black_right() :
        turn_right(15)
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
            move_forward_cm(10)
            count += 1
            if (count != 3 and saw_red_right()) : 
                while (saw_red_left() or saw_red_right()) : 
                    move_forward_cm(1)
        else:
            follow_line()
    turn_90_right()

def pick_passenger() : 
    global passenger_size
    global time_forward
    found_nothing = False
    if total_of_passengers > 1 :
        turn_90_right()
    stopwatch.reset()
    while not saw_blue_left() and not saw_blue_right() :
        move_forward(100)
    stop()
    time_forward = stopwatch.time()
    move_forward_cm(1.75)
    turn_90_left()
    stopwatch.reset() 
    while (color_front_sensor.reflection() < 1 ): 
        # print(color_front_sensor.reflection())
        move_right(40)
        if stopwatch.time() > 4500:
            found_nothing = True
            break 
    time_spin = stopwatch.time()
    if found_nothing :
        stopwatch.reset() 
        while (stopwatch.time() < time_spin) : 
            move_left(50)
        move_forward_cm(7)
        stopwatch.reset()
        while (color_front_sensor.reflection() < 1 ): 
            # print(color_front_sensor.reflection())
            move_right(40)
        time_spin = stopwatch.time()
    turn_right(5)
    stop() 
    
    move_forward_cm(9) 
    if (color_over_sensor.reflection() > 0) : 
        passenger_size = 15
        print("É O JÚLIO!")
        ev3.speaker.beep(200)
    else :
        passenger_size = 10
        print("É A JESS!")
        ev3.speaker.beep(100)
    stop() 
    close_claw()
    move_backward_cm(9) 
    stop()
    turn_left(5)
    stopwatch.reset() 
    while (stopwatch.time() < time_spin) : 
        move_left(40)
    turn_90_right()
    move_backward_cm(1.75) 
    stopwatch.reset()
    print(time_forward)
    while not saw_red_left() and not saw_red_right() :
        print(stopwatch.time())
        move_backward(100) 
        if time_forward <= stopwatch.time() :
            break
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
    print('count_turns_left: ' + str(count_turns_left) + ' count_turns_right: ' + str(count_turns_right))
    while not saw_red_left() and not saw_red_right() or (count_turns_left < 4 and count_turns_right < 4) : 
        follow_line()
    stop() 
    turn_90_left_and_move_distance(100)
    move_forward_cm(18) #andando
    open_claw() 
    move_backward_cm(18) #andando
    turn_90_left() 
    while (saw_red_left() or saw_red_right() ): 
        move_forward(150)
    count_turns_left = 0
    count_turns_right = 0
    while not saw_red_left() and not saw_red_right() or (count_turns_left < 4 and count_turns_right < 4) : 
        follow_line() 
    move_forward_cm(10)
    
def go_to_lanchonete() : 
    global count_turns_left
    global count_turns_right
    while (saw_red_left() or saw_red_right()) :
        move_forward(150) 

    count_turns_left = 0
    count_turns_right = 0

    print('count_turns_left: ' + str(count_turns_left) + ' count_turns_right: ' + str(count_turns_right))
    while not saw_red_left() and not saw_red_right() or (count_turns_left < 4 and count_turns_right < 4) :
        follow_line() 

    stop() 
    move_forward_cm(10) 
    turn_90_right() 
    move_forward_cm(18) #andando
    open_claw()
    move_backward_cm(18) #andando
    turn_90_right()
    while(saw_red_left() or saw_red_right()): 
        move_forward(150)
    count_turns_left = 0
    count_turns_right = 0
    while not saw_red_left() and not saw_red_right() or (count_turns_left < 4 and count_turns_right < 4) :
        follow_line() 
    move_forward_cm(10) 
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
    print('count_turns_left: ' + str(count_turns_left) + ' count_turns_right: ' + str(count_turns_right))
    while cont < 2 :
        follow_line() 
        if (saw_red_left() or saw_red_right()) and (count_turns_left > 4 or count_turns_right > 4) : 
            cont += 1 
            print("Viu vermelho")
            move_forward_cm(10) 
            count_turns_left = 0
            count_turns_right = 0
    print("Chegou na escola")
    ev3.speaker.beep()
    stop() 
    turn_90_right() 
    move_forward_cm(18) #andando
    open_claw()
    move_backward_cm(18) #andando
    turn_90_right()
    
    while (saw_red_left() or saw_red_right()) :
        move_forward(180)

    cont = 0

    while cont < 2 :
        follow_line() 
        if (saw_red_left() or saw_red_right()) and (count_turns_left > 4 or count_turns_right > 4) : 
            cont += 1 
            print("Viu vermelho")
            move_forward_cm(10) 
            count_turns_left = 0
            count_turns_right = 0
            if (saw_red_left() and cont != 2 ): 
                move_forward_cm(7.5)
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
            if total_of_passengers_of_15cm % 3 == 1 :
                print("Partiu levar Júlio na Lanchonete")
                go_to_lanchonete()
                total_of_passengers_of_15cm += 1
            elif total_of_passengers_of_15cm % 3 == 2 :
                print("Partiu levar Júlio na Escola")
                go_to_school()
                total_of_passengers_of_15cm += 1
            elif total_of_passengers_of_15cm % 3 == 0 :
                print("Partiu levar Júlio no Cinema")
                go_to_cinema()
                total_of_passengers_of_15cm += 1
        else :
            if total_of_passengers_of_10cm % 3 == 1 :
                print("Partiu levar Jess no Cinema")
                go_to_cinema()
                total_of_passengers_of_10cm += 1
            elif total_of_passengers_of_10cm % 3 == 2 :
                print("Partiu levar Jess na Escola")
                go_to_school()
                total_of_passengers_of_10cm += 1
            elif total_of_passengers_of_10cm % 3 == 0 :
                print("Partiu levar Jess na Lanchonete")
                go_to_lanchonete()
                total_of_passengers_of_10cm += 1
        total_of_passengers += 1

#-------------------------------------------------------------------------------------------------------