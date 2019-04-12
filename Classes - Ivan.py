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
        super(WrittenPaper, self). __init__(name, value, instructions)
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
candy_bar = Candybar(True, "A crunch bar", "Push 4 then p to take out then o to use", 5)
soda = Soda(True, "A sprite bottle", "Pus 4 then l to take out o to use", 10)
bandage = Bandage(True, "A bandage", "Push 4 then m to take out o to use", 15)
med_kit = Medkit(True, "Its a medkit", "Push 4 then n to take out then o to use", 100)
air_pods = Airpods(True, "Apples new air pods", -100, "Push 3 then q to take out o to use")
written_paper = WrittenPaper(True, "Its a paper?", "G to grab then r to read", 5)

