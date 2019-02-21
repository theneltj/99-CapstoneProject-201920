# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
def robot_go_zorg():
    robot_direction = 'north'
    print(robot_direction)
    def new_direction(robot_direction):
        while True:
            if(robot_direction == 'north'):
                robot_direction = input('new')
                if(robot_direction == 'east'):
                    print('rotate 90 cw')
                    return('east')
                elif(robot_direction == 'south'):
                    print('rotate 180 cw')
                    return('south')
                elif(robot_direction == 'west'):
                    print('rotate 270 cw')
                elif(robot_direction == 'north'):
                    print('do not rotate')
            elif(robot_direction == 'east'):
                robot_direction = input('new')
                if (robot_direction == 'east'):
                    print('do not rotate')
                    return ('east')
                elif (robot_direction == 'south'):
                    print('rotate 90 cw')
                    return ('south')
                elif (robot_direction == 'west'):
                    print('rotate 180 cw')
                    return ('west')
                elif (robot_direction == 'north'):
                    print('rotate 270 cw')
                    return ('north')
            elif(robot_direction == 'south'):
                robot_direction = input('new')
                if (robot_direction == 'east'):
                    print('rotate 270 cw')
                    return ('east')
                elif (robot_direction == 'south'):
                    print('do not rotate')
                    return ('south')
                elif (robot_direction == 'west'):
                    print('rotate 90')
                    return ('west')
                elif (robot_direction == 'north'):
                    print('rotate 180 cw')
                    return ('north')

            elif (robot_direction == 'west'):
                robot_direction = input('new')
                if (robot_direction == 'east'):
                    print('rotate 180 cw')
                    return ('east')
                elif (robot_direction == 'south'):
                    print('rotate 270 cw')
                    return ('south')
                elif (robot_direction == 'west'):
                    print('do not rotate')
                    return ('west')
                elif (robot_direction == 'north'):
                    print('rotate 90 cw')
                    return ('north')

    robot_direction = new_direction(robot_direction)
    print(robot_direction)
    robot_direction = new_direction(robot_direction)
    print(robot_direction)
robot_go_zorg()