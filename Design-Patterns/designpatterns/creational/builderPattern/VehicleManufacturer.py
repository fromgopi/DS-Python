
class VehicleManufacturer(object):

    def __init__(self):
        self.builder = None

    def create(self):
        assert not self.builder is None, "No defined Builder"
        self.builder.make_wheels()
        self.builder.make_doors()
        self.builder.make_seats()

        return self.builder.vehicle
