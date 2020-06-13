from abc import ABC, abstractmethod


class Database(ABC):
    """This is concrete Interface."""

    @abstractmethod
    def connection(self):
        """Abstract Method which will allow user to implement it."""
        pass
