################################
# mission_two.py
################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_two(r):
    print("Running Mission 2")
    #Lydia and Madeleine
    #Drive to Finn and John
    r.robot.drive(601,0)  
    wait(5000)
    r.robot.stop()