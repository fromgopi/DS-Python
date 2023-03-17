from door_state import DoorState
from close import CloseState

class OpenState(DoorState):
    def open_state(self):
        print("The door is already open")
        return self
    
    def close_state(self):
        print("Closing the door...")
        return CloseState()