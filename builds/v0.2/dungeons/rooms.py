# dungeons/room.py

class Room:
    def __init__(self, description="An empty room"):
        self.description = description

    def enter(self, player):
        print(self.description)
        # This method should be overridden in subclasses to implement specific room interactions
