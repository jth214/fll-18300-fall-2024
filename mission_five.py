import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from robot_18300 import robot_18300

def mission_five(r):
    print("Running Mission 5")
    r.ev3.screen.draw_text(30, 60, "Mission 5")
    wait(1000)
    r.ev3.screen.clear()
    r.robot.straight(450)
    r.robot.turn(-45)
    r.robot.straight(252)
    r.robot.turn(90)
    r.robot.straight(257)
    r.robot.straight(-53)
    r.robot.straight(53)
    r.robot.stright(-53)
    r.robot.straight(53)