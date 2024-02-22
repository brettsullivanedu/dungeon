import random
from dungeon.rooms.base_room import Room


class Dungeon:
    def __init__(self, size):
        self.size = size  # Size of the dungeon grid (size x size)
        self.grid = [[None for _ in range(size)] for _ in range(size)]  # Dungeon grid initialization
        self.populate_dungeon()

    def populate_dungeon(self):
        """Populate the dungeon grid with rooms of different types."""
        room_types = ['treasure', 'trap', 'enemy', 'empty']
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 and j == 0:
                    self.grid[i][j] = Room('empty')  # Start room
                elif i == self.size - 1 and j == self.size - 1:
                    self.grid[i][j] = Room('boss')  # Boss room at the opposite corner
                else:
                    # Randomly choose room types, with a bias towards 'enemy' rooms.
                    self.grid[i][j] = Room(random.choice(room_types + ['enemy']*2))

    def get_room(self, x, y):
        """Return the room located at the specified coordinates in the grid."""
        return self.grid[y][x]

    def get_possible_moves(self, x, y):
        """Determine possible movement directions from the current room."""
        moves = []
        if x > 0: moves.append('left')
        if x < self.size - 1: moves.append('right')
        if y > 0: moves.append('up')
        if y < self.size - 1: moves.append('down')
        return moves