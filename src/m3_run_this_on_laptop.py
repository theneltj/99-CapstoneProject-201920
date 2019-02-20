"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zack Z.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
from tkinter import *
import time


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------

    mqtt_sender=com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------

    root=tkinter.Tk()
    root.title('ZZ Capstone Project')


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------



    main_frame = ttk.Frame(root, padding=10,borderwidth=5,relief="groove")
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    #teleop_frame, arm_frame, control_frame,drive_system_frame, sound_system_frame=get_shared_frames(main_frame,mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    #Feature 9 Person 3
    #flashy_pickup_frame=ttk.Frame(padding=10,borderwidth=5,relief="groove")
    #flashy_pickup_button=ttk.Button(flashy_pickup_frame,text="Flashy Pickup")
    #speed_label=ttk.Label(flashy_pickup_frame, text='Starting Flash Speed')
    #speed_entry=ttk.Entry(flashy_pickup_frame, width='10')
    #increase_label=ttk.Label(flashy_pickup_frame, text='Flash Speed Increase')
    #increase_entry=ttk.Entry(flashy_pickup_frame, width='10')
    #flashy_pickup_label=ttk.Label(flashy_pickup_frame, text='Flash While Getting an Item')

    #flashy_pickup_label.grid(row=0, column=1)
    #flashy_pickup_button.grid(row=1, column=1)
    #speed_label.grid(row=1, column=0)
    #speed_entry.grid(row=2,column=0)
    #increase_label.grid(row=1, column=2)
    #increase_entry.grid(row=2, column=2)

    #flashy_pickup_button["command"]=lambda: handle_flashy_pickup(speed_entry,increase_entry,mqtt_sender)


    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    #grid_frames(teleop_frame,arm_frame,control_frame,drive_system_frame,sound_system_frame,flashy_pickup_frame)

    #--------------------------------------------------------------------------

    #Sprint 3 Stuff (Final Personalized GUI)

    #--------------------------------------------------------------------------

    filename = PhotoImage(file="C:\\Users\\zdanavz\\Documents\\Classes\\CS120\\Jaws.jpg")
    Jaws_Pic = ttk.Label(main_frame, image=filename)
    Jaws_Pic.grid()


    RoboShark_Frame=ttk.Frame(padding=10,borderwidth=5,relief="groove")
    RoboShark_Label=ttk.Label(RoboShark_Frame,text="ROBOSHARK")
    Hunt_Button=ttk.Button(RoboShark_Frame,text="HUNT!")
    Lazer_Beam_Button=ttk.Button(RoboShark_Frame, text="FIRE LAZER!")
    Action_Label=ttk.Label(RoboShark_Frame, text="Waiting")



    RoboShark_Frame.grid(row=0, column=1)
    RoboShark_Label.grid(row=0,column=1)
    Hunt_Button.grid(row=1,column=1)
    Lazer_Beam_Button.grid(row=2, column=1)
    Action_Label.grid(row=3,column=1)


    Hunt_Button["command"]=lambda: (handle_hunt(mqtt_sender), Action_Label.config(text="Hunting"))
    Lazer_Beam_Button["command"]=lambda: (handle_Lazer(mqtt_sender), Action_Label.config(text="Lazer Fired"))






    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def handle_flashy_pickup(speed,increase,mqtt_sender):
    print('Flashy Pickup')
    mqtt_sender.send_message("Flashy_Pickup", [speed.get(), increase.get()])


def handle_hunt(mqtt_sender):
    print('Hunting')
    mqtt_sender.send_message("Hunt")

def handle_Lazer(mqtt_sender):
    print("Firing Lazer")
    mqtt_sender.send_message("Fire_Lazer")



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame=shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
    drive_system_frame=shared_gui.get_drive_system_frame(main_frame,mqtt_sender)
    sound_system_frame=shared_gui.get_sound_system_frame(main_frame,mqtt_sender)

    return teleop_frame, arm_frame, control_frame,drive_system_frame,sound_system_frame


def grid_frames(teleop_frame, arm_frame, control_frame,drive_system_frame, sound_system_frame,flashy_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    drive_system_frame.grid(row=3,column=0)
    sound_system_frame.grid(row=4,column=0)
    flashy_frame.grid(row=0,column=1)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()