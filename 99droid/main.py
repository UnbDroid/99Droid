#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (InfraredSensor, UltrasonicSensor)
from pybricks.parameters import Stop, Direction, Button
from pybricks.tools import wait, StopWatch, DataLog
#from pybricks.media.ev3dev import SoundFile, ImageFile

from modules.motors import *
from modules.colors import *
from modules.detect import *
from modules.path import *

#Declaração de variáveis globais e objetos

count = 0 #Declaração da variável que conta o número de blocos vermelhos que o robô leu
passenger_size = 0 #Declaração da variável que armazena o tamanho do passageiro
total_of_passengers = 1 #Declaração da variável que conta o número de passageiros que o robô pegou
total_of_passengers_of_10cm = 1 #Declaração da variável que conta o número de passageiros de 10 cm de altura que o robô pegou
total_of_passengers_of_15cm = 1 #Declaração da variável que conta o número de passageiros de 15 cm de altura que o robô pegou

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)

go_to_passengers() #O robô vai até a área de captura dos passageiros
while total_of_passengers <= 5 : #O robô leva os 5 passageiros
    pick_passenger()
    drop_passenger()