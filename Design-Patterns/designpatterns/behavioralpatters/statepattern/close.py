import door_state as ds
import open as o
class CloseState(ds.DoorState):
    def open_state(self):
        print("Opening the door")
        return o.OpenState()
    
    def close_state(self):
        print("Doors are already closed")
        return self