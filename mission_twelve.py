################################
# mission_twelve.py
################################

import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_19991 import robot_19991

def mission_twelve(r):  
    print("Running Mission 12")
    # Mission Name 
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 12")
    r.ev3.screen.draw_text(30, 60, "Mission 12")
    wait(time=100)
    