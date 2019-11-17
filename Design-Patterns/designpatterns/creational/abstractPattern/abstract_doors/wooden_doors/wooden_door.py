from designpatterns.creational.abstractPattern.abstract_doors.doors import Door


class WoodenDoor(Door):
    """Wooden Door overriding Door."""
    def get_description(self):
        """
        Overridden method which gives description about door.
        :return: None.
        """
        print("This is wooden door.")
