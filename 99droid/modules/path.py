from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import StopWatch

from modules.motors import *
from modules.colors import *
from modules.detect import *


def follow_line() :
    global count 
    #calibration(sensor_color) 
    move_forward(140)
    if saw_black_left() and saw_black_right() : #Se os dois sensores de cor estiverem em cima da linha preta
        pass
    elif saw_black_left() : #Se o sensor de cor esquerdo estiver em cima da linha preta
        #O robô vira para a esquerda em aproximadamente 90 graus
        turn_90_left_and_move_distance(50)
    elif saw_black_right() :
        #O robô vira para a direita em aproximadamente 90 graus
        turn_90_right_and_move_distance(50)
        
#-------------------------------------------------------------------------------------------------------
    
#Funções referentes ao trajeto do robô

def go_to_passengers() :
    global count #Chama a variável global count, responsável por armazenar o número de vezes que o robô leu o bloco de cor vermelha
    count = 0
    while not saw_red_left() and saw_red_right() : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho
        follow_line() #O robô segue a linha
    count += 1 #O count é incrementado ao encontrar o bloco vermelho
    print("count + 1") #Imprime que o count foi incrementado em 1
    turn_90_left_and_move_distance(100) #O robô vira para a esquerda em aproximadamente 90 graus
    if saw_red_left or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward_cm(10) #O robô sai do vermelho
    while count < 3 : #Enquanto o count for menor que 3, ou seja, o robô não leu o bloco vermelho 3 vezes
        if saw_red_right() : #Se o sensor de cor direito estiver em cima do bloco vermelho
            move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
            count += 1 #O count é incrementado em 1
            #Para caso o robô não esteja nos blocos vermelhos afrente da área de captura dos passageiros
            if count != 3 and saw_red_right() : #Se o count for diferente de 3 e o sensor de cor direito estiver em cima do bloco vermelho
                while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
                    move_forward_cm(1) #O robô anda para frente até os sensores saírem do bloco vermelho	
        follow_line() #O robô segue a linha

def distance_front() : #Função que retorna a distância do sensor de distância frontal em cm
    return ultrasonic_front_sensor.distance()/10 #Retorna a distância do sensor de distância frontal em cm

def pick_passenger() : #Função que captura o passageiro
    #Vai funcionar como um radar, o robô vai girar para a direita até encontrar o passageiro com o sensor de cor apontado para frente
    stopwatch.reset() #O cronômetro é resetado
    while color_front_sensor.reflection() < 1 : #Enquanto o sensor de cor frontal não estiver apontado pro passageiro
        print(color_front_sensor.reflection()) #Imprime o valor RGB do sensor de cor frontal4
        move_right(30) #O robô gira para a direita
    time_spin = stopwatch.time() #O cronômetro é parado e o tempo levado para girar até o passageiro é armazenado na variável time_spin
    stop() #O robô para
    move_forward_cm(10) #O robô anda para frente até ficar de frente para o passageiro
    stop() #O robô para
    if distance_front() < 10 : #Se o sensor de cima detectar algo a menos de 10 cm
        passenger_size = 15 #O tamanho do passageiro é 15 cm
    else :
        passenger_size = 10 #Se não, o tamanho do passageiro é 10 cm
    fechaGarra() #A garra fecha e captura o passageiro
    move_backward_cm(10) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    stop() #O robô para
    stopwatch.reset() #O cronômetro é resetado
    while stopwatch.time() < time_spin : #Enquanto o tempo do cronômetro for menor que o tempo armazenado na variável time_spin
        move_left(30) #O robô gira para a esquerda, voltando para a linha preta
        
def go_to_cinema() : #Função que leva o passageiro até o cinema
    turn180()
    while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward(140)
    while not saw_red_left() and saw_red_right() : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho do cinema
        follow_line() #O robô segue a linha
    #Ao chegar no bloco vermelho na frente do cinema...
    stop() #O robô para
    turn_90_left_and_move_distance(100)
    move_forward_cm(10) #O robô anda para frente até entrar no cinema
    abreGarra() #A garra abre e solta o passageiro
    move_forward_cm(-00) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    turn_90_left() #O robô gira para a esquerda em 90 graus
    while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward(150) #O robô anda para frente
    while not saw_red_left() and saw_red_right() : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho da área de captura dos passageiros
        follow_line() #O robô segue a linha
    move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    
def go_to_lanchonete() : #Função que leva o passageiro até a lanchonete
    while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward(150) #O robô anda para frente
    while not saw_red_left() and saw_red_right() : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho da lanchonete
        follow_line() #O robô segue a linha
    #Ao chegar no bloco vermelho na frente da lanchonete...
    stop() #O robô para
    move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    turn_90_right() #O robô gira para a direita em 90 graus
    move_forward_cm(10) #O robô anda para frente até entrar na lanchonete
    abreGarra() #A garra abre e solta o passageiro
    move_backward_cm(10) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    turn_90_right() #O robô gira para a direita em 90 graus
    while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward(150) #O robô anda para frente
    while not saw_red_left() and saw_red_right() : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho da área de captura dos passageiros
        follow_line() #O robô segue a linha
    move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    turn180() #O robô gira para a direita em 180 graus
    
def go_to_escola() : #Função que leva o passageiro até a escola
    while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward(150) #O robô anda para frente
    for cont in range(3) : #Para o count de 0 até 3, lendo o número de vezes que o robô passou por cima do bloco vermelho 
        follow_line() #O robô segue a linha
        if saw_red_left() or saw_red_right() : #Se um dos dois sensores de cor estiverem em cima do bloco vermelho
            cont += 1 #O count aumenta em 1
            move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
            if saw_red_right() and cont != 3 : #Se o sensor de cor direito estiver em cima do bloco vermelho e o count for diferente de 3
                move_forward_cm(5) #O robô anda para frente até sair do bloco vermelho
    #Ao chegar no bloco vermelho na frente da escola...
    stop() #O robô para
    move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    turn_90_right() #O robô gira para a direita em 90 graus
    move_forward_cm(10) #O robô anda para frente até entrar na escola
    abreGarra() #A garra abre e solta o passageiro
    move_backward_cm(10) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    turn_90_right() #O robô gira para a direita em 90 graus
    while saw_red_left() or saw_red_right() : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        move_forward(180) #O robô anda para frente
    #Mesma coisa do for cont de cima, mas pra voltar pra área de captura dos passageiros
    for cont in range(3) : 
        follow_line()
        if saw_red_left() or saw_red_right() :
            cont += 1
            move_forward_cm(10)
            if saw_red_right() and cont != 3 :
                move_forward_cm(5)
    move_forward_cm(10) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    turn180() #O robô gira para a direita em 180 graus
    
def drop_passenger() : #Função que leva o passageiro até o seu destino dependendo do tamanho dele e do número de passageiros de cada tamanho que já foram levados
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
                go_to_escola()
        else :
            if total_of_passengers_of_10cm == 1 :
                go_to_cinema()
            elif total_of_passengers_of_10cm == 2 :
                go_to_escola()
        total_of_passengers += 1
    elif total_of_passengers >= 3 :
        if passenger_size == 15 :
            if total_of_passengers_of_15cm == 1 :
                go_to_lanchonete()
            elif total_of_passengers_of_15cm == 2 :
                go_to_escola()
            elif total_of_passengers_of_15cm == 3 :
                go_to_cinema()
        else :
            if total_of_passengers_of_10cm == 1 :
                go_to_cinema()
            elif total_of_passengers_of_10cm == 2 :
                go_to_escola()
            elif total_of_passengers_of_10cm == 3 :
                go_to_lanchonete()
        total_of_passengers += 1

#-------------------------------------------------------------------------------------------------------