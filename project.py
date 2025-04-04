# Hello, Introduction to Programming Students! Welcome to PA2!
# Your task is to implement the necessary functions in this file.

# We wanted to say we were so inspired while doing this game we let our mind flourish and implemented our ideas the best
# way possible. We hope you will enjoy our game and most of all have fun while playing it.
# Julian and Samil

# In this assignment, we will work with dictionaries. Dictionaries are a
# data structure used to store data in key-value pairs.
# For more information, visit:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# We made the inventory a Dictionary, which includes a brief description of each item.
# Aside from that, we also made the map a lot bigger and added 3 other ghosts.
# Another thing we made is when you enter the Master bedroom you are invaded by a Hunter, who you must kill or run
# away from to survive. To kill the boss you need a sword gained by finding a doll, surviving an encounter with 5 ghosts
# and going to the guest bedroom.

rooms = {
    'Grand Hall': {'n': 'Attic', 's': 'Library', 'e': 'Dining Room', 'w': None},
    'Library': {'n': 'Grand Hall', 's': 'Office', 'e': 'Hallway', 'w': None},
    'Dining Room': {'n': 'Kitchen', 's': None, 'e': 'Garden', 'w': 'Grand Hall'},
    'Garden': {'n': None, 's': None, 'e': None, 'w': 'Dining Room'},
    'Secret Room': {'n': None, 's': None, 'e': None, 'w': 'Garden'},
    'Attic': {'n': None, 's': 'Grand Hall', 'e': None, 'w': None},
    'Kitchen': {'n': None, 's': 'Dining Room', 'e': 'Cellar', 'w': None},
    'Cellar': {'n': None, 's': None, 'e': None, 'w': 'Kitchen'},
    'Office': {'n': 'Library', 's': None, 'e': None, 'w': None},
    'Hallway': {'n': None, 's': 'Master Bedroom', 'e': 'Guest Bedroom', 'w': 'Library'},
    'Guest Bedroom': {'n': None, 's': None, 'e': None, 'w': 'Hallway'},
    'Master Bedroom': {'n': 'Hallway', 's': None, 'e': None, 'w': None},
}

room_descriptions = {
    'Grand Hall': "You stand in the majestic Grand Hall.",
    'Library': "You are surrounded by towering ancient books in the Library.",
    'Dining Room': "The dusty Dining Room feels eerily quiet.",
    'Garden': "You find yourself in an overgrown Garden.",
    'Secret Room': "A mysterious Secret Room with a glowing artifact lies ahead.",
    'Attic': 'Up the stairs you find a cramped room, filled with dust and spider webs.',
    'Kitchen': 'A vast kitchen with food and drinks to feed a village.',
    'Cellar': 'A storage room filled with even more food.',
    'Office': 'A room with an old desk and tons of papers.',
    'Hallway': 'This long hallway holds two doors, don\'t let curiosity carry you away.',
    'Guest Bedroom': 'Just a plain old bedroom, nothing much to see here.',
    'Master Bedroom': 'You entered a wide and eerie room, dimly lit by the shine of the moon.',
}
room_objects = {
    'Library': {'item': 'ancient_book of secrets', 'in_inventory': False},
    'Dining Room': {'item': 'mysterious hidden key', 'in_inventory': False},
    'Secret Room': {'item': 'glowing artifact', 'in_inventory': False},
    'Grand Hall': {'item': 'ragged map', 'in_inventory': False},
    'Office': {'item': 'flashlight', 'in_inventory': False},
    'Attic': {'item': 'Dusty Shawl', 'in_inventory': False},
    'Solaire Quest': {'item': 'doll', 'in_inventory': False},
    'Kitchen': {'item': 'Flask of Estus', 'in_inventory': False},
    'Cellar': {'item': 'Bubbling Drink', 'in_inventory': False},
    'Guest Bedroom': {'item': 'Moonlight Great-sword', 'in_inventory': False, 'availability': False}
    # TODO TASK 6 MYSTICAL ARTIFACTS
}


object_descriptions = {
    'mysterious hidden key': 'A mysterious hidden key, found in the Dining Room, may open a hidden door.',
    'ancient_book of secrets': 'A book with insanely valuable information. Use "r" command to read it.',
    'glowing artifact': "The artifact has these words written: \"To claim the fallen sword a "
                        "blessing of strength is required, aside from that you must be cursed with the visit of five "
                        "entities.\"",
    'flashlight': 'An object providing light in times of need. Battery: 60%',
    'doll': 'A beautiful doll granting whomever holds it great strength',
    'Flask of Estus': 'A glowing yellow drink, marked with the symbol of a great king.',
    'Bubbling Drink': 'A drink made to raise a warrior\'s spirits, capable of increasing strength to in-humane levels.',
    'Dusty Shawl': "A piece of soft fabric with great heating capabilities. Also quite fashionable despite being dusty."
    , 'Moonlight Great-sword': "The blade of a warrior fallen from the sky. It shall mentor you and guide"
                             "you in your journey."

}
# TASK 1 COMMANDS FUNCTIONS -----------------------------------------------------+
# Your first task is to implement the functions for each command.
# Commands represent the input from the player.

# TODO: Implement `Move`. This function updates the player's current room
#       when a valid movement command ('n', 's', 'e', 'w') is given.
#       If the move is valid, update the `current_room` and print the
#       room's description (use `room_descriptions`). If invalid,
#       print "You can't go that way."
def Move(current_room, command):
    if command not in ('n', 's', 'e', 'w'):
        print("Invalid command")
    elif rooms[current_room][command] is not None:
        current_room = rooms[current_room][command]
        print(room_descriptions[current_room])
    else:
        print("You can't go that way.")
    return current_room
# TODO: Implement `OpenFrontDoor`. This function checks if the player
# #       wins the game. If the player is in the 'Grand Hall' and has 5 items
#       in the inventory, print a victory message and call `exit()`.
def OpenFrontDoor(inventory, current_room):
    if len(inventory)>=5:
        print("You left the mansion!")
        exit()
    else:
        print(f'You dont have the items')
        return current_room

# TODO: Implement `OpenSecretRoom`. This function opens the secret room
#       if the player is in the Garden and possesses the "mysterious hidden key".
def OpenSecretRoom(current_room, inventory):
    if room_objects['Dining Room']['in_inventory']:
        current_room = "Secret Room"
        print(room_descriptions[current_room])
    else:
        print("You need the mysterious key to open this door.")
    return current_room

# TODO: Implement `Get`. This function allows the player to pick up an item
#       in the current room, if it hasn't been picked up yet. Add the item
#       to the player's inventory and mark it as collected.
def Get(current_room, inventory):
    if current_room == "Grand Hall":
        if room_objects[current_room]["in_inventory"] == False:
            room_objects[current_room]["in_inventory"] = True
            print("You took the Map from the Grand Hall wall")
        else:
            print('You already have the map in your inventory. Press \'v\' to open it.')
    elif current_room == 'Guest Bedroom':
        object = room_objects[current_room]['item']
        if room_objects[current_room]["in_inventory"]:
            print("You already have the Sword in your possession")
        elif not room_objects[current_room]["in_inventory"] and not room_objects[current_room]['availability']:
            print('You are unable to claim the great-sword in your current state.')
        elif not room_objects[current_room]["in_inventory"] and room_objects[current_room]['availability']:
            print('The Moonlight Great-Sword has deemed you worthy. May all enemies fall to your blade.')
            room_objects[current_room]["in_inventory"] = True
            inventory[object] = object_descriptions[object]
    elif current_room in room_objects and current_room != 'Grand Hall':
        object = room_objects[current_room]['item']
        if not room_objects[current_room]["in_inventory"]:
            inventory[object] = object_descriptions[object]
            room_objects[current_room]["in_inventory"] = True
            print("You took the item:", room_objects[current_room]["item"])
        else:
            print("You already took the item from this room.")
    else:
        print("There is no item in this room.")

# TODO: Implement `ShowInventory`. This function displays all items in the
#       player's inventory.
def ShowInventory(inventory):
    print('The items currently in your inventory are:')
    if len(inventory) == 0:
        print(f'You dont have any items in your inventory.')
    else:
        for item, description in inventory.items():
            print(f'\n{item}: "{description}"')

# TODO: Implement `Read`. This function allows the player to read the
#       "ancient_book of secrets" if it's in the inventory.
def Read(inventory):
    if "ancient_book of secrets" in inventory:
        print(f'\"The grandmaster off the manor hidden a specific item from all guest. His favourite hiding spot \n'
              f'resides within a place that you would enjoy a meal.\"')
    else:
        print('You need to find the book first')

# TODO: Implement `ToggleHide`. This function toggles the player's hiding
#       state, printing the appropriate message.
def ToggleHide(hiding):
    if hiding == True:
        print('You are no longer hiding')
        return False
    elif hiding == False:
        print('You are now hiding')
        return True

# ADDED FUNCTION:
# We decided to add a function that helped the player navigate the mansion more easily by reading a map
# For this we added the function bellow and made its command 'v' (view map)
# Also, the map is found in the Grand Hall, and it does not count as an object for winning.
def Show_Map():
    if room_objects["Dining Room"]["in_inventory"] == False:
        print(
            '\n           Attic          Kitchen    →   Cellar\n'
            '              ↑              ↑          \n'
            'Exit <|  Grand Hall →   Dining Room   →   Garden  → ???\n'
            '              ↓\n'
            '          Library  →   Hallway   →  Guest Bedroom \n'
            '             ↓            ↓  \n'
            '           Office    Master Bedroom\n'
        )
    else:
        print(
            '\n           Attic          Kitchen    →   Cellar\n'
            '              ↑              ↑          \n'
            'Exit <|  Grand Hall →   Dining Room   →   Garden  → Secret Room\n'
            '              ↓\n'
            '          Library  →   Hallway   →  Guest Bedroom \n'
            '             ↓            ↓  \n'
            '           Office    Master Bedroom\n'
        )



# Available Commands -------------------------------------------+
# This function displays all possible player commands.
def Manual():
    print(
        "Available Commands:\n"
        "n = move north\n"
        "s = move south\n"
        "e = move east\n"
        "w = move west\n"
        "o = open an object (e.g. door)\n"
        "g = get an item in the room\n"
        "i = display inventory\n"
        "r = read an item (e.g., book)\n"
        "h = hide/un-hide\n"
        "m = show commands\n"
        "q = quit the game\n"
        "v = view the map \n"
        "t = talk to someone\n"
    )


# Exit the game ------------------------------------------------+
def Quit():
    print("Thanks for playing!")
    exit()

# TASK 2 PROCESS COMMAND -----------------------------------------------------+
# TODO: Complete the `ProcessCommand` function. It should check
#       the player's command and call the respective function.
def ProcessCommand(command, current_room, inventory, hiding):
    if hiding == False:
        if command == 'm':
            Manual()
        elif command == 'q':
            Quit()
        elif command == 'n':
            current_room = Move(current_room, command)
        elif command == "s":
            current_room = Move(current_room, command)
        elif command == "e":
            current_room = Move(current_room, command)
        elif command == "w":
            current_room = Move(current_room, command)
        elif command == "o":
            if current_room == "Grand Hall":
                current_room = OpenFrontDoor(inventory, current_room)
            elif current_room == "Garden":
                current_room = OpenSecretRoom(inventory, current_room)
            else:
                print("There's no door to open")
        elif command == "g":
            Get(current_room, inventory)
        elif command == "i":
            ShowInventory(inventory)
        elif command == 'r':
            Read(inventory)
        elif command == 'h':
            hiding = ToggleHide(hiding)
        elif command == 'v':
            if room_objects['Grand Hall']['in_inventory']:
                Show_Map()
            else:
                print('You did not pick up the map')
        elif command=='t':
            if current_room!='Attic':
                print(f'There is no one to talk to in this room.')
        else:
            print("Invalid command.")

    else:
        if command == 'h':
            hiding = ToggleHide(hiding)
        else:
            print("You cannot use any other movement while hiding")

    return current_room, hiding

# TASK 3 GHOST INTERACTIONS -------------------------------------------+
# TODO: Implement `GhostEncounterDinningRoom`. This function presents
#       the player with a riddle and checks if they solve it correctly.
def GhostEncounterDinningRoom():
    print("You find a message in the table that reads: \n"
          "\"Which of the following numbers is a prime number:\n"
          "25, 123, 13\"")
    answer = int(input('> '))
    if answer != 13:
        print('The last thing you heard was "Wrong answer."')
        exit()
    else:
        print('You felt something leave the area, so you decided to hurry.')

# TASK 5 MORE GHOSTS -------------------------------------------+
# TODO: Implement `GhostEncounterLibraryRoom`. This function tells
#       the player to hide. If they fail to hide, they lose the game.
def GhostEncounterLibraryRoom():
    print('However, when you enter you feel the floor sticky...\n'
          'Then you feel a drop of blood fall upon your shoulder...')
    response = input('> ')
    if response != 'h':
        print('The beast fell on you and ate you.\n'
              '\nYOU DIED !')
        exit()
    else:
        print('The beast lost sight of you, you are safe... for now.')
    un_hide = input('> ')
    while un_hide != 'h':
        print('You must get out of hiding before moving')
        un_hide = input('> ')
    print('You are no longer hiding')

# TODO: Implement `GhostEncounterGardenRoom`. This function makes
#       the player lose an item from their inventory. Remember to update
#       the `room_objects` `in_inventory` to false
def GhostEncounterGardenRoom(inventory):
    print(f'A lady ghost suddenly advances towards you quickly.')
    if len(inventory) == 0:
        print(f'You dont have any items in your inventory')
    elif 'flashlight' in inventory:
        print('\nYou used the flashlight to blind the lady and she left.')
    else:
        remove_item = inventory.popitem()
        print(f'You lost {remove_item[0]}')
        for key, item in room_objects.items():
            if item['item']==remove_item[0]:
                room_objects[key]['in_inventory'] = False
#MORE GHOST!!

def GhostEncounterKitchen():
    print('\nThe sound of liquids in a cauldron are the first thing you hear.\n'
          'Then a voice from across the room says: "Would you care to drink from my esteemed potion?'
          '\nI promise it\'ll prove as aid for your mission.(y / n)')
    answer = input('> ')
    while answer != 'y' and answer != 'n':
        print('The question required a simple yes or no...')
        answer = input('> ')
    if answer == 'y':
        print('Oh foolish player, we instructed you to be careful...how could you drink from a ghost\'s potion\n'
            '\nYOU DIED')
        exit()
    elif answer == 'n':
        print('HAHAHA , you are smarter than I thought.\n The ghost and his potion disappeared.')
def GhostEncounterAttic(solaire_meetings, inventory):
    if solaire_meetings==3:
        print(f'\"Well my friend, these talks with yoy have given this old man a big pile of happiness I\'d say.\n'
              f'I\'d like to present to you this gift, a beautiful doll, given to me by a strong woman in a clocktower.\"\n'
              f'\nSolaire has given you a doll, to see its description, press \'i\' to open the inventory.')
        item='doll'
        inventory[item]=object_descriptions[item]
        room_objects['Solaire Quest']['in_inventory'] = True
    if solaire_meetings==1:
        print(
              f'\n\"Ah, hello! You don\'t look Hollow, far from it!\n'
              f'I am Solaire of Astora, an adherent of the Lord of Sunlight. Or at least I was.\n'
              f'\nI see you\'re confused, don\'t worry, I\'m not a normal ghost, or I hope I don\'t become one soon\n'
              f'Hah Hah Hah!\"'
              )
    elif solaire_meetings==2:
        print(f'\"I see that you are still confused, if you wish, I can tell you the story of\n'
              f'this strange Haunted Mansion. Maybe knowing the story behind all this will help you find a way out.\n'
              f'Hah Hah Hah!\"(y/n)\n')
        answer = input('> ')
        while answer != 'y' and answer != 'n':
            print(f'\"My friend I asked to tell you the story, nothing else...\"')
            answer = input('> ')
        if answer == 'y':
            print(f'\"Very well, the Mansion was funded a millennia ago by a profound nobleman known as Ludwig.\n'
                  f'He was a fine swordsman with powers unlike human knowledge. His skills surpassed even those '
                  f'of a mage.\n As scary as it sounds, he was actually a quite nice guy, he built this manor to serve'
                  f'as refuge for those lost in the madness of nightmares.\n However, during the last hundred years '
                  f'after his passing, Ludwig\'s killer, the Hunter, is the chief of this manor. \n'
                  f'During his reign he\'s allowed any and all beasts to roam the manor, without caring about the'
                  f'repercussions.\n And so, if you wish to fight the hunter, I must advise against it, for he is a man'
                  f'worshiped like a god. A ruthless killer.\"')
        elif answer=='n':
            print('\"Well, if you change your mind and want to hear the story, let me know,\n'
                  'or maybe you don\'t need the story to get out of here.\n'
                  'Hah Hah Hah!\"')
    elif solaire_meetings>3:
        print(f'Do you wish for me to repeat any of our conversations? I know it\'s a lot to take in, I\'d be glad to ' 
        f'help\nPress "1" for Solaire to reintroduce himself.\nPress "2" to hear about the manor\'s history\n'
        f'Press "3" to hear about the doll\'s backstory.\n'
        f'Press "4" to listen to Solaire\'s advice\n'
        f'\nPress any other key to exit this menu.\n')
        answer=input('> ')
        if answer=='1':
            print(
                f'\n\"Ah, hello! You don\'t look Hollow, far from it!\n'
                f'I am Solaire of Astora, an adherent of the Lord of Sunlight. Or at least I was.\n'
                f'\nI see you\'re confused, don\'t worry, I\'m not a normal ghost, or I hope I don\'t become one soon\n'
                f'Hah Hah Hah!\"\n'
            )
        elif answer=='2':
            print(f'\"Very well, the Mansion was funded a millennia ago by a profound nobleman known as Ludwig.\n'
                  f'He was a fine swordsman with powers unlike human knowledge. His skills surpassed even those '
                  f'of a mage.\n As scary as it sounds, he was actually a quite nice guy, he built this manor to serve'
                  f'as refuge for those lost in the madness of nightmares.\n However, during the last hundred years '
                  f'after his passing, Ludwig\'s killer, the Hunter, is the chief of this manor. \n'
                  f'During his reign he\'s allowed any and all beasts to roam the manor, without caring about the '
                  f'repercussions.\n And so, if you wish to fight the hunter, I must advise against it, for he is a man'
                  f'worshiped like a god. A ruthless killer.\"\n')
        elif answer=='3':
            print(f'\"Well my friend, these talks with yoy have given this old man a big pile of happiness I\'d say.\n'
                  f'I\'d like to present to you this gift, a beautiful doll, given to me by a strong woman in a clocktower.\"')
        elif answer=='4':
            print(f'What advice do you want to hear?\n'
                  f'Press "1" to hear about a ragged map.\n'
                  f'Press "2" to hear about the experience of Solaire.\n'
                  f'Press "3" to hear a secret.\n'
                  f'Press any other key to exit this menu.\n')
            response=input('> ')
            if response=='1':
                print('"I remember an old friend of mine also got stuck in this manor once, he created a map and place it on the Grand Hall\'s walls.\n'
                  'If you find yourself lost traveling the manor, I suggest you claim it for yourself.\n'
                  'Unless of course you love labrynth exploring. Hah Hah Hah!"')
            elif response=='2':
                print('"With the experience I have exploring these halls, I recommend that you examine each room you visit,\n'
                      'you never know when you will find an item that will serve you in the least expected moments."')
            elif response=='3':
                print('\"If you hear the story about this manor, let me tell you that a sacred treasure is found in one of these rooms.\n'
                      "This treasure belonged to Ludwig, the founder of this manor. But let me tell you that just finding it is not enough to take it,\n"
                      "you need several attributes before you can use such a sacred treasure.\"\n"
                      '\nDo you want to ask Solaire for more information about Ludwig\'s sacred treasure? (y/n)')
                response=input('> ')
                if response=='y':
                    print(f'Ha ha ha! I see that you are very interested in the topic, however, I have no more information about Ludwig\'s treasure..\n'
                          f'But don\'t be discouraged, I trust that you can find a way to get hold of Ludwig\'s treasure, maybe even the doll\n'
                          f'that I gave you, as proof of our friendship, is something key to said treasure... but don\'t get me wrong, that\'s just a guess.\n'
                          f'Hah Hah Hah!')
                else:
                    return
            else:
                return

        else:
            return

def GhostEncounterHallway():
    print('You see a beautiful maid brushing the floor. Her clothes are filthy from cleaning the manor.\n'
          '"My, what have we here, a guest. Please, help yourself to the bedroom ahead.\n'
          'Oh, but be careful! The floor in front of you is slippery." (Use "f" key to move forward slowly)')
    movement = input('> ')
    if movement == 'f':
        print('Thank you sir, I will clean your footsteps shortly. :)')
    elif movement == 't':
        print('You may help yourself to the room ahead, but be careful, the floor is wet and slippery.')
    else:
        print('You fell...\n\"Oh my, geez sir, are you okay? Worry not about the mess, it is my duty to clean it.\"')

def GhostEncounterCount(a,b,c,d,e,f):
    all_encounters = (a, b, c, d, e, f)
    counter = 0
    for i in all_encounters:
        if i:
            counter += 1
    return counter

def ClaimTheSword(a):
    if a >= 5 and room_objects['Solaire Quest']["in_inventory"]:
        room_objects['Guest Bedroom']["availability"] = True

def HunterEncounter():
    print('... silence falls upon the room... then, from the darkness, you hear footsteps getting near.\n'
          'He stops with the moonlight barely shining upon his figure, revealing a tall man wearing a thief\'s mask.\n'
          'Your gaze falls to his hands, where you see he holds a strange scythe...\n'
          'The Mere sight is enough to send a cold shiver down your spine. \n'
          'You now know you must find a way to survive his hunt.')
    # This will now print the boss fight controls.
    print(
        "\t\tCombat commands:\n"
        "\t'a' = Attack with sword or without.\n"
        "\t't' = Turn around and run away from the room.\n"
        "\t'd' = Dodge the hunter's attacks.\n"
        "\t'c' = Drink the Bubbling Potion\n"
        "\t'h' = Drink a Healing Potion (Estus Flask)\n"
        "Note: If you decide to fight, you are not allowed to run away beyond that point."
    )
    action = input('☼>')
    hunter_moves = {
        'Dodge': 'The hunter has dodged your move but lost his footing, press "a" again to attack',
        'Parry': 'Your blades have clashed and sparks are flying across the air. \n'
                 'However, the hunter prepares for an attack.',
        'Attack': 'In the blink of an eye, the hunter\'s blade is about to kill you.You must dodge quickly to survive.'
    }
    if action not in ('a', 't', 'd', 'c', 'h'):
        print(f'YOU DIED! ')
        exit()
    hunter_health=100
    player_health=100
    player_damage=5
    player_drank_bubbling=False
    if room_objects['Guest Bedroom']["in_inventory"]:
        player_damage=20
        if player_drank_bubbling:
            player_damage=30

    if action=='c':
        if room_objects['Cellar']['in_inventory']:
            player_drank_bubbling=True

