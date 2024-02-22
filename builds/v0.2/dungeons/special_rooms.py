# dungeons/special_rooms.py
from .rooms import Room
from characters.enemy import Goblin, Ogre, Dragon  # Assuming these are defined in the characters.enemy module
import random

class TreasureRoom(Room):
    def enter(self, player):
        print("You've found a treasure!")
        player.collect_treasure()

class TrapRoom(Room):
    def enter(self, player):
        print("It's a trap! You take damage.")
        player.trigger_trap()

class PuzzleRoom(Room):
    def enter(self, player):
        print("You've encountered a puzzle.")
        player.solve_puzzle()

class EnemyRoom(Room):
    def __init__(self, description="You've encountered an enemy!", is_boss=False):
        super().__init__(description)
        self.is_boss = is_boss
        self.enemy = self.spawn_enemy()

    def spawn_enemy(self):
        if self.is_boss:
            return Dragon()
        else:
            return random.choice([Goblin(), Ogre()])

    def enter(self, player):
        print(self.description)
        player.fight_enemy(is_boss=self.is_boss)
