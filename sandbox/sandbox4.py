# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
def main():
    robot = 'east'
    print(robot)
    def a(robot):
        while True:
            if(robot == 'east'):
                robot = input('new')
                if(robot == 'east'):
                    print('forward')
                    return('east')
                elif(robot == 'west'):
                    print('backward')
                    return('west')
            elif(robot == 'west'):
                robot = input('new')
                if (robot == 'east'):
                    print('backward')
                    return ('east')
                elif (robot == 'west'):
                    print('forward')
                    return ('west')
    robot = a(robot)
    print(robot)
    robot = a(robot)
    print(robot)
main()