import abc


class VehicleBuilder(object):
    __metadata__ = abc.ABCMeta

    @abc.abstractmethod
    def make_wheels(self):
        pass

    @abc.abstractmethod
    def make_doors(self):
        pass

    @abc.abstractmethod
    def make_seats(self):
        pass
