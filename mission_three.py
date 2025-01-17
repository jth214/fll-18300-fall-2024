################################
# mission_three.py
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

def mission_three(r):
    print("Running Mission 3")
    # Mission Name
    # Authors
    r.ev3.screen.clear()
    print("Running Mission 3")
    r.ev3.screen.draw_text(30, 60, "Mission 3")
    wait(time=100)
    # Mission Name
    # sebstian.cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    #r.gyro_drive_straight_distance(speed=500,distance=750)
    #r.gyro_tank_turn(speed=500,angle=30)
    #r.gyro_drive_straight_distance(speed=500,distance=750)
    #r.right_attachment_motor.run_time(speed=500, time=5000, then=Stop.HOLD, wait=True)
    r.gyro_drive_straight_distance(speed=150,distance=960)
    r.gyro_drive_straight_distance(speed=150,distance=-75)
    r.gyro_tank_turn(speed=150,angle=135)
    r.gyro_drive_straight_distance(speed=150,distance=-200)
    #r.ev3.screen.draw_text(30, 60, "AHHH")
    r.gyro_tank_turn(speed=500,angle=30)
    r.robot.straight(distance=350)
    #wait(200)
    r.gyro_drive_straight_distance(speed=150,distance=-600)
    r.gyro_drive_straight_distance(speed=150,distance=320)
    r.gyro_drive_straight_distance(speed=150,distance=-600)
    r.gyro_drive_straight_distance(speed=150,distance=320)
    #r.gyro_tank_turn(speed=500,angle=45)
    #r.gyro_drive_straight_distance(speed=500,distance=-100)
    #r.gyro_tank_turn(speed=500,angle=-200)
    #drive home
    #r.gyro_drive_straight_distance(speed=500,distance=300)
    #r.gyro_tank_turn(speed=500,angle=-15)
    #r.gyro_drive_straight_distance(speed=500,distance=300)