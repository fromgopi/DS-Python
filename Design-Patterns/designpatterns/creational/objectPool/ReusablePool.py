from .Reusable import Reusable


class ReusablePool:
    """
    Manage Reusable objects for use by Client objects.
    """

    def __init__(self, size=5):
        """
        Reusable Pool Constructor
        :param size: size of the Object Pool.
        """
        self._reusables = [Reusable() for _ in range(size)]

    def acquire(self):
        """
        Function to acquire the resource from the pool.
        :return: None
        """
        return self._reusables.pop()

    def release(self, reusable) -> list:
        """
        Function to replace the resource back into the object Pool.
        :param reusable: Instance of the Reusable class.
        :return:
        """
        self._reusables.append(reusable)
        return self._reusables
