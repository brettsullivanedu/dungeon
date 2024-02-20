from states.MenuState import MenuState
from states.DungeonState import DungeonState
from states.CombatState import CombatState
import pickle

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.state = MenuState(self)

    def change_state(self, new_state):
        self.state = new_state

    def to_dungeon(self):
        self.change_state(DungeonState(self))

    def to_combat(self):
        self.change_state(CombatState(self))

    def to_menu(self):
        self.change_state(MenuState(self))

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw(self.screen)

    def save_game(self):
        with open('savegame.pkl', 'wb') as f:
            pickle.dump(self.state, f)

    def load_game(self):
        with open('savegame.pkl', 'rb') as f:
            self.state = pickle.load(f)
