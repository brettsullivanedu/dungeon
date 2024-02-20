# dungeons/special_rooms.py
from dungeons.rooms import Room

class TreasureRoom(Room):
    def enter(self, player):
        print("You've found a treasure!")

class TrapRoom(Room):
    def enter(self, player):
        print("It's a trap! You take damage.")
        player.take_damage(20)

class PuzzleRoom(Room):
    def enter(self, player):
        print("You've encountered a puzzle.")
