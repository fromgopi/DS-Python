from designpatterns.creational.builderPattern import CarBuilder
from designpatterns.creational.builderPattern import VehicleManufacturer

if __name__ == "__main__":
    manufacture = VehicleManufacturer()
    manufacture.builder = CarBuilder()

    car = manufacture.create()
    car.view()
