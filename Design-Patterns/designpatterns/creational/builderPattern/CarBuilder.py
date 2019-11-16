from designpatterns.creational.builderPattern import Vehicle
from designpatterns.creational.builderPattern import VehicleBuilder


class CarBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("car ")

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 4

    def make_seats(self):
        self.vehicle.seats = 7
