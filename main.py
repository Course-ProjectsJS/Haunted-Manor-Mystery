from project import (ProcessCommand, room_descriptions, GhostEncounterGardenRoom,
                     GhostEncounterLibraryRoom, GhostEncounterDinningRoom, GhostEncounterKitchen,GhostEncounterAttic,
                     ClaimTheSword,GhostEncounterCount,GhostEncounterHallway,HunterEncounter)

def Main():
    current_room = 'Grand Hall'
    inventory = {}
    ghost_encountered_dining_room = False
    ghost_encountered_library_room = False
    ghost_encountered_garden_room = False
    ghost_encountered_kitchen = False
    solaire_encountered_attic = False
    solaire_meetings=0
    ghost_encountered_hallway = False
    hunter_encountered=False
    hiding = False

    print(room_descriptions[current_room])

    while True:
        command = input("> ")
        current_room, hiding = ProcessCommand(command, current_room, inventory, hiding)

        ClaimTheSword(GhostEncounterCount(ghost_encountered_dining_room, ghost_encountered_library_room,
                                          not solaire_encountered_attic, ghost_encountered_garden_room,
                                          ghost_encountered_kitchen, ghost_encountered_hallway))

        if current_room == 'Dining Room' and not ghost_encountered_dining_room:
            GhostEncounterDinningRoom()
            ghost_encountered_dining_room = True
        if current_room == 'Library' and not ghost_encountered_library_room:
            GhostEncounterLibraryRoom()
            ghost_encountered_library_room = True
        if current_room == 'Garden' and not ghost_encountered_garden_room:
            GhostEncounterGardenRoom(inventory)
            ghost_encountered_garden_room = True
        if current_room == 'Kitchen' and not ghost_encountered_kitchen:
            GhostEncounterKitchen()
            ghost_encountered_kitchen = True
        if current_room == 'Attic' and not solaire_encountered_attic:
            if command=='t':
                solaire_meetings += 1
                GhostEncounterAttic(solaire_meetings, inventory)
            if solaire_meetings==0:
                print(f'\nYou found a very peculiar ghost, different from the others.\n'
                  f'\nPress \'t\' to talk to him')
            else:
                print(
                      f'\nPress \'t\' to talk to Solaire of Astrora')
        if current_room == 'Hallway' and not ghost_encountered_hallway:
            GhostEncounterHallway()
            ghost_encountered_hallway = True
        if current_room == 'Master Bedroom' and not hunter_encountered:
            HunterEncounter()
            hunter_encountered = True
print("Welcome to the Haunted Manor Mystery!\n")
print('To escape the Manor you have two options, either gather 5 objects and leave through the main entrance\n'
      'or, you could kill the Hunter and end this nightmare by leaving through the front door.\n'
      'We recommend caution, there are many enemies that could kill you or steal your stuff.\n'
      '\nTo view the commands, press \'m\'.\n')
Main()