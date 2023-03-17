from close import CloseState


class Door:
    def __init__(self) -> None:
        self.current_state = CloseState()
        
    def change_state(self, state):
        self.current_state = state
    
    def open(self):
        self.change_state(self.current_state.open_state())
        
    def close(self):
        self.change_state(self.current_state.close_state())