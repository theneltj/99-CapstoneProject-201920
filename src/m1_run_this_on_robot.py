"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Tyler J Thenell.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    robot = rosebot.RoseBot()
    robot.sound_system.tone_maker.play_tone(100, 300)
    time.sleep(0.5)
    # real_thing()
    for k in range(10):
        print(robot.beacon_system.get_distance_to_beacon())  # int value 0 to 100 (-128 if not found)
        # print(beacon_seeker.heading)  # int value -25 to 25 (degrees)
        time.sleep(1)





def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        if delegate.stop_program == True:
            break
        time.sleep(0.01)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()