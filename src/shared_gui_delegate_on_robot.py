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

    def robot_go_zorg(self,robot_direction, old_robot_direction):
            if (old_robot_direction == 'north'):
                if (robot_direction == 'east'):

                    self.robot.drive_system.go(50, -50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going East")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('east')
                elif (robot_direction == 'south'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(4.2)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going South")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('south')
                elif (robot_direction == 'west'):
                    self.robot.drive_system.go(-50, 50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going West")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('west')
                elif (robot_direction == 'north'):
                    self.robot.sound_system.speech_maker.speak("I am going North")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('north')
            elif (old_robot_direction == 'east'):

                if (robot_direction == 'east'):
                    self.robot.sound_system.speech_maker.speak("I am going East")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('east')
                elif (robot_direction == 'south'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going South")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('south')
                elif (robot_direction == 'west'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(4.2)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going West")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('west')
                elif (robot_direction == 'north'):
                    self.robot.drive_system.go(-50, 50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going North")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('north')
            elif (old_robot_direction == 'south'):
                if (robot_direction == 'east'):
                    self.robot.drive_system.go(-50, 50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going East")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('east')
                elif (robot_direction == 'south'):
                    self.robot.sound_system.speech_maker.speak("I am going South")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('south')
                elif (robot_direction == 'west'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going West")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('west')
                elif (robot_direction == 'north'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(4.2)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going North")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('north')

            elif (old_robot_direction == 'west'):
                if (robot_direction == 'east'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(4.2)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going East")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('east')
                elif (robot_direction == 'south'):
                    self.robot.drive_system.go(-50, 50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going South")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('south')
                elif (robot_direction == 'west'):
                    self.robot.sound_system.speech_maker.speak("I am going West")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('west')
                elif (robot_direction == 'north'):
                    self.robot.drive_system.go(50, -50)
                    time.sleep(2.1)
                    self.robot.drive_system.stop()
                    self.robot.sound_system.speech_maker.speak("I am going North")
                    self.robot.drive_system.go_straight_for_inches_using_time(5, 100)
                    return ('north')

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
        self.robot.drive_system.go(speed, speed)
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

    """"Plays the original cartoon/tv theme commonly referred to as Dunna Dunna Dunna Dunna- Batman!"""
    def play_cartoon_theme(self):
        for _ in range(4):
            self.robot.sound_system.tone_maker.play_tone(587.33, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(587.33, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(554.37, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(554.37, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(523.25, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(523.25, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(554.37, 50)
            time.sleep(.05)
            self.robot.sound_system.tone_maker.play_tone(554.37, 50)
            time.sleep(.05)
        self.robot.sound_system.speech_maker.speak('Batman')

    """"Plays the movie theme using tones and pauses"""
    def play_movie_theme(self):
        self.robot.sound_system.tone_maker.play_tone(293.66, 100)
        time.sleep(.1)
        self.robot.sound_system.tone_maker.play_tone(329.63, 100)
        time.sleep(.1)
        self.robot.sound_system.tone_maker.play_tone(349.23, 100)
        time.sleep(.1)
        self.robot.sound_system.tone_maker.play_tone(466.16, 300)
        time.sleep(.3)
        self.robot.sound_system.tone_maker.play_tone(440.00, 150)
        time.sleep(.6)

        self.robot.sound_system.tone_maker.play_tone(293.66, 100)
        time.sleep(.1)
        self.robot.sound_system.tone_maker.play_tone(329.63, 100)
        time.sleep(.1)
        self.robot.sound_system.tone_maker.play_tone(349.23, 100)
        time.sleep(.1)
        self.robot.sound_system.tone_maker.play_tone(440, 600)
        time.sleep(.6)
        self.robot.sound_system.tone_maker.play_tone(493.88, 300)
        time.sleep(.3)
        self.robot.sound_system.tone_maker.play_tone(523.25, 150)
        time.sleep(.15)

    """"The following capture frames are all repeated junks that use change the color signature before running the next
    parts of the code. The area used in the spin_clockwise function also slightly differ due to different 
    sensitivities with the colors. THEY EACH TARGET THE SPECIFIED CHARACTER. After locating the desired color signature,
    the robot calls the acquire_target function which puts the character in range of the arm and claw. After that, the
    arm is raised and the Bat-bot waits for information to be sent to it from the user regarding what is to be done with
    the character"""
    def capture_joker(self):
        self.robot.sensor_system.camera.set_signature('SIG1')
        self.robot.drive_system.spin_clockwise_until_sees_object(30, 600)
        self.robot.drive_system.batman_acquire_target()
        self.robot.arm_and_claw.raise_arm()

    def capture_riddler(self):
        self.robot.sensor_system.camera.set_signature('SIG2')
        self.robot.drive_system.spin_clockwise_until_sees_object(30, 300)
        self.robot.drive_system.batman_acquire_target()
        self.robot.arm_and_claw.raise_arm()

    def save_robin(self):
        self.robot.sensor_system.camera.set_signature('SIG3')
        self.robot.drive_system.spin_clockwise_until_sees_object(30, 800)
        self.robot.drive_system.batman_acquire_target()
        self.robot.arm_and_claw.raise_arm()

    def save_girl(self):
        self.robot.sensor_system.camera.set_signature('SIG4')
        self.robot.drive_system.spin_clockwise_until_sees_object(30, 600)
        self.robot.drive_system.batman_acquire_target()
        self.robot.arm_and_claw.raise_arm()

    """"The say_phrase function will say the phrase given to it by the GUI. This is either the main catch phrase 
    or a custom phrase inserted by the user"""
    def say_phrase(self, phrase):
        self.robot.sound_system.speech_maker.speak(phrase)

    """"The deliver function takes the keybinding given and reassigns the pressed key to the number 
    associated with the desired color. The function then calls functions from sprint 2 and drives 
    until we land on the color. We then also lower the arm"""
    def deliver(self, first_letter_of_color):
        if first_letter_of_color == 'w':
            color = 6
        if first_letter_of_color == 'g':
            color = 3
        if first_letter_of_color == 'r':
            color = 5
        if first_letter_of_color == 'b':
            color = 2
        self.robot.drive_system.go_straight_until_color_is(color, 50)
        self.robot.arm_and_claw.lower_arm()

    def Hunt(self):
        whats_around=self.robot.sensor_system.color_sensor.get_color()
        if whats_around == 6:
            self.robot.drive_system.Land()
        elif whats_around == 5:
            self.robot.drive_system.Blood()
        elif whats_around ==2:
            self.robot.drive_system.Beach()
        else:
            self.robot.drive_system.Nothing()


    def Fire_Lazer(self):
        self.robot.sound_system.speech_maker.speak("PEW")
        self.robot.led_system.right_led.turn_on()
        self.robot.led_system.left_led.turn_on()
        time.sleep(1)
        self.robot.led_system.right_led.turn_off()
        self.robot.led_system.left_led.turn_off()
        self.robot.sound_system.speech_maker.speak("BOOM")

    def Change_Label(self):
        whats_around = self.robot.sensor_system.color_sensor.get_color()
        if whats_around == 7:
            return "I'm on Land"
        elif whats_around == 5:
            return "I Smell Blood"
        elif whats_around == 2:
            return "I Found a Beach with Swimmers"
        else:
            return "There's nothing around"
