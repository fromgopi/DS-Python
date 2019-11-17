from designpatterns.creational.abstractPattern.abstract_doors.doors import DoorFittingExpert


class Carpenter(DoorFittingExpert):

    def get_description(self):
        print("I can only fit wooden doors.")
