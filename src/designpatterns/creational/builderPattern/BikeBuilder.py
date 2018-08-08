from src.designpatterns.creational.builderPattern.Vehicle import Vehicle
from src.designpatterns.creational.builderPattern.VehicleBuilder import VehicleBuilder


class BikeBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("Bike")

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2
