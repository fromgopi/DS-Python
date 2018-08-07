from src.designpatterns.creational.builderPattern.CarBuilder import CarBuilder
from src.designpatterns.creational.builderPattern.VehicleManufacturer import VehicleManufacturer


class BuilderPatterDemo():

    if __name__ == "__main__":
        manufacture = VehicleManufacturer()
        manufacture.builder = CarBuilder()

        car = manufacture.create()
        car.view()
