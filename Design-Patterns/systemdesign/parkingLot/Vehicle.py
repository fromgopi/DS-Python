class Vehicle:
    def __init__(self, wheel_number, type):
        self._type = type
        self._wheel_number = wheel_number

    def get_type(self):
        return self._type

    def get_wheel_number(self):
        return self._wheel_number
