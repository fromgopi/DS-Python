from door_state import DoorState
from open import OpenState

class CloseState(DoorState):
    def open_state(self):
        print("Opening the door")
        return OpenState()
    
    def close_state(self):
        print("Doors are already closed")
        return self