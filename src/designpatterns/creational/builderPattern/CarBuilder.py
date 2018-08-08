from src.designpatterns.creational.builderPattern.Vehicle import Vehicle
from src.designpatterns.creational.builderPattern.VehicleBuilder import VehicleBuilder


class CarBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("car ")

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 4

    def make_seats(self):
        self.vehicle.seats = 7
