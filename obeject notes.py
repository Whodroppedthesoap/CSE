import Special_Random


class WaterGun(object):
    def __init__(self, capacity, distance=30, stock=False):
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.duration_of_pressure = 5

    def shoot(self, time):
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure")
            elif self.duration_of_pressure < time:
                print("You ran out of pressure after firing for %s seconds",  self.duration_of_pressure)
                self.duration_of_pressure = 0

            else:
                print("You shot for %s seconds" % time)
                self.duration_of_pressure -= time
        else:
            print("There's no trigger")

    def pump_it_up(self):
        self.duration_of_pressure = 5
        print("You pump the tank back to full pressure")


my_water_gun = WaterGun(5.2, 40, True)
your_water_gun = WaterGun(1.0, 1, False)
wiebe_water_gun = WaterGun(999999999999999999, 999999999999999999999999999999999, True)
yahir_water_gun = WaterGun(0.1)

wiebe_water_gun.shoot(5)
wiebe_water_gun.pump_it_up()
wiebe_water_gun.shoot(5)

print(Special_Random.RandomWeibe.special_random())
