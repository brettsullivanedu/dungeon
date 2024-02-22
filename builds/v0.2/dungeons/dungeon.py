# dungeons/dungeon.py
import random
from .rooms import Room
from .special_rooms import TreasureRoom, TrapRoom, PuzzleRoom, EnemyRoom

class Dungeon:
    def __init__(self, size):
        self.size = size
        self.rooms = [[None for _ in range(size)] for _ in range(size)]
        self.populate_dungeon()

    def populate_dungeon(self):
        for y in range(self.size):
            for x in range(self.size):
                room_choice = random.choice([TreasureRoom, TrapRoom, PuzzleRoom, EnemyRoom])
                self.rooms[y][x] = room_choice()

    def get_room(self, position):
        x, y = position
        return self.rooms[y][x]
