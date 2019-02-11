"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tyler Thenell, Jacob Jarski, Zack Z.
  Winter term, 2018-2019.
"""
import rosebot

class ResponderToGUIMessages(object):
    def __init__(self, robot):
        """

            :type robot: rosebot.RoseBot
        """
        self.robot = robot
        self.stop_program = False

    def go(self, left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        right = int(right_wheel_speed)
        self.robot.drive_system.go(left, right)

    def left(self, left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        #Further implemeting

    def left(self, left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        #Further implemeting

    def stop(self):
        self.robot.drive_system.stop()

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, position):
        self.robot.arm_and_claw.move_arm_to_position(position)

    def quit(self):
        self.stop_program = True

    def exit(self):
        pass 