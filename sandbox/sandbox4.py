import time

def robot_go_zorg(robot, robot_direction, old_robot_direction):
    while True:
        if (old_robot_direction == 'north'):
            if (robot_direction == 'east'):

                robot.drive_system.go(50, -50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going East")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('east')
            elif (robot_direction == 'south'):
                robot.drive_system.go(50, -50)
                time.sleep(4.2)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going South")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('south')
            elif (robot_direction == 'west'):
                robot.drive_system.go(-50, 50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going West")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('west')
            elif (robot_direction == 'north'):
                robot.sound_system.speech_maker.speak("I am going North")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('north')
        elif (old_robot_direction == 'east'):
            robot_direction = input('new')
            if (robot_direction == 'east'):
                robot.sound_system.speech_maker.speak("I am going East")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('east')
            elif (robot_direction == 'south'):
                robot.drive_system.go(50, -50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going South")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('south')
            elif (robot_direction == 'west'):
                robot.drive_system.go(50, -50)
                time.sleep(4.2)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going West")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('west')
            elif (robot_direction == 'north'):
                robot.drive_system.go(-50, 50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going North")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('north')
        elif (old_robot_direction == 'south'):
            robot_direction = input('new')
            if (robot_direction == 'east'):
                robot.drive_system.go(-50, 50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going East")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('east')
            elif (robot_direction == 'south'):
                robot.sound_system.speech_maker.speak("I am going South")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('south')
            elif (robot_direction == 'west'):
                robot.drive_system.go(50, -50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going West")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('west')
            elif (robot_direction == 'north'):
                robot.drive_system.go(50, -50)
                time.sleep(4.2)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going North")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('north')

        elif (old_robot_direction == 'west'):
            robot_direction = input('new')
            if (robot_direction == 'east'):
                robot.drive_system.go(50, -50)
                time.sleep(4.2)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going East")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('east')
            elif (robot_direction == 'south'):
                robot.drive_system.go(-50, 50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going South")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('south')
            elif (robot_direction == 'west'):
                robot.sound_system.speech_maker.speak("I am going West")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('west')
            elif (robot_direction == 'north'):
                robot.drive_system.go(50, -50)
                time.sleep(2.1)
                robot.drive_system.stop()
                robot.sound_system.speech_maker.speak("I am going North")
                robot.drive_system.go_straight_for_inches_using_time(5, 100)
                return ('north')