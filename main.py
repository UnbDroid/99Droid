#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Declaração de variáveis globais e objetos
motorL = Motor(Port.A) #Declaração do motor esquerdo
motorR = Motor(Port.B) #Declaração do motor direito
motorGarra = Motor(Port.D) #Declaração do motor da garra
sensorCorL = ColorSensor(Port.S1) #Declaração do sensor de cor esquerdo
sensorCorR = ColorSensor(Port.S2) #Declaração do sensor de cor direito
tempoAbrirGarra = 0 #Declaração da variável que armazena o tempo que a garra leva para abrir
crono = StopWatch() #Declaração do cronômetro
sonarFrente = UltrasonicSensor(Port.S3) #Declaração do sensor ultrassônico de cima
corFrente = ColorSensor(Port.S4) #Declaração do sensor de cor apontado para frente
robo = DriveBase(motorL, motorR, wheel_diameter = 42.1, axle_track = 111.2) #Declaração do robô
contador = 0 #Declaração da variável que conta o número de blocos vermelhos que o robô leu
tamanhoPassageiro = 0 #Declaração da variável que armazena o tamanho do passageiro
nPassageiros = 1 #Declaração da variável que conta o número de passageiros que o robô pegou
nPassageiros10 = 1 #Declaração da variável que conta o número de passageiros de 10 cm de altura que o robô pegou
nPassageiros15 = 1 #Declaração da variável que conta o número de passageiros de 15 cm de altura que o robô pegou

#-------------------------------------------------------------------------------------------------------

#Declaração dos valores RGB dos sensores de cor

def redLeft() :
    return sensorCorL.rgb()[0]
def greenLeft() :
    return sensorCorL.rgb()[1]
def blueLeft() :
    return sensorCorL.rgb()[2]
def redRight() :
    return sensorCorR.rgb()[0]
def greenRight() :
    return sensorCorR.rgb()[1]
def blueRight() :
    return sensorCorR.rgb()[2]

#-------------------------------------------------------------------------------------------------------

#Núcleo do seguidor de linha

def seguirLinha() :
    global contador #Chama a variável global contador
    print(sensorCorR.rgb()) #Imprime os valores RGB do sensor de cor direito
    robo.drive(140,0) #Define a velocidade do robô
    if redLeft() < 18 and greenLeft() < 18 and blueLeft() < 18 and redRight() < 18 and greenRight() < 18 and blueRight() < 18 : #Se os dois sensores de cor estiverem em cima da linha preta
        pass
    elif redLeft() < 18 and greenLeft() < 18 and blueLeft() < 18 : #Se o sensor de cor esquerdo estiver em cima da linha preta
        #O robô vira para a esquerda em aproximadamente 90 graus
        robo.straight(50) #O robô anda para frente até ficar com o meio do robô em cima da linha preta
        robo.turn(-90) #O robô vira para a esquerda em aproximadamente 90 graus
        robo.stop() #O robô para
        #Acabou o ajuste
    elif redRight() < 18 and greenRight() < 18 and blueRight() < 18 :
        robo.straight(50) #O robô anda para frente até ficar com o meio do robô em cima da linha preta
        robo.turn(90) #O robô vira para a direita em aproximadamente 90 graus
        robo.stop() #O robô para
        #Acabou o ajuste
        
#-------------------------------------------------------------------------------------------------------
    
#Funções referentes ao trajeto do robô

def irAteAreaDeCaptura() :
    global contador #Chama a variável global contador, responsável por armazenar o número de vezes que o robô leu o bloco de cor vermelha
    contador = 0
    while redLeft() < (greenLeft() + blueLeft()) and redRight() < (greenRight() + blueRight()) : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho
        seguirLinha() #O robô segue a linha
    contador += 1 #O contador é incrementado ao encontrar o bloco vermelho
    print("contador + 1") #Imprime que o contador foi incrementado em 1
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da cruz preta
    robo.turn(-90) #O robô vira para a esquerda em aproximadamente 90 graus
    robo.stop() #O robô para
    #Acabou o ajuste
    if redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.straight(100) #O robô sai do vermelho
    while contador < 3 : #Enquanto o contador for menor que 3, ou seja, o robô não leu o bloco vermelho 3 vezes
        if redRight() > (greenRight() + blueRight()) : #Se o sensor de cor direito estiver em cima do bloco vermelho
            robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
            contador += 1 #O contador é incrementado em 1
            #Para caso o robô não esteja nos blocos vermelhos afrente da área de captura dos passageiros
            if contador != 3 and redRight() > (greenRight() + blueRight()) : #Se o contador for diferente de 3 e o sensor de cor direito estiver em cima do bloco vermelho
                while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
                    robo.straight(10) #O robô anda para frente até os sensores saírem do bloco vermelho	
        seguirLinha() #O robô segue a linha
def distFrente() : #Função que retorna a distância do sensor de distância frontal em cm
    return sonarFrente.distance()/10 #Retorna a distância do sensor de distância frontal em cm

def fechaGarra() : #Função que fecha a garra :)
    global tempoAbrirGarra #Chama a variável global tempoAbrirGarra, responsável por armazenar o tempo levado para fechar a garra
    crono.reset() #O cronômetro é resetado
    motorGarra.run_target(-200, -90, then=Stop.HOLD, wait=False) #O motor da garra gira para fechar até travar
    tempoAbrirGarra = crono.time() #O cronômetro é parado e o tempo levado para fechar a garra é armazenado na variável tempoAbrirGarra
    motorGarra.hold() #O motor da garra é travado para não girar mais
    
def abreGarra() : #Função que abre a garra :)
    global tempoAbrirGarra #Chama a variável global tempoAbrirGarra, responsável por armazenar o tempo levado para abrir a garra
    crono.reset() #O cronômetro é resetado
    while crono.time() < tempoAbrirGarra : #Enquanto o tempo do cronômetro for menor que o tempo armazenado na variável tempoAbrirGarra
        motorGarra.run(200) #O motor da garra gira para abrir
    motorGarra.hold() #O motor da garra é travado para não girar mais
    
def capturaPassageiro() : #Função que captura o passageiro
    #Vai funcionar como um radar, o robô vai girar para a direita até encontrar o passageiro com o sensor de cor apontado para frente
    crono.reset() #O cronômetro é resetado
    while corFrente.reflection() < 1 : #Enquanto o sensor de cor frontal não estiver apontado pro passageiro
        print(corFrente.reflection()) #Imprime o valor RGB do sensor de cor frontal4
        robo.drive(0,30) #O robô gira para a direita
    timerRodar = crono.time() #O cronômetro é parado e o tempo levado para girar até o passageiro é armazenado na variável timerRodar
    robo.stop() #O robô para
    robo.straight(100) #O robô anda para frente até ficar de frente para o passageiro
    robo.stop() #O robô para
    if distFrente() < 10 : #Se o sensor de cima detectar algo a menos de 10 cm
        tamanhoPassageiro = 15 #O tamanho do passageiro é 15 cm
    else :
        tamanhoPassageiro = 10 #Se não, o tamanho do passageiro é 10 cm
    fechaGarra() #A garra fecha e captura o passageiro
    robo.straight(-100) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    robo.stop() #O robô para
    crono.reset() #O cronômetro é resetado
    while crono.time() < timerRodar : #Enquanto o tempo do cronômetro for menor que o tempo armazenado na variável timerRodar
        robo.drive(0,-30) #O robô gira para a esquerda, voltando para a linha preta
        
def levarAteCinema() : #Função que leva o passageiro até o cinema
    robo.turn(180) #O robô gira para a esquerda em 180 graus
    while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.drive(150,0) #O robô anda para frente
    while redLeft() < (greenLeft() + blueLeft()) and redRight() < (greenRight() + blueRight()) : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho do cinema
        seguirLinha() #O robô segue a linha
    #Ao chegar no bloco vermelho na frente do cinema...
    robo.stop() #O robô para
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    robo.turn(-90) #O robô gira para a esquerda em 90 graus
    robo.straight(100) #O robô anda para frente até entrar no cinema
    abreGarra() #A garra abre e solta o passageiro
    robo.straight(-100) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    robo.turn(-90) #O robô gira para a esquerda em 90 graus
    while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.drive(150,0) #O robô anda para frente
    while redLeft() < (greenLeft() + blueLeft()) and redRight() < (greenRight() + blueRight()) : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho da área de captura dos passageiros
        seguirLinha() #O robô segue a linha
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    
def levarAteLanchonete() : #Função que leva o passageiro até a lanchonete
    while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.drive(150,0) #O robô anda para frente
    while redLeft() < (greenLeft() + blueLeft()) and redRight() < (greenRight() + blueRight()) : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho da lanchonete
        seguirLinha() #O robô segue a linha
    #Ao chegar no bloco vermelho na frente da lanchonete...
    robo.stop() #O robô para
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    robo.turn(90) #O robô gira para a direita em 90 graus
    robo.straight(100) #O robô anda para frente até entrar na lanchonete
    abreGarra() #A garra abre e solta o passageiro
    robo.straight(-100) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    robo.turn(90) #O robô gira para a direita em 90 graus
    while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.drive(150,0) #O robô anda para frente
    while redLeft() < (greenLeft() + blueLeft()) and redRight() < (greenRight() + blueRight()) : #Enquanto os dois sensores de cor não estiverem em cima do bloco vermelho da área de captura dos passageiros
        seguirLinha() #O robô segue a linha
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    robo.turn(180) #O robô gira para a direita em 180 graus
    
def levarAteEscola() : #Função que leva o passageiro até a escola
    while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.drive(150,0) #O robô anda para frente
    for cont in range(3) : #Para o contador de 0 até 3, lendo o número de vezes que o robô passou por cima do bloco vermelho 
        seguirLinha() #O robô segue a linha
        if redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Se um dos dois sensores de cor estiverem em cima do bloco vermelho
            cont += 1 #O contador aumenta em 1
            robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
            if redRight() > (greenRight() + blueRight()) and cont != 3 : #Se o sensor de cor direito estiver em cima do bloco vermelho e o contador for diferente de 3
                robo.straight(50) #O robô anda para frente até sair do bloco vermelho
    #Ao chegar no bloco vermelho na frente da escola...
    robo.stop() #O robô para
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    robo.turn(90) #O robô gira para a direita em 90 graus
    robo.straight(100) #O robô anda para frente até entrar na escola
    abreGarra() #A garra abre e solta o passageiro
    robo.straight(-100) #O robô anda para trás até ficar com o meio do robô em cima da curva preta
    robo.turn(90) #O robô gira para a direita em 90 graus
    while redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) : #Enquanto os dois sensores de cor estiverem em cima do bloco vermelho
        robo.drive(180,0) #O robô anda para frente
    #Mesma coisa do for cont de cima, mas pra voltar pra área de captura dos passageiros
    for cont in range(3) : 
        seguirLinha()
        if redLeft() > (greenLeft() + blueLeft()) or redRight() > (greenRight() + blueRight()) :
            cont += 1
            robo.straight(100)
            if redRight() > (greenRight() + blueRight()) and cont != 3 :
                robo.straight(50)
    robo.straight(100) #O robô anda para frente até ficar com o meio do robô em cima da curva preta
    robo.turn(180) #O robô gira para a direita em 180 graus
    
def levarPassageiro() : #Função que leva o passageiro até o seu destino dependendo do tamanho dele e do número de passageiros de cada tamanho que já foram levados
    global nPassageiros
    global nPassageiros15
    global nPassageiros10
    global tamanhoPassageiro7
    if nPassageiros == 1 :
        if tamanhoPassageiro == 15 :
            levarAteLanchonete()
        else :
            levarAteCinema()
        nPassageiros += 1
    elif nPassageiros == 2 :
        if tamanhoPassageiro == 15 :
            if nPassageiros15 == 1 :
                levarAteLanchonete()
            elif nPassageiros15 == 2 :
                levarAteEscola()
        else :
            if nPassageiros10 == 1 :
                levarAteCinema()
            elif nPassageiros10 == 2 :
                levarAteEscola()
        nPassageiros += 1
    elif nPassageiros >= 3 :
        if tamanhoPassageiro == 15 :
            if nPassageiros15 == 1 :
                levarAteLanchonete()
            elif nPassageiros15 == 2 :
                levarAteEscola()
            elif nPassageiros15 == 3 :
                levarAteCinema()
        else :
            if nPassageiros10 == 1 :
                levarAteCinema()
            elif nPassageiros10 == 2 :
                levarAteEscola()
            elif nPassageiros10 == 3 :
                levarAteLanchonete()
        nPassageiros += 1

#-------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)

irAteAreaDeCaptura() #O robô vai até a área de captura dos passageiros
while nPassageiros <= 5 : #O robô leva os 5 passageiros
    capturaPassageiro()
    levarPassageiro()