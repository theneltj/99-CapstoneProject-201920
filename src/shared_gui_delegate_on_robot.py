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

    def stop(self):
        self.robot.drive_system.stop()

    def raise_arm(self):
        self.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        self.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    def quit(self):
        self.stop_program = True

    def exit(self):
        pass

    def straight_for_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def straight_for_inches_using_time(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def beeper(self, n):
        for _ in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def toner(self, freq_entry, time_entry):
        self.robot.sound_system.tone_maker.play_tone(freq_entry, time_entry)

    def speaker(self,speaker_entry):
        self.robot.sound_system.speech_maker.speak(speaker_entry)