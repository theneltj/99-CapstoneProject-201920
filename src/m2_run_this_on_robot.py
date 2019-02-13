"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Jarski.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    robot = rosebot.RoseBot()
    # robot.arm_and_claw.raise_arm()
    # robot.arm_and_claw.calibrate_arm()
    # robot.arm_and_claw.move_arm_to_position(180*14.2)
    # robot.arm_and_claw.lower_arm()
    robot.sound_system.beeper.beep()
    robot.drive_system.go_backward_until_distance_is_greater_than(12, 50)
    robot.sound_system.beeper.beep()



    # robot.sound_system.tone_maker.play_tone(293, 250).wait()
    # robot.sound_system.tone_maker.play_tone(293, 250).wait()
    # robot.sound_system.tone_maker.play_tone(587, 250).wait()
    # robot.sound_system.tone_maker.play_tone(440, 250).wait()
    # robot.sound_system.tone_maker.play_tone(415, 250).wait()
    # robot.sound_system.tone_maker.play_tone(392, 250).wait()
    # robot.sound_system.tone_maker.play_tone(349, 250).wait()
    # robot.sound_system.tone_maker.play_tone(293, 250).wait()
    # robot.sound_system.tone_maker.play_tone(349, 250).wait()
    # robot.sound_system.tone_maker.play_tone(392, 250).wait()
    # robot.sound_system.tone_maker.play_tone(261, 250).wait()
    # robot.sound_system.tone_maker.play_tone(261, 250).wait()
    # robot.sound_system.tone_maker.play_tone(587, 250).wait()
    # robot.sound_system.tone_maker.play_tone(440, 250).wait()
    # robot.sound_system.tone_maker.play_tone(415, 250).wait()
    # robot.sound_system.tone_maker.play_tone(392, 250).wait()
    # robot.sound_system.tone_maker.play_tone(349, 250).wait()
    # robot.sound_system.tone_maker.play_tone(293, 250).wait()
    # robot.sound_system.tone_maker.play_tone(349, 250).wait()
    # robot.sound_system.tone_maker.play_tone(392, 250).wait()
    # robot.sound_system.tone_maker.play_tone(246, 250).wait()
    # robot.sound_system.tone_maker.play_tone(246, 250).wait()






    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        if delegate.stop_program:
            break
        time.sleep(0.01)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()