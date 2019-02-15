"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tyler Thenell, Jacob Jarski, Zack Z.
  Winter term, 2018-2019.
"""
import rosebot
import time

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
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    def quit(self):
        self.stop_program = True

    def exit(self):
        self.stop_program = True

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

    def straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, speed)

    def straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, speed)

    def straight_while_intensity_less_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)

    def straight_while_intensity_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity, speed)

    def Spin_C_While_Looking(self,speed,area):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed,area)

    def Spin_CC_While_Looking(self,speed,area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed,area)

    def Display_Info(self):
        self.robot.drive_system.display_camera_data()

    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)

    def go_until_distance_is_within(self, delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(self, delta, inches, speed)

    #Feature 9 Person 3

    def Flashy_Pickup(self,speed,increase):
        self.robot.drive_system.go(50,50)
        time_on=float(speed)
        while self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()>1.5:
            self.robot.led_system.left_led.turn_on()
            time.sleep(float(time_on))
            self.robot.led_system.left_led.turn_off()
            self.robot.led_system.right_led.turn_on()
            time.sleep(float(time_on))
            self.robot.led_system.left_led.turn_on()
            time.sleep(float(time_on))
            self.robot.led_system.left_led.turn_off()
            self.robot.led_system.right_led.turn_off()
            time.sleep(float(time_on))
            time_on=time_on-float(increase)
            if time_on<0.1:
                time_on=0.1
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.raise_arm()

    def forward_grab(self, speed):
        self.robot.drive_system.go(speed, speed)
        while self.robot.sensor_system.ir_proximity_sensor.get_distance() > 3:
            self.robot.sound_system.beeper.beep()
            time.sleep(self.robot.sensor_system.ir_proximity_sensor.get_distance()/100)
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.raise_arm()

    def spin_forward_grab(self, speed, direction):
        if direction == 'CW':
            self.robot.drive_system.spin_clockwise_until_sees_object(speed, 200)
        if direction == 'CCW':
            self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, 200)
        self.forward_grab(speed)

    def increasing_pitch_pickup(self, speed):
        self.robot.drive_system(speed, speed)
        while self.robot.sensor_system.ir_proximity_sensor.get_distance() > 3:
            self.robot.sound_system.tone_maker.play_tone((100 - self.robot.sensor_system.ir_proximity_sensor.get_distance())* 8, 250)
            time.sleep(.5)
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.raise_arm()

    def spin_increasing_pitch_pickup(self, speed, direction):
        if direction == 'CW':
            self.robot.drive_system.spin_clockwise_until_sees_object(speed, 200)
        if direction == 'CCW':
            self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, 200)
        self.increasing_pitch_pickup(speed)
