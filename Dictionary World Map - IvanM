world_map = {
    'R19A': {
        'NAME': "Safe Room",
        'DESCRIPTION': "A basic room with food and supplies with A note on the wall With"
                       " A door On the north and south of you you",
        'PATHS': {
            'NORTH': "MALL_HALLWAY",
            'SOUTH': "PARKING_LOT"
        }
    },

    'MALL_HALLWAY': {
        'NAME': "The Empty HallWay Of a Mall",
        'DESCRIPTION': "The Mall Looks like it in bad shape but i don't know why The south is The Safe room",

        'PATHS': {
            'SOUTH': "R19A",
            'NORTH': "APPLE_STORE",
            'WEST': "FOOD_COURT",
            'EAST': "HALLWAY_ROOM_2"
        }
    },

    'PARKING_LOT': {
        'NAME': "The Destroyed parking lot",
        'DESCRIPTION': "The parking lot is mostly destroyed with cars everywhere",
        'PATHS': {
            'NORTH': "PARKING_LOT_3",
            'SOUTH': "R19A",
            'WEST': "HIGH_WAY",
            'EAST': "PARKING_LOT_ROOM_2"

        }
    },

    'APPLE_STORE': {
        'NAME': "Its the apple store",
        'DESCRIPTION': "Just like the hallway Its abandoned and destroyed red marks everywhere I try not to throw up",
        'PATHS': {
            'SOUTH': "MALL_HALLWAY"
        }
    },

    'FOOD_COURT': {
        'NAME': "The Food court",
        'DESCRIPTION': "Its the food court my favorite place but it smells bad",
        'PATHS': {
            'EAST': "MALL_HALLWAY"
        }
    },

    'HIGH_WAY': {
        'NAME': "The highway",
        'DESCRIPTION': "Its the highway with crashed vehicles everywhere there's nowhere else to go i see something"
                       " staring at me its dark with white eyes i cant move im scared to it runs away ",
        'PATHS': {
            'EAST': "PARKING_LOT"
        }
    },

    'PARKING_LOT_ROOM_2': {
        'NAME': "A different part of the parking lot",
        'DESCRIPTION': "Its Another area of the parking lot you look at a destroyed car with red liquid falling from it"
                       "Your vision starts going dark you hear something speak but you couldn't understand what it said"
                       "you pass out and die"
    },

    'HALLWAY_ROOM_2': {
        'NAME': "A different part of the hallway mall",
        'DESCRIPTION': "Its another area of the mall hallway but it looks worse",
        'PATHS': {
            'NORTH': "MACYS",
            'SOUTH': "MALL_HALLWAY",
            'WEST': "GAME_STOP",
            'EAST': "BUILD_A_BEAR"
        }
    },

    'GAME_STOP': {
        'NAME': "Its a gamestop",
        'DESCRIPTION': "Its my favorite place in the mall but it looks horrible it doesnt look like how i remember it",
        'PATHS': {
            'SOUTH': "HALLWAY_ROOM_2"

}
    },

    'MACYS': {
        'NAME': "Its a macys ",
        'DESCRIPTION': "This place looks rough like a black friday at walmart",
        'PATHS': {
            'SOUTH': "HALLWAY_ROOM_2",
            'NORTH': "HALLWAY_ROOM_3",
            'UP': "MACYS_ROOM_2"
        }
    },

    'BUILD_A_BEAR': {
        'NAME': "A kids build a bear workshop",
        'DESCRIPTION': "Its a build a bear but destroyed bear stuffing is everywhere you see something run by it was a "
                       "creature with white eyes it then leave I look around before leaving",
        'PATHS': {
            'SOUTH': "HALLWAY_ROOM_2"
        }
    },

    'PARKING_LOT_3': {
        'NAME': "Its a parking lot with a crashed bus",
        'DESCRIPTION': "Its a parking lot but i don't have a good feeling about this",
        'PATHS': {
            'SOUTH': "PARKING_LOT",
            'NORTH': "BUS"
        }
    },

    'BUS': {
        'NAME': "Its a bus",
        'DESCRIPTION': "Its a bus but it has rotten corpses within the bus everything seems to be broken ",
        'PATHS': {
            'SOUTH': "PARKING_LOT_3"
        }
    },

    'HALLWAY_ROOM_3': {
        'NAME': "Its the last hallway within the mall",
        'DESCRIPTION': "its the last hallway but there red liquid everywhere and smells horrifying",
        'PATHS': {
            'EAST': "HOLLISTER",
            'SOUTH': "MACYS",
            'WEST': "IN_N_OUT"
        }
    },

    'HOLLISTER': {
        'NAME': "its a hollister",
        'Description': "Its a hollister but nothing seems to be taken it looks good surprisingly",
        'PATHS': {
            'SOUTH': "HALLWAY_ROOM_3"
        }
    },

    'MACYS_ROOM_2': {
        'NAME': "Its the second floor of the Macys",
        'DESCRIPTION': "The second floor of the macys looks horrifying",
        'PATHS': {
            'DOWN': "MACYS"
        }
    },

    'IN_N_OUT': {
        'NAME': "Its an in n out burger",
        'DESCRIPTION': "This place ive never been too but i regret it it smells really good in here",
        'PATHS': {
            'SOUTH': "HALLWAY_ROOM_3"
        }
    }

}
current_node = world_map['R19A']
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True
debug = True

while playing:
    if debug:
        print(world_map['R19A'].keys())
    print(current_node["NAME"])
    command = input(">")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I cant go that way")
    else:
        print("Command not recognized")
