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

count = 0 
passenger_size = 0 
total_of_passengers = 1
total_of_passengers_of_10cm = 1
total_of_passengers_of_15cm = 1

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)

go_to_passengers()
while total_of_passengers <= 5 :
    pick_passenger()
    drop_passenger()