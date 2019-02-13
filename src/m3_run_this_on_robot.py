"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Zack Z.
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

    #run_test_arm()

    #run_test_calibration()

    #run_test_move_arm(1000)
    #run_test_move_arm(5112)
    #run_test_move_arm(2000)
    #run_test_move_arm(0)

    #real_thing()
    run_test_get_blob_data()


def run_test_arm():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def run_test_calibration():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def run_test_move_arm(x):
    robot=rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(x)

def real_thing():
    robot=rosebot.RoseBot()
    delegate=shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)

def run_test_get_blob_data():
    robot=rosebot.RoseBot()
    robot.drive_system.display_camera_data()




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()