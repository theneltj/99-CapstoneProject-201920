# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
def main():
 place = 'Campground'
 action_array = [0, 0, 0, 0, 0, 0, 0]

 def place_discriptions(place, action_array):
     Campground_Description = 'You arrive back at your small campground, the fire still burning brightly.'
     Forest_Description = 'While the forest is vast, there does not appear to be anything here'
     Gashed_Tree_Description = 'You arrive at a tree that appears to have a sharp knife stuck in the bark.' \
                               'You think you could remove it if you tried to.'
     Cliff_Description = 'There is a large cliff in front of you, not easily scalable without any assistance.' \
                         'There appears to be a latch for a rope of some sort halfway up the cliff.'
     Ridge_Description = 'Struck into the rock is a large sledgehammer. You can remove it if you would like'
     Tree_With_Rope_Description = 'In front of you stands an incredibly large oak tree, with rope fastened to climb upon it.' \
                                  'Perhaps the rope could be useful if you cut it?'
     Shack_Description = 'You arrive at the shack, but the door is locked. You can see something inside however.' \
                         'The door could be broken with a large item'
     Plains_Description = 'You arrive in a large plains, surrounded by a large amount of low standing grasses.' \
                          'Galloping in the grass reminds you pleasantly of your childhood.' \
                          'It does not appear like anything other than wasting time can be done here'
     House_Description = 'You arrive at the doorstep of the house, but the front door is locked with a key.' \
                         'A note is written on the door. "Left the key in the shack."' \
                         'You take the note with you and place it in your pocket'
     if action_array[0] == 1:
        Gashed_Tree_Description = 'You arrive at a tree that once had a sharp knife in its bark, pulled out by yourself'
     if action_array[1] == 1:
         Tree_With_Rope_Description = 'In front of you stands an incredibly large oak tree, with remnants of rope attached'
     if action_array[4] == 1:
         Cliff_Description = 'There is a large cliff in front of you, able to be scaled with the rope you have attached.'
     if action_array[2] == 1:
         Ridge_Description = 'A large rock has several hammer marks from the large sledgehammer you have taken.'
     if action_array[5] == 1:
         Shack_Description = 'You arrive at the shack, but the door is now non-existent due to you bludgeoning it with' \
                             'a large sledgehammer, a key appears to be inside!'
     if action_array[3] == 1:
         Shack_Description = 'You arrive at a shack, but the door is now non-existent due to you bludgeoning it with' \
                             'a large sledgehammer, only junk and dust appear to reside here'
     if action_array[6] == 1:
         House_Description = 'You arrive at the doorstep of the house, but the front door is locked with a key.' \
                             'A note appears to have been taken. Oh right! You pull the note out of your pocket and' \
                             'read it again. "Left the key in the shack". You place the note back in your pocket'
     if action_array[3] == 1:
         House_Description = 'You arrive at the doorstep of the house, but the front door is locked with a key.' \
                             'The key you have looks like it would fit!'

     if place == 'Campground':
         return Campground_Description
     if place == "Forest":
         return Forest_Description
     if place == 'Gashed Tree':
         return Gashed_Tree_Description
     if place == 'Cliff':
         return Cliff_Description
     if place == 'Ridge':
         return Ridge_Description
     if place == 'Tree With Rope':
         return Tree_With_Rope_Description
     if place == 'Shack':
         return Shack_Description
     if place == 'Plains':
         return Plains_Description
     if place == 'House':
         return House_Description


 def direction_discriptions(place, action_array):
    Default_Description = "nothing appears to be in this direction"
    North = Default_Description
    East = Default_Description
    South = Default_Description
    West = Default_Description

    Campground_Description = 'You see your campground in the distance defined by the brightly burning campfire'
    Forest_Description = 'appears to be a large forest area, it seems to go on for a while'
    Tree_With_Rope_Description = 'you see a large oak tree, much larger than the surrounding trees. ' \
                             'It looks like something is attached to it...'
    Cliff_Description = 'you see a large cliff, with a ridge above it. ' \
                        'The cliff appears to be huge in comparison to yourself, ' \
                        'about 12 feet tall or so...'
    Plains_Description = 'you see a large amount of plains, almost flat. ' \
                         'There appears to be something in the distance'
    Gashed_Tree_Description = 'you see a glint appearing from a tree, an item of some sort?'
    Ridge_Description = 'there is a large ridge that is not possible to scale without help. ' \
                        'There appears to be a large sledgehammer on top of the ridge'
    Shack_Description = 'there appears to be a shack, small but apparently quite sturdy.' \
                        'The door on the front looks like it could be broken with enough force.'
    House_Description = 'There appears to be a large house, resembling the bandits house you have heard of!'

    if action_array[0] == 1:
        Gashed_Tree_Description = 'The apparent glint from the tree is no longer there now that you have removed the knife'

    if action_array[1] == 1:
        Tree_With_Rope_Description = 'you see a large oak tree, much larger than the surrounding trees. Nothing' \
                                     'looks to be attached to it...'
    if action_array[4] == 1:
        Ridge_Description = 'there is a large ridge in front of you, able to be scaled with the rope you have attached.' \
                            'There appears to be a large sledgehammer on top of the cliff.'
    if action_array[2] == 1:
        Ridge_Description = 'there is a large ridge in front of you, able to be scaled with the rope you have attached.' \
                             'The sledgehammer previously seen has now been take by yourself.'
    if action_array[5] == 1:
        Shack_Description = 'There appears to be a shack, small but apparently quite sturdy. The door on the front has' \
                            'been demolished by a large sledgehammer'



    if place == 'Campground':
        North = Plains_Description
        East = Forest_Description
        South = Tree_With_Rope_Description
        West = Cliff_Description

    if place == 'Forest':
        East = Gashed_Tree_Description
        West = Campground_Description

    if place == 'Gashed Tree':
        West = Forest_Description

    if place == 'Cliff':
        East = Campground_Description
        West = Ridge_Description

    if place == 'Ridge':
        East = Cliff_Description

    if place == 'Tree With Rope':
        North = Campground_Description
        South = Shack_Description

    if place == 'Shack':
        North = Tree_With_Rope_Description

    if place == 'Plains':
        North = House_Description
        South = Campground_Description

    if place == 'House':
        South = Plains_Description


    return [North, East, South, West]



 def where_am_i_now(place, direction):
     if place == 'Campground':
         if direction == 'East':
             place = 'Forest'
             return place
         if direction == 'West':
             place = 'Cliff'
             return place
         if direction == 'North':
             place = 'Plains'
             return place
         if direction == 'South':
             place = 'Tree With Rope'
             return place


     if place == 'Forest':
        if direction == 'West':
            place = 'Campground'
            return place
        if direction == 'East':
            place = 'Gashed Tree'
            return place
        else:
            print('You have entered an incorrect direction')
            return place


     if place == 'Gashed Tree':
         if direction == 'West':
             place = 'Forest'
             return place
         else:
             print('You have entered an incorrect direction')
             return place


     if place == 'Cliff':
         if direction == 'East':
             place = 'Campground'
             return place
         if direction == 'West':
             if action_array[2] == 1:
                place = 'Ridge'
                return place
             else:
                 print('You cannot scale the cliff!')
                 return place
         else:
             print('You have entered an incorrect direction')
             return place


     if place == 'Ridge':
         if direction == 'East':
             place = 'Cliff'
             return place
         else:
             print('You have entered an incorrect direction')
             return place


     if place == 'Tree With Rope':
         if direction == 'North':
             place = 'Campground'
             return place
         if direction == 'South':
             place = 'Shack'
             return place
         else:
             print('You have entered an incorrect direction')
             return place


     if place == 'Shack':
         if direction == 'North':
             place = 'Tree With Rope'
             return place
         else:
             print('You have entered an incorrect direction')
             return place


     if place == 'Plains':
         if direction == 'North':
             place = 'House'
             return place
         if direction == 'South':
             place = 'Campground'
             return place
         else:
             print('You have entered an incorrect direction')
             return place


     if place == 'House':
         if direction == 'South':
             place = 'Plains'
             return place
         else:
             print('You have entered an incorrect direction')
             return place



 def direction(place):
     while True:
         direction = str(input('What direction would you like to go? If you would like to interact instead input "Interact"'))

         if direction == "West" or direction == 'East' or direction == 'South' or direction == 'North' or direction == 'Interact':
             break
         else:
             print('That is not a correct input, please enter a direction of '
                   'North, East, South, or West. If you want to interact enter "Interact"')
     if place == 'Campground':
         print('You have headed,', direction)

     if place == 'Forest':
        if direction == 'East' or 'West':
            print('You have headed,',direction)

     if place == 'Gashed Tree':
         if direction == "West":
             print('You have headed,', direction)

     if place == 'Cliff':
         if direction == 'Interact':
             if action_array[4] == 0:
                 if action_array[1] == 1:
                     print('You attach the rope to the latch, allowing you to go up the cliff if you desire')
                     action_array[4] = 1
                 else:
                     print('You do not have anything to attach to the latch!')
             else:
                 print('The rope is already attached, there is nothing else to interact with here')

         if direction == 'East':
             print('You have headed,', direction)

         if direction == 'West':
             if action_array[2] == 1:
                 print('You have climbed up the rope',direction)

     if place == 'Ridge':
         if direction == 'Interact':
             if action_array[2] == 0:
                print('You manage to grab the large sledgehammer out quite easily.')
                action_array[2] = 1
             else:
                 print('There is nothing to interact with here.')
         if direction == 'East':
             print('You have climbed down the rope', direction)

     if place == 'Tree With Rope':
         if direction == 'Interact':
             if action_array[1] == 0:
                 if action_array[0] == 1:
                    print('You manage to detach most of the rope after cutting it with your knife')
                    action_array[1] = 1
                 if action_array[0] == 0:
                     print('You do not have anything to cut the rope with!')
             elif action_array[1] == 1:
                 print('You have already cut the rope, there is nothing else to interact with here.')
         if direction == 'North' or 'South':
             print('You have headed,', direction)

     if place == 'Shack':
         if direction == 'North':
             print('You have headed,', direction)

     if place == 'Plains':
         if direction == 'North' or 'South':
             print('You have headed,', direction)


     if place == 'House':
         if direction == 'South':
             print('You have headed,', direction)
     print('')
     return direction

 def position(place, action_array):
     direction_discription = direction_discriptions(place, action_array)
     place_discription = place_discriptions(place, action_array)
     print(place_discription)
     print('')
     print('To the North,', direction_discription[0])
     print('')
     print('To the East,', direction_discription[1])
     print('')
     print('To the South,', direction_discription[2])
     print('')
     print('To the West,', direction_discription[3])
     print('')



 position(place, action_array)

 while True:

    going_this_direction = direction(place)
    place = where_am_i_now(place, going_this_direction)
    position(place, action_array)









main()

