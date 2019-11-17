from designpatterns.creational.abstractPattern.abstract_doors.doors import Door


class IronDoor(Door):
    """Iron door class extending Door."""

    def get_description(self):
        """
        Overridden method which gives description of Iron door.
        :return: None
        """
        print("This Iron door.")

