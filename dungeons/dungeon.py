# dungeons/dungeon.py
from dungeons.rooms import Room
from dungeons.special_rooms import TreasureRoom, TrapRoom, PuzzleRoom
import random

class Dungeon:
    def __init__(self, size):
        self.size = size
        self.rooms = [[None for _ in range(size)] for _ in range(size)]
        self.populate_dungeon()

    def populate_dungeon(self):
        for y in range(self.size):
            for x in range(self.size):
                room_type = random.choice([TreasureRoom, TrapRoom, PuzzleRoom])
                self.rooms[y][x] = room_type("A mysterious room")
