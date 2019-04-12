class Rooms(object):
    def __init__(self, name, north=None, south=None, west=None, east=None, description="", up=None, down=None,
                 items=None):
        if items is None:
            items = []
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.description = description
        self.up = up
        self.down = down
        self.items = items


class rangedweapon(object):
    def __init__(self, name, instructions, ammo):
        self.name = name
        self.instructions = instructions
        self.ammo = ammo


class melee(object):
    def __init__(self, name, instructions, durability):
        self.name = name
        self.instructions = instructions
        self.durability = durability


class healing(object):
    def __init__(self, name, instructions, healingpoints):
        self.name = name
        self.instructions = instructions
        self.healingpoints = healingpoints


class supplies(object):
    def __init__(self, name, instructions, throw):
        self.name = name
        self.instructions = instructions
        self.throw = throw


class WrittenPaper(supplies):
    def __init__(self, read, name, instructions, value):
        super(WrittenPaper, self).__init__(name, value, instructions)
        self.read = read


class Airpods(supplies):
    def __init__(self, use, name, value, instructions):
        super().__init__(name, value, instructions)
        self.use = use


class Medkit(healing):
    def __init__(self, use, name, instructions, healingpoints):
        super().__init__(name, instructions, healingpoints)
        self.use = use


class Bandage(healing):
    def __init__(self, use, name, instructions, healingpoints):
        super().__init__(name, instructions, healingpoints)
        self.use = use


class Soda(healing):
    def __init__(self, use, name, instructions, healingpoints):
        super().__init__(name, instructions, healingpoints)
        self.use = use


class Candybar(healing):
    def __init__(self, use, name, instructions, healingpoints):
        super().__init__(name, instructions, healingpoints)
        self.use = use


class Nerfgun(rangedweapon):
    def __init__(self, cockit, shoot, reload, name, value, instructions):
        super().__init__(name, value, instructions)
        self.cockit = cockit
        self.shoot = shoot
        self.reload = reload


class Lantern(supplies):
    def __init__(self, on, off, name, value, instructions):
        super().__init__(name, value, instructions)
        self.on = on
        self.off = off


class WinnieThePoohPlushie(supplies):
    def __init__(self, throw, name, value, instructions):
        super().__init__(name, value, instructions)
        self.throw = throw


class Flashlight(supplies):
    def __init__(self, on, off, name, value, instructions):
        super().__init__(name, value, instructions)
        self.on = on
        self.off = off


class Baseball(rangedweapon):
    def __init__(self, throw, name, instructions, ammo):
        super().__init__(name, instructions, ammo)
        self.throw = throw


class Woodenbat(melee):
    def __init__(self, swing, throw, name, instructions, ammo):
        super().__init__(name, instructions, ammo)
        self.swing = swing
        self.throw = throw


class Screwdriver(supplies):
    def __init__(self, use, throw, name, instructions, ammo):
        super().__init__(name, instructions, ammo)
        self.throw = throw
        self.use = use


class AirSoftPistol(rangedweapon):
    def __init__(self, reload, shoot, name, instructions, ammo):
        super().__init__(name, instructions, ammo)
        self.reload = reload
        self.shoot = shoot


class Crowbar(melee):
    def __init__(self, name, instructions, durability, swing, throw):
        super().__init__(name, instructions, durability)
        self.swing = swing
        self.throw = throw


class Shield(supplies):
    def __init__(self, durability, name, instructions, throw):
        super().__init__(name, instructions, throw)
        self.durability = durability


class Fireaxe(melee):
    def __init__(self, swing, throw, name, instructions, durability):
        super().__init__(name, instructions, durability)
        self.swing = swing
        self.throw = throw


class Keycard(supplies):
    def __init__(self, use, name, instructions, throw):
        super().__init__(name, instructions, throw)
        self.use = use


key_card = Keycard("unlock", "Generic keycard", "Push 3 then push P to take it out", False)
fire_axe = Fireaxe(True, True, "an emergency axe", "Push 1 then the p button to take out the axe push o to swing", 50)
shield = Shield(100, "A police riot shield", "push 1 The L button to take out the shield", True)
crow_bar = Crowbar(" Its a crowbar", "push 1 then M to take out the crowbar push o to swing", 75, True, True)
pistol = AirSoftPistol(True, True, "its my airsoftgun", "Push 2 then p to take it out o to shot", 12)
screw_driver = Screwdriver(True, True, "Its a security guards screw driver", "push 3 then k to take it out o  to swing"
                                                                             "", False)
wooden_bat = Woodenbat(True, True, "A baseball players bat?", "Push 1 then N to take it out o to swing", False)
base_ball = Baseball(True, "Its the Baseball for the bat", "Push 2 then L to take it out", False)
flash_light = Flashlight(False, True, "Its a flashlight", 20, "Push 3 then f then o to turn on push o again to turn off"
                         )
winnie_plushie = WinnieThePoohPlushie(True, "WinnieThePooh", 5, "push 3 then m to take out then o to throw")
lantern = Lantern(False, True, "An old lantern from a shop", 40, "Push 3 then n to take out then o to turn on")
nerf_gun = Nerfgun(True, True, True, "A Mega X", 3, "Push 2 then b to take out then o to shoot r to reload then to cock"
                                                    "it")
candy_bar = Candybar(True, "A candy bar", "Push 4 then p to take out then o to use", 5)
soda = Soda(True, "Its a soda bottle", "Pus 4 then l to take out o to use", 10)
bandage = Bandage(True, "Its seems to be a bandage", "Push 4 then m to take out o to use", 15)
med_kit = Medkit(True, "some kind of healing object", "Push 4 then n to take out then o to use", 100)
air_pods = Airpods(True, "On the ad out side its called airpods?", -100, "Push 3 then q to take out o to use")
written_paper = WrittenPaper(True, "Paper with writing", "G to grab then r to read", 5)

inventory = []


class Character(object):
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage


class deadly_creature(object):
    def __init__(self, starting_location):
        self.current_location = starting_location


class Player(object):
    def __init__(self, starting_location, ):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This method moves a character to a new location
        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


R19A = Rooms('This is the safe room', None, None, None, None, "There's some items in the room type search to see them"
             " ,now type take to take the item you want with the number of said item then "
             "type inventory", None, None, [written_paper, wooden_bat])
parking_lot = Rooms('The parking lot', None, None, None, None, "Its the destroyed parking lot but it has a bad felling"
                                                               " with it", None, None, [winnie_plushie])
high_way = Rooms('Its the high way', None, None, None, None, "Its the highway with crashed vehicles everywhere there's"
                 "nowhere else to go,there's something dark in the corner of my eye its  staring at me i cant move like"
                 " there's a presence around me", None, None, [flash_light])

parking_lot_2 = Rooms('The other part of the parking lot', None, None, None, None, "another parking lot area, I turn"
                      " to leave but a sharp pain hits my back everything goes black : Dead")

parking_lot_3 = Rooms('Its the other part of the parking lot', None, None, None, None, "Its another parking area but "
                      "there's a crashed bus up north", None, None, [key_card])

bus = Rooms('Its a crashed bus', None, None, None, None, "Its A crashed bus the corpse of the bus driver is very bloody"
            " i turn away so i don't throw up but weird enough there's no animals near it like fly's over the smell of "
            "it, its abnormal", None, None, [screw_driver]
            )
mall_hallway = Rooms('The mall hallway', None, None, None, None, "Its the malls destroyed and empty hallway I have a "
                     "bad feeling with this", None, None, [nerf_gun])

apple_store = Rooms('Its the Apple store', None, None, None, None, "Its the apple store and the ad for the new air pods"
                    "is still up", None, None, [air_pods])

food_court = Rooms('Its the food court', None, None, None, None, "Its food court a once happy and expensive place"
                   "that smelled really good is now abandoned and has an awful smell with it", None, None,
                   [candy_bar, soda])

hallway_room_2 = Rooms('Its another hallway', None, None, None, None, "Its the second hallway its basically the same "
                       "as the first one but has a bad feeling with it something is watching me", None, None,
                       [crow_bar])

game_stop = Rooms('The game stop', None, None, None, None, "Its a gamestop with many ads about black ops 4")

macys = Rooms('Its the Macys', None, None, None, None, "Its the macys it looks destroyed and bad like its been raided",
              None, None, [fire_axe])

macys_room_2 = Rooms('Its the second floor', None, None, None, None, "Its the second floor of the macys but looks worse"
                     " and smells like blood", [med_kit])

build_a_bear = Rooms('Its a build a bear', None, None, None, None, "Its a build a bear this is where i took my kids,"
                     "wait what happened to them?", None, None, [base_ball])

hallway_room_3 = Rooms('Its the final hallway', None, None, None, None, "its the last hallway of this darn place"
                       "its looks more peaceful but there's marks on the floor like someone was walking here,"
                       "recently", None, None, [shield])

hollister = Rooms('Its the hollister', None, None, None, None, "its the hollister but looks broke down like the "
                  "business went out for decades, how long was i out?", None, None, [Bandage])

in_n_out = Rooms('Its the in n out burger joint', None, None, None, None, "Its the in n out burger smells...good?"
                 "there's no one here but why does it smell good", None, None, [pistol])

managers_office = Rooms('Its the managers office', None, None, None, None, "Its the managers office the cameras show"
                        "what happened to everyone and everything to see how everyone died but most importantly what" 
                        "happened to my daughter and son... I don't see them but i see that those creatures i saw they"
                        "murdered everyone and there's not only 3 there's seems to be more than what we could've "
                        "handled, i look to see that there's a camera in this place...im not alone there was no way to "
                        "escape i stand still awaiting my fate: You win Game over", None, None, None)

R19A.south = parking_lot
R19A.north = mall_hallway
parking_lot.south = R19A
parking_lot.north = parking_lot_2
parking_lot.west = high_way
parking_lot.east = parking_lot_3
parking_lot_3.north = bus
parking_lot_3.south = parking_lot
bus.south = parking_lot_3
high_way.south = parking_lot
mall_hallway.south = R19A
mall_hallway.north = apple_store
mall_hallway.west = food_court
mall_hallway.east = hallway_room_2
apple_store.south = mall_hallway
food_court.south = mall_hallway
hallway_room_2.south = mall_hallway
hallway_room_2.west = game_stop
hallway_room_2.east = build_a_bear
hallway_room_2.north = macys
game_stop.south = hallway_room_2
build_a_bear.south = hallway_room_2
macys.south = hallway_room_2
macys.north = hallway_room_3
macys.up = macys_room_2
macys_room_2.down = macys
hallway_room_3.north = managers_office
hallway_room_3.south = macys
hallway_room_3.east = hollister
hallway_room_3.west = in_n_out
hollister.south = hallway_room_3
in_n_out.south = hallway_room_3


player = Player(R19A)
deadly_creature = deadly_creature(parking_lot_2)

playing = True
directions = ['north', 'south', 'west', 'east', 'up', 'down']
short_directions = ['n', 's', 'w', 'e', 'u', 'd']


while playing:
    # print(player.current_location)
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            if room_name is None:
                raise AttributeError
            player.move(room_name)
        except AttributeError:
            print("This path does not exist")
        except KeyError:
            print("I can't go that way.")
    elif command.lower() in ["search"]:
        if len(player.current_location.items) > 0:
            print()
            print("The following items are in the room: ")
            for num, item in enumerate(player.current_location.items):
                print(str(num + 1) + ": " + item.name)
        else:
            print("There are no items in the room.")
    elif command.lower() in ["inventory", "I"]:
        Item = 0
        for i in player.inventory:
            print(player.inventory[Item].name)
            Item += 1
    elif "take" in command:
        choice = input("what will you pick up: ")

        number = int(choice)
        if len(player.current_location.items) >= number > 0:
            player.inventory.append(player.current_location.items[number - 1])
            player.current_location.items.pop(number - 1)

        print("The item is in your inventory")
        print()
    elif "drop" in command:
        choice = input("What will you drop:")

        number = int(choice)
        if len(player.current_location.items) > 0:
            player.current_location.items.append((player.inventory[number - 1]))
            player.inventory.pop(number - 1)
    else:
        print("Command Not Recognized")
    print()
