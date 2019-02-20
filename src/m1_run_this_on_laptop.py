"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Tyler J Thenell.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
from tkinter import *



def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('CSSE120 Capstone Project')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth = 5, relief = 'groove')
    # main_frame.grid()
    batman_main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    batman_main_frame_label = ttk.Label(batman_main_frame, text="                                                      "
                                                                "   THE BATBOT")
    batman_main_frame_label.config(background='black', foreground='yellow')
    batman_main_frame_label.config(font=('times', 20, 'bold'))
    batman_main_frame_label.config(width=68)
    batman_main_frame_label.grid(row=0, column=0)

    filename = PhotoImage(file="C:\\Users\\theneltj\\Pictures\\Batman.png")
    batman_main_frame_image = ttk.Label(batman_main_frame, image=filename)
    batman_main_frame_image.grid(row=1, column=0)

    side_frame = ttk.Frame(batman_main_frame)
    side_frame.grid(row=1, column=1)

    batman_main_frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, drive_system_frame, arm_frame, sound_system_frame, control_frame, my_m1_frame = get_shared_frames(main_frame, mqtt_sender)
    batman_music_frame, batman_capture_frame, batman_save_frame, batman_catchphrase_frame = get_batman_frames(side_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, drive_system_frame, arm_frame, sound_system_frame, control_frame, my_m1_frame)
    grid_batman_frames(batman_music_frame, batman_capture_frame, batman_save_frame, batman_catchphrase_frame)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    my_m1_frame = shared_gui.get_my_m1_frame(main_frame, mqtt_sender)
    return teleop_frame, drive_system_frame, arm_frame, sound_system_frame, control_frame, my_m1_frame

def grid_frames(teleop_frame, drive_system_frame, arm_frame, sound_system_frame, control_frame, my_m1_frame):
    teleop_frame.grid(row=0, column=0)
    drive_system_frame.grid(row=1, column=0)
    arm_frame.grid(row=2, column=0)
    sound_system_frame.grid(row=3, column=0)
    control_frame.grid(row=5, column=0)
    my_m1_frame.grid(row=0,column=1)

def get_batman_frames(batman_main_frame, mqtt_sender):
    batman_music_frame = shared_gui.get_batman_music_frame(batman_main_frame, mqtt_sender)
    batman_capture_frame = shared_gui.get_batman_capture_frame(batman_main_frame, mqtt_sender)
    batman_save_frame = shared_gui.get_batman_save_frame(batman_main_frame, mqtt_sender)
    batman_catchphrase_frame = shared_gui.get_batman_catchphrase_frame(batman_main_frame, mqtt_sender)
    return batman_music_frame, batman_capture_frame, batman_save_frame, batman_catchphrase_frame

def grid_batman_frames(batman_music_frame, batman_capture_frame, batman_save_frame, batman_catchphrase_frame):
    batman_music_frame.grid(row=1, column=2)
    batman_capture_frame.grid(row=2, column=2)
    batman_save_frame.grid(row=3, column=2)
    batman_catchphrase_frame.grid(row=4, column=2)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()