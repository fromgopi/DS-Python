import door_state as ds
import  close as c

class OpenState(ds.DoorState):
    def open_state(self):
        print("The door is already open")
        return self
    
    def close_state(self):
        print("Closing the door...")
        return c.CloseState()