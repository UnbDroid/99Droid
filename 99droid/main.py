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
from modules.claw import *

#Declaração de variáveis globais e objetos

#----------------------------------------------------------------------------------------------------------------------------------

#Programa principal (minúsuclo pq é o programa principal lmfao)
#close_claw()
motors.settings(150, 300, 100, 1000)
go_to_passengers()
while total_of_passengers < 4 :
    pick_passenger()
    drop_passenger()
    # time_open_claw += 500
# print(sensor_color_right.rgb())
# close_claw()
# open_claw()
# while True :
#    print(sensor_color_right.rgb())

#while True:
 #   print(distance_front())
  #  if (distance_front() > 200) : 
   #     passenger_size = 15
    #    print("É O JÚLIO!")
    #else :
     #   passenger_size = 10
      #  print("É A JESS!")
    #wait(5000)

# finish()