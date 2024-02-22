class GameStateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name, state):
        self.states[state_name] = state

    def change_state(self, state_name):
        if self.current_state:
            self.current_state.exit_state()
        self.current_state = self.states[state_name]
        self.current_state.enter_state()

    def update(self, events):
        if self.current_state:
            self.current_state.update(events)

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)
