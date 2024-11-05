################################
# robot_19991.py
################################

# Import the necessary libraries
import sys
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait, StopWatch
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font

# Define all constants here
STRAIGHT_SPEED = 400
STRAIGHT_ACCELERATION = 100
WHEEL_DIAMETER=97
AXLE_TRACK_MM=111.4
TURN_RATE=200
TURN_ACCELERATION=75
MIN_DRIVE_SPEED = 60
#DRIVE_ACCELERATION = 0.5
DRIVE_ACCELERATION = 1
MIN_TANK_TURN_SPEED = 30
WHEEL_RADIUS = WHEEL_DIAMETER/2
AXLE_TRACK_CM = AXLE_TRACK_MM/10
GYRO_GAIN = 3
GYRO_PD = 6 #4 is also a good value
GYRO_MOUNT = "up" # or "down"

################################
# Define custom_robot Class
################################
class robot_19991:

    def __init__(self):
        
        '''
        This is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''

        # Initialize the brick, motors, sensors
        # Use "try" so there can be an exception if there is an initialization error
        try:
            self.ev3 = EV3Brick()
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"EV3 FAIL")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_attachment_motor = Motor(Port.A)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT A")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_attachment_motor = Motor(Port.D)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT D")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_drive_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT B")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_drive_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT C")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        ''' 
        try:
            self.left_color_sensor = ColorSensor(Port.S1)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 1")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.middle_color_sensor = ColorSensor(Port.S2)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 2")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_color_sensor = ColorSensor(Port.S3)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 3")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        '''
        try:
            self.gyro_sensor = GyroSensor(Port.S4)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 4")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK_MM)
            self.robot.settings(straight_speed=STRAIGHT_SPEED, straight_acceleration=STRAIGHT_ACCELERATION, turn_rate=TURN_RATE, turn_acceleration=TURN_ACCELERATION)
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.GREEN)
            self.watch = StopWatch()
            self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
            self.ev3.screen.set_font(Font(size=30, bold=True))
            wait(1000)
            self.ev3.screen.clear()    
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"NOT WIRING")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            #self.ev3.speaker.say("startup error, check wiring")
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()

        # This sets the minimum drive speed to prevent stalling
        self.min_drive_speed = 60.

        # This sets how quickly the robot speeds up and slows down
        # unit(s) of speed (mm/s) per 1 unit of distance (mm)
        self.drive_acceleration = DRIVE_ACCELERATION

        # This sets the minimum tank turn speed to prevent stalling
        self.min_tank_turn_speed = 30.

        # This is the radius of the wheels in cms
        # This is so we can convert distance to wheel rotation(s) or the 
        # other way around
        self.wheel_radius = WHEEL_RADIUS/10

        # half of the distace between the wheels(in cms, obvously)
        # We need this in order to convert from degrees we want to spin the bot
        # to how far those wheels have to move.
        self.axle_track = AXLE_TRACK_CM

        # this is the gain we use when going straight with the gyro sensor
        self.gyro_gain = GYRO_GAIN

################################
# Define functions 
################################
    
    # Reset The Gyro
    def calibrate_gyro(self, port_number):
        retry = 1
        while retry == 1:
            print("calibrating the Gyro")
            self.ev3.screen.draw_text(0, 0, "Reset Gyro")
            self.ev3.screen.draw_text(0, 22, "DO NOT MOVE!")
            if port_number == 1:
                analog_sensor = AnalogSensor(Port.S1)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S1)
                wait(1000)
            elif port_number == 2:
                analog_sensor = AnalogSensor(Port.S2)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S2)
                wait(1000)
            elif port_number == 3:
                analog_sensor = AnalogSensor(Port.S3)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S3)
                wait(1000)
            else:
                analog_sensor = AnalogSensor(Port.S4)
                wait(1000)
                gyro_sensor = GyroSensor(Port.S4)
                wait(1000)
            i = 0
            while i <= 10:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(0, 0, "RESET GYRO")
                self.ev3.screen.draw_text(0, 22, "DO NOT MOVE!")
                self.ev3.screen.draw_text(0, 44, "Gyro= " + str(gyro_sensor.angle()))
                wait(100)
                self.ev3.screen.clear()
                i = i + 1
            if gyro_sensor.angle() == 0:
                retry = 0
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(0, 44, "Gyro")
                self.ev3.screen.draw_text(0, 44, "Calibration")
                self.ev3.screen.draw_text(0, 84, "Complete")
                wait(500)
                self.ev3.screen.clear()
    
    # gyro tank turn
    def gyro_tank_turn(self,speed, angle):
        ''' Tank turn using the gyro
            angle positive = clockwise
            angle negative = counter-clockwise
        '''
        self.gyro_sensor.reset_angle(angle=0)
        min_speed = 50
        #Get the current angle
        starting_angle = 0
        target_angle = angle
        # The gyro is mounted upside-down which reverses the gyro measurements 
        if GYRO_MOUNT == "down":
            if angle >= 0:
            #clockwise
                while self.gyro_sensor.angle() >= target_angle:
                    # Ramp the speed based on the perecntage of the turn completed.
                    scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                    unbound_speed = speed * (1 - scale)
                    current_speed = max(unbound_speed, self.min_tank_turn_speed)
                    self.left_drive_motor.run(current_speed)
                    self.right_drive_motor.run(-current_speed)
                    print("gt %s" % self.gyro_sensor.angle())
            else:
            #counter-clockwise
                while self.gyro_sensor.angle() <= target_angle:
                    # Ramp the speed based on the perecntage of the turn completed.
                    scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                    unbound_speed = speed * (1 - scale)
                    current_speed = max(unbound_speed, self.min_tank_turn_speed)
                    self.left_drive_motor.run(-current_speed)
                    self.right_drive_motor.run(current_speed)
                    print("lt %s" % self.gyro_sensor.angle())
        else:
            if angle <= 0:
            #counter-clockwise
                while self.gyro_sensor.angle() > target_angle:
                    # Ramp the speed based on the perecntage of the turn completed.
                    scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                    unbound_speed = speed * (1 - scale)
                    current_speed = max(unbound_speed, self.min_tank_turn_speed)
                    self.left_drive_motor.run(-current_speed)
                    self.right_drive_motor.run(current_speed)
                    print("gt %s" % self.gyro_sensor.angle())
            else:
            #clockwise
                while self.gyro_sensor.angle() < target_angle:
                    # Ramp the speed based on the perecntage of the turn completed.
                    scale = abs((self.gyro_sensor.angle() - starting_angle) / (target_angle - starting_angle))
                    unbound_speed = speed * (1 - scale)
                    current_speed = max(unbound_speed, self.min_tank_turn_speed)
                    self.left_drive_motor.run(current_speed)
                    self.right_drive_motor.run(-current_speed)
                    print("lt %s" % self.gyro_sensor.angle())

        self.left_drive_motor.brake()
        self.right_drive_motor.brake()    

    # gyro drive straight
    def gyro_drive_straight_distance_pd(self,speed, distance, pd):
        ''' Drive straight using the gyro.
            Use a proportional feedback loop.
        '''
        # Reset the distance to 0.
        self.robot.reset()
        self.gyro_sensor.reset_angle(0)

        # Define the feedback loop gain value, "pd."  This determines how much the robot
        # will correct when it drives off course.  
        # This value may need to be adjusted.  Here are some tips:
        # 1) If the value is too large, the robot will over-correct for errors and snake back and forth.  
        # 2) If the value is too small, the robot will not correct enough and will go off course.
        # 3) If the robot spins in circles, try making this value negative (pd=-1)
        #pd = GYRO_PD

        # Get the current gyro angle.  This is the direction the robot should keep driving. 
        starting_angle = self.gyro_sensor.angle()
        # Create a while loop so the robot will drive until it reaches the target distance.  Inside the loop
        # the robot's current direction, "self.gyro_sensor.angle()" is repeatedly checked to see if it has gone off course. 
        # If needed, a course correction is made to turn back to the desired direction (starting_angle)
        while abs(self.robot.distance()) <= distance:
            # Calculate the error (the difference) between where the robot should be pointed and where it is pointed
            # Where the robot should be pointed:     starting_angle
            # Where the robot is currently pointed:  self.gyro_sensor.angle()
            direction_error = starting_angle - self.gyro_sensor.angle()
            print(self.gyro_sensor.angle())

            # Use the feedback loop gain value, "pd" multiplied by the, "direction_error" to make the robot turn back
            # on course.
            turn = direction_error * pd

            # The robot should drive with the speed passed into this method, "gyro_drive_straight" and turn based on
            # the correction needed to keep going straight.
            self.robot.drive(speed,turn)
        self.robot.stop()
        self.left_drive_motor.brake()
        self.right_drive_motor.brake()

        # gyro drive straight
    def gyro_drive_straight_distance(self,speed, distance):
        ''' Drive straight using the gyro.
            Use a proportional feedback loop.
        '''
        # Reset the distance to 0.
        self.robot.reset()

        # Define the feedback loop gain value, "pd."  This determines how much the robot
        # will correct when it drives off course.  
        # This value may need to be adjusted.  Here are some tips:
        # 1) If the value is too large, the robot will over-correct for errors and snake back and forth.  
        # 2) If the value is too small, the robot will not correct enough and will go off course.
        # 3) If the robot spins in circles, try making this value negative (pd=-1)
        pd = GYRO_PD

        # Get the current gyro angle.  This is the direction the robot should keep driving. 
        starting_angle = self.gyro_sensor.angle()
       
        # Create a while loop so the robot will drive until it reaches the target distance.  Inside the loop
        # the robot's current direction, "self.gyro_sensor.angle()" is repeatedly checked to see if it has gone off course. 
        # If needed, a course correction is made to turn back to the desired direction (starting_angle)
        # while self.robot.distance() <= distance:
        if distance < 0:
            while self.robot.distance() > distance:
                reverse_speed = -1*speed
                # Calculate the error (the difference) between where the robot should be pointed and where it is pointed
                # Where the robot should be pointed:     starting_angle
                # Where the robot is currently pointed:  self.gyro_sensor.angle()
                direction_error = starting_angle - self.gyro_sensor.angle()

                # Use the feedback loop gain value, "pd" multiplied by the, "direction_error" to make the robot turn back
                # on course.
                turn = direction_error * pd

                # The robot should drive with the speed passed into this method, "gyro_drive_straight" and turn based on
                # the correction needed to keep going straight.
                self.robot.drive(reverse_speed,turn)
        else:
            while self.robot.distance() < distance:
                # Calculate the error (the difference) between where the robot should be pointed and where it is pointed
                # Where the robot should be pointed:     starting_angle
                # Where the robot is currently pointed:  self.gyro_sensor.angle()
                direction_error = starting_angle - self.gyro_sensor.angle()

                # Use the feedback loop gain value, "pd" multiplied by the, "direction_error" to make the robot turn back
                # on course.
                turn = direction_error * pd

                # The robot should drive with the speed passed into this method, "gyro_drive_straight" and turn based on
                # the correction needed to keep going straight.
                self.robot.drive(speed,turn)
        self.robot.stop()
        self.left_drive_motor.brake()
        self.right_drive_motor.brake()

    # gyro drive straight
    def gyro_drive_straight_time(self,speed, time):
        ''' Drive straight using the gyro.
            Use a proportional feedback loop.
        '''
        # Reset the time to 0.
        watch = StopWatch()
        watch.reset()

        # Define the feedback loop gain value, "pd."  This determines how much the robot
        # will correct when it drives off course.  
        # This value may need to be adjusted.  Here are some tips:
        # 1) If the value is too large, the robot will over-correct for errors and snake back and forth.  
        # 2) If the value is too small, the robot will not correct enough and will go off course.
        # 3) If the robot spins in circles, try making this value negative (pd=-1)
        pd = GYRO_PD

        # Get the current gyro angle.  This is the direction the robot should keep driving. 
        starting_angle = self.gyro_sensor.angle()
       
        # Create a while loop so the robot will drive until it reaches the target distance.  Inside the loop
        # the robot's current direction, "self.gyro_sensor.angle()" is repeatedly checked to see if it has gone off course. 
        # If needed, a course correction is made to turn back to the desired direction (starting_angle)
        while watch.time() <= time:
            # Calculate the error (the difference) between where the robot should be pointed and where it is pointed
            # Where the robot should be pointed:     starting_angle
            # Where the robot is currently pointed:  self.gyro_sensor.angle()
            direction_error = starting_angle - self.gyro_sensor.angle()

            # Use the feedback loop gain value, "pd" multiplied by the, "direction_error" to make the robot turn back
            # on course.
            turn = direction_error * pd

            # The robot should drive with the speed passed into this method, "gyro_drive_straight" and turn based on
            # the correction needed to keep going straight.
            self.robot.drive(speed,turn) 
        self.robot.stop()
        self.left_drive_motor.brake()
        self.right_drive_motor.brake()

