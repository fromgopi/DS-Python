from designpatterns.creational.abstractPattern.abstract_doors.doors import DoorFittingExpert


class Welder(DoorFittingExpert):
    def get_description(self):
        print("I can fit only Iron doors.")