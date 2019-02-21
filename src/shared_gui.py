"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Tyler Thenell, Jacob Jarski, Zack Z.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame

def get_drive_system_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive System")

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    seconds_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    distance_entry = ttk.Entry(frame, width=8)
    speed_label = ttk.Label(frame, text="Speed:")
    time_label = ttk.Label(frame, text="Time:")
    distance_label = ttk.Label(frame, text="Distance:")

    seconds_button = ttk.Button(frame, text="STRAIGHT: Time")
    inches_time_button = ttk.Button(frame, text="STRAIGHT: Inches (Time)")
    inches_encoder_button = ttk.Button(frame, text="STRAIGHT: Inches (Distance)")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    seconds_button.grid(row=1, column=0)
    inches_time_button.grid(row=1, column=1)
    inches_encoder_button.grid(row=1, column=2)

    speed_label.grid(row=2, column=0)
    time_label.grid(row=2, column=1)
    distance_label.grid(row=2, column=2)

    speed_entry.grid(row=3, column=0)
    seconds_entry.grid(row=3, column=1)
    distance_entry.grid(row=3, column=2)


    # Colors and intensity:

    color_label = ttk.Label(frame, text="COLOR LIST:")
    color_0_label = ttk.Label(frame, text="0-None")
    color_1_label = ttk.Label(frame, text="1-Black")
    color_2_label = ttk.Label(frame, text="2-Blue")
    color_3_label = ttk.Label(frame, text="3-Green")
    color_4_label = ttk.Label(frame, text="4-Yellow")
    color_5_label = ttk.Label(frame, text="5-Red")
    color_6_label = ttk.Label(frame, text="6-White")
    color_7_label = ttk.Label(frame, text="7-Brown")

    color_label.grid(row=10, column=0)
    color_0_label.grid(row=10, column=1)
    color_1_label.grid(row=10, column=2)
    color_2_label.grid(row=11, column=0)
    color_3_label.grid(row=11, column=1)
    color_4_label.grid(row=11, column=2)
    color_5_label.grid(row=12, column=0)
    color_6_label.grid(row=12, column=1)
    color_7_label.grid(row=12, column=2)

    color_is_button = ttk.Button(frame, text="Straight while on color:")
    color_is_not_button = ttk.Button(frame, text="Straight while not on color:")
    color_entry = ttk.Entry(frame, width=8)
    color_is_button.grid(row=5, column=0)
    color_is_not_button.grid(row=5, column=1)
    color_entry.grid(row=5, column=2)
    color_entry_label = ttk.Label(frame, text="Color:")
    color_entry_label.grid(row=4,column=2)

    intensity_less_than_button = ttk.Button(frame, text="Straight with Intensity less than:")
    intensity_greater_than_button = ttk.Button(frame, text="Straight with Intensity greater than:")
    intensity_entry = ttk.Entry(frame, width=8)
    intensity_less_than_button.grid(row=7, column=0)
    intensity_greater_than_button.grid(row=7, column=1)
    intensity_entry.grid(row=7, column=2)
    intensity_entry_label = ttk.Label(frame, text="Intensity:")
    intensity_entry_label.grid(row=6, column=2)

    # Set the button callbacks:
    seconds_button["command"] = lambda: handle_straight_for_seconds(seconds_entry, speed_entry, mqtt_sender)
    inches_time_button["command"] = lambda: handle_straight_for_inches_using_time(distance_entry, speed_entry, mqtt_sender)
    inches_encoder_button["command"] = lambda: handle_straight_for_inches_using_encoder(distance_entry, speed_entry, mqtt_sender)

    color_is_button["command"] = lambda: handle_straight_until_color_is(color_entry, speed_entry, mqtt_sender)
    color_is_not_button["command"] = lambda: handle_straight_until_color_is_not(color_entry, speed_entry, mqtt_sender)
    intensity_less_than_button["command"] = lambda: handle_straight_while_intensity_less_than(intensity_entry, speed_entry, mqtt_sender)
    intensity_greater_than_button["command"] = lambda: handle_straight_while_intensity_greater_than(intensity_entry, speed_entry, mqtt_sender)

    #################
    #Camera Stuff
    ################

    C_spin_button=ttk.Button(frame,text="Spin While Looking")
    CC_spin_button=ttk.Button(frame,text="Spin CC While Looking")
    Object_Info_button=ttk.Button(frame,text="Object Info")
    spin_entry=ttk.Entry(frame, width="8")
    spin_label=ttk.Label(frame,text="Spin Speed")
    area_label=ttk.Label(frame,text="Item Area")
    area_entry=ttk.Entry(frame,width="8")

    C_spin_button.grid(row=1,column=3)
    CC_spin_button.grid(row=2,column=3)
    spin_label.grid(row=3,column=3)
    spin_entry.grid(row=4,column=3)
    area_label.grid(row=5,column=3)
    area_entry.grid(row=6,column=3)
    Object_Info_button.grid(row=7,column=3)

    C_spin_button["command"]=lambda: handle_C_Spin(spin_entry,area_entry,mqtt_sender)
    CC_spin_button["command"]=lambda: handle_CC_Spin(spin_entry,area_entry,mqtt_sender)
    Object_Info_button["command"]=lambda: handle_Object_Info_Button(mqtt_sender)
    return frame

def get_my_m1_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    forward_grab_button = ttk.Button(frame, text="Forward Grab")
    spin_forward_grab_button = ttk.Button(frame, text="Spin Forward Grab")
    forward_grab_button.grid(row=0, column=0)
    spin_forward_grab_button.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame)
    speed_label = ttk.Label(frame, text="Speed:")
    cw_entry = ttk.Entry(frame)
    cw_label = ttk.Label(frame, text="CW/CCW")

    speed_label.grid(row=1, column=0)
    cw_label.grid(row=1, column=1)
    speed_entry.grid(row=2, column=0)
    cw_entry.grid(row=2, column=1)

    forward_grab_button["command"] = lambda: handle_forward_grab(speed_entry, mqtt_sender)
    spin_forward_grab_button["command"] = lambda: handle_spin_forward_grab(speed_entry, cw_entry, mqtt_sender)

    return  frame
def get_my_m2_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    increasing_pitch_pickup_button = ttk.Button(frame, text="Increasing Pitch Pickup")
    spin_increasing_pitch_pickup_button = ttk.Button(frame, text="Spin Increasing Pitch Pickup")
    increasing_pitch_pickup_button.grid(row=0, column=0)
    spin_increasing_pitch_pickup_button.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame)
    speed_label = ttk.Label(frame, text="Speed:")
    cw_entry = ttk.Entry(frame)
    cw_label = ttk.Label(frame, text="CW/CCW")

    speed_label.grid(row=1, column=0)
    cw_label.grid(row=1, column=1)
    speed_entry.grid(row=2, column=0)
    cw_entry.grid(row=2, column=1)

    increasing_pitch_pickup_button["command"] = lambda: handle_increasing_pitch_pickup(speed_entry, mqtt_sender)
    spin_increasing_pitch_pickup_button["command"] = lambda: handle_spin_increasing_pitch_pickup(speed_entry, cw_entry, mqtt_sender)

    return frame

def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame

def get_sound_system_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sound System")

    number_beeps_entry = ttk.Entry(frame, width=8)
    freq_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    time_entry = ttk.Entry(frame, width=8)
    phrase_entry = ttk.Entry(frame, width=8)
    number_beeps_label = ttk.Label(frame, text="Number:")
    freq_label = ttk.Label(frame, text="Frequency:")
    time_label = ttk.Label(frame, text="Milliseconds:")
    phrase_label = ttk.Label(frame, text="Phrase:")

    beep_button = ttk.Button(frame, text="Beeper")
    tone_button = ttk.Button(frame, text="Toner")
    speak_button = ttk.Button(frame, text="Speaker")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    beep_button.grid(row=1, column=0)
    tone_button.grid(row=1, column=1)
    speak_button.grid(row=1, column=2)

    number_beeps_label.grid(row=2, column=0)
    freq_label.grid(row=2, column=1)
    time_label.grid(row=4, column=1)
    phrase_label.grid(row=2, column=2)

    number_beeps_entry.grid(row=3, column=0)
    freq_entry.grid(row=3, column=1)
    time_entry.grid(row=5, column=1)
    phrase_entry.grid(row=3, column=2)

    # Set the button callbacks:
    beep_button["command"] = lambda:handle_beeper(number_beeps_entry,mqtt_sender)
    tone_button["command"] = lambda: handle_tone(freq_entry,time_entry,mqtt_sender)
    speak_button["command"] = lambda: handle_speaker(phrase_entry, mqtt_sender)

    return frame

def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

"""Creates the music frame with 2 options: Cartoon or Movie theme"""
def get_batman_music_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="MUSIC")
    frame_label.grid(row=0, column=0)
    cartoon_theme_button = ttk.Button(frame, text="Play Cartoon Theme")
    cartoon_theme_button.grid(row=1, column=0)
    movie_theme_button = ttk.Button(frame, text="Play Movie Theme")
    movie_theme_button.grid(row=2, column=0)

    cartoon_theme_button['command'] = lambda: handle_play_cartoon_theme(mqtt_sender)
    movie_theme_button['command'] = lambda: handle_play_movie_theme(mqtt_sender)

    return frame

"""This function creates and returns the different villians that are to be captured by the robot. Clicking on one 
initiates the robots capture abilities"""
def get_batman_capture_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="CAPTURE")
    frame_label.grid(row=0, column=0)
    joker_button = ttk.Button(frame, text="Joker")
    joker_button.grid(row=1, column=0)
    riddler_button = ttk.Button(frame, text="Riddler")
    riddler_button.grid(row=2, column=0)

    joker_button['command'] = lambda: handle_capture_joker(mqtt_sender)
    riddler_button['command'] = lambda: handle_capture_burglar(mqtt_sender)

    return frame

"""This function creates and returns the different friends/characters that are to be saved by the robot. 
Clicking on one initiates the robots save abilities"""
def get_batman_save_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="SAVE")
    frame_label.grid(row=0, column=0)
    robin_button = ttk.Button(frame, text="Robin")
    robin_button.grid(row=1, column=0)
    girl_button = ttk.Button(frame, text="Girl")
    girl_button.grid(row=2, column=0)

    robin_button['command'] = lambda: handle_save_robin(mqtt_sender)
    girl_button['command'] = lambda: handle_save_girl(mqtt_sender)

    return frame

"""The catchphrase function sends information to the robot including the original catchphrase or a custom one created
by the user."""
def get_batman_catchphrase_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="CATCHPHRASE")
    frame_label.grid(row=0, column=0)
    catchphrase_button = ttk.Button(frame, text="Catchphrase!")
    catchphrase_button.grid(row=1, column=0)
    phrase_label = ttk.Label(frame, text='Enter your own:')
    phrase_label.grid(row=2,column=0)
    phrase_entry = ttk.Entry(frame, width=8)
    phrase_entry.grid(row=3, column=0)
    say_it_button = ttk.Button(frame, text='Say it!')
    say_it_button.grid(row=4, column=0)

    catchphrase_button['command'] = lambda: handle_phrase(mqtt_sender, 'I am the vengeance, I am the night, I am Batman')
    say_it_button['command'] = lambda: handle_phrase(mqtt_sender, str(phrase_entry.get()))

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Forward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('go', [left_entry_box.get(), right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Backward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('go', [str(-int(left_entry_box.get())), str(-int(right_entry_box.get()))])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Left', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('go', [str(-int(left_entry_box.get())), str(int(right_entry_box.get()))])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('Right', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('go', [str(int(left_entry_box.get())), str(-int(right_entry_box.get()))])

def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Stop')
    mqtt_sender.send_message('stop')

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Raise Arm')
    mqtt_sender.send_message('raise_arm')

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Lower Arm')
    mqtt_sender.send_message('lower_arm')

def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Calibrate Arm')
    mqtt_sender.send_message('calibrate_arm')

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('Move Arm to Position')
    mqtt_sender.send_message('move_arm_to_position', [arm_position_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################

def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print("Quit")
    mqtt_sender.send_message("quit")

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('Exit')
    mqtt_sender.send_message("exit")


###############################################################################
# Handlers for Buttons in the Sound System frame.
###############################################################################

def handle_beeper(number_beeps_entry, mqtt_sender):
    print('Beeper')
    mqtt_sender.send_message('beeper', [number_beeps_entry.get()])

def handle_tone(freq_entry , time_entry, mqtt_sender):
    print('Toner')
    mqtt_sender.send_message('toner', [freq_entry.get(),time_entry.get()])

def handle_speaker(phrase_entry, mqtt_sender):
    print('Saying the Phrase!')
    mqtt_sender.send_message('speaker', [phrase_entry.get()])

###############################################################################
# Handlers for Buttons in the Drive System frame.
###############################################################################

def handle_straight_for_seconds(seconds_entry, speed_entry, mqtt_sender):
    print('Straight for Seconds')
    mqtt_sender.send_message('straight_for_seconds',
                             [str(int(seconds_entry.get())), str(int(speed_entry.get()))])

def handle_straight_for_inches_using_time(distance_entry, speed_entry, mqtt_sender):
    print('Straight for Inches (Time)')
    mqtt_sender.send_message('straight_for_inches_using_time',
                             [str(int(distance_entry.get())), str(int(speed_entry.get()))])

def handle_straight_for_inches_using_encoder(distance_entry, speed_entry, mqtt_sender):
    print('Straight for Inches (Encoder)')
    mqtt_sender.send_message('straight_for_inches_using_encoder',
                             [str(int(distance_entry.get())), str(int(speed_entry.get()))])

def handle_straight_until_color_is(color_entry, speed_entry, mqtt_sender):
    print('Straight until color is')
    mqtt_sender.send_message('straight_until_color_is', [int(color_entry.get()), int(speed_entry.get())])

def handle_straight_until_color_is_not(color_entry, speed_entry, mqtt_sender):
    print('Straight until color is not')
    mqtt_sender.send_message('straight_until_color_is_not', [(int(color_entry.get())), int(speed_entry.get())])

def handle_straight_while_intensity_less_than(intensity_entry, speed_entry, mqtt_sender):
    print('Straight while intensity is less')
    mqtt_sender.send_message('straight_while_intensity_less_than', [int(intensity_entry.get()), int(speed_entry.get())])

def handle_straight_while_intensity_greater_than(intensity_entry, speed_entry, mqtt_sender):
    print('Straight while intensity is greater')
    mqtt_sender.send_message('straight_while_intensity_greater_than', [int(intensity_entry.get()), int(speed_entry.get())])

def handle_C_Spin(speed,area,mqtt_sender):
    print('Spin While Looking for Object')
    mqtt_sender.send_message('Spin_C_While_Looking',[int(speed.get()), int(area.get())])

def handle_CC_Spin(speed,area,mqtt_sender):
    print('Spin CC While Looking for Object')
    mqtt_sender.send_message('Spin_CC_While_Looking', [int(speed.get()), int(area.get())])

def handle_Object_Info_Button(mqtt_sender):
    print('Getting Info')
    mqtt_sender.send_message('Display_Info')

def handle_forward_grab(speed_entry, mqtt_sender):
    print('Forward Grab')
    mqtt_sender.send_message('forward_grab', [int(speed_entry.get())])

def handle_spin_forward_grab(speed_entry, cw_entry, mqtt_sender):
    print('Spin Forward Grab')
    mqtt_sender.send_message('spin_forward_grab', [int(speed_entry.get()), str(cw_entry.get())])

def handle_increasing_pitch_pickup(speed_entry, mqtt_sender):
    print('Increasing Pitch Pickup')
    mqtt_sender.send_message('increasing_pitch_pickup', [int(speed_entry.get())])

def handle_spin_increasing_pitch_pickup(speed_entry, cw_entry, mqtt_sender):
    print('Spin Increasing Pitch Pickup')
    mqtt_sender.send_message('spin_increasing_pitch_pickup', [int(speed_entry.get()), str(cw_entry.get())])

def handle_play_cartoon_theme(mqtt_sender):
    print('Playing Cartoon Theme')
    mqtt_sender.send_message('play_cartoon_theme')

def handle_play_movie_theme(mqtt_sender):
    print('Playing Movie Theme')
    mqtt_sender.send_message('play_movie_theme')

def handle_capture_joker(mqtt_sender):
    print('Capturing The Joker')
    mqtt_sender.send_message('capture_joker')

def handle_capture_burglar(mqtt_sender):
    print('Capturing The Riddler')
    mqtt_sender.send_message('capture_riddler')

def handle_save_robin(mqtt_sender):
    print('Saving Robin')
    mqtt_sender.send_message('save_robin')

def handle_save_girl(mqtt_sender):
    print('Saving Girl')
    mqtt_sender.send_message('save_girl')

def handle_phrase(mqtt_sender, phrase):
    print('Saying Phrase')
    print(phrase)
    mqtt_sender.send_message('say_phrase', [phrase])
