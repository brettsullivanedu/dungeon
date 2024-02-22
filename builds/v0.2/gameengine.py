# gameengine.py

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.states = {}  # Initialize an empty dictionary for states
        self.current_state = None

    def register_state(self, name, state):
        """Register a new state with the game engine."""
        self.states[name] = state

    def change_state(self, state_name, **kwargs):
        """Change the current state to a different state."""
        # Ensure the current state has an on_exit method and call it
        if self.current_state and hasattr(self.current_state, 'on_exit'):
            self.current_state.on_exit()

        # Retrieve the new state from registered states and call its on_enter method
        new_state = self.states.get(state_name)
        if new_state:
            if hasattr(new_state, 'on_enter'):
                new_state.on_enter(**kwargs)
            self.current_state = new_state
        else:
            print(f"State '{state_name}' not found.")

    def update(self):
        """Update the logic of the current state."""
        if self.current_state and hasattr(self.current_state, 'update'):
            self.current_state.update()

    def draw(self):
        """Draw the visuals of the current state."""
        
        if self.current_state and hasattr(self.current_state, 'draw'):
            self.current_state.draw(self.screen)

    def to_dungeon(self, player):
        # Assume 'player' is an instance of a character class (Warrior, Mage, Rogue)
        if 'dungeon' in self.states:
            self.states['dungeon'].player = player  # Update the player in DungeonState
            self.states['dungeon'].on_enter()  # Re-initialize DungeonState if needed
        self.change_state('dungeon')
