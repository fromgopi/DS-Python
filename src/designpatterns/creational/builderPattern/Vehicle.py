class Vehicle(object):

    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

        def view(self):
            print(
                "This vehicle is a " +
                self.type +
                " with; " +
                str(self.wheels) +
                " wheels, " +
                str(self.doors) +
                " doors, and " +
                str(self.seats) +
                " seats."
            )
