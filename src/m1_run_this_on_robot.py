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
    # robot.arm_and_claw.raise_arm()
    # robot.arm_and_claw.calibrate_arm()
    # robot.arm_and_claw.raise_arm()
    # robot.arm_and_claw.lower_arm()

    #robot.drive_system.go_straight_for_inches_using_encoder(10, 100)

    real_thing()

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()