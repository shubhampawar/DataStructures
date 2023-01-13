import random


class car:
    def __init__(self):
        self.speed = random.Random()

    def accelerate(self):
        print("speeding up")

    def pull_brakes(self):
        print("applyong brakes")

    def assign_drier(self):
        print("aassingning driver")


class bike():
    def __init__(self):
        self.speed = random.Random()

    def throttling(self):
        print("speeding up bike")

    def apply_brakes(self):
        print("applyong brakes")

    def assign_rider(self):
        print("aassingning rider")


class Bike_adapter:
    def __init__(self,obj):
        self.bike = obj

    def accelerate(self):
        self.bike.throttling()

    def pull_brakes(self):
        self.bike.apply_brakes()

    def assign_drier(self):
        self.bike.assign_rider()


if __name__ == "__main__":
    car = car()
    bike = bike()
    bike_adapter = Bike_adapter(bike)

    car.accelerate()
    car.pull_brakes()
    car.assign_drier()

    bike_adapter.accelerate()



