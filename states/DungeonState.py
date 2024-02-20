import random
from states.GameState import GameState
from states.CombatState import CombatState
# Assuming other necessary imports

# Room types: 1 = Empty, 2 = Monster, 3 = Treasure, 4 = Trap, 5 = Puzzle, 6 = Special Event
ROOM_TYPES = {
    "EMPTY": 1,
    "MONSTER": 2,
    "TREASURE": 3,
    "TRAP": 4,
    "PUZZLE": 5,
    "SPECIAL_EVENT": 6
}


class DungeonState(GameState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.dungeon_size = (10, 10)  # Example size, can be adjusted
        self.dungeon_layout = self.generate_dungeon()
        self.player_position = [0, 0]  # Player starts at the entrance

    def generate_dungeon(self):
        layout = [[0 for _ in range(self.dungeon_size[0])] for _ in range(self.dungeon_size[1])]
        # Starting point for the random walk
        x, y = random.randint(0, self.dungeon_size[0] - 1), random.randint(0, self.dungeon_size[1] - 1)
        self.player_position = [x, y]  # Update player start position

        for _ in range(100):  # Steps in the random walk
            layout[y][x] = random.choice([1, 2, 3])  # 1 = Empty, 2 = Monster, 3 = Treasure
            step = random.choice(['up', 'down', 'left', 'right'])
            if step == 'up' and y > 0: y -= 1
            elif step == 'down' and y < self.dungeon_size[1] - 1: y += 1
            elif step == 'left' and x > 0: x -= 1
            elif step == 'right' and x < self.dungeon_size[0] - 1: x += 1

        # Ensure the starting position is empty
        layout[self.player_position[1]][self.player_position[0]] = 1
        return layout
    
    def check_room(self):
        room_type = self.dungeon_layout[self.player_position[1]][self.player_position[0]]
        if room_type == 2:  # Monster encounter
            print("Encountered a monster!")
            self.game_engine.change_state(CombatState(self.game_engine))
        elif room_type == 3:  # Treasure room
            print("Found treasure!")
            # Logic for adding treasure to player inventory

