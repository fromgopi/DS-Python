from abc import ABC, abstractmethod

class DoorState(ABC):
    """_summary_

    Arguments:
        ABC -- _description_
    """
    @abstractmethod
    def open_state(self):
        pass
    
    @abstractmethod
    def close_state(self):
        pass