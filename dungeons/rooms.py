# dungeons/room.py
class Room:
    def __init__(self, description):
        self.description = description

    def enter(self, player):
        raise NotImplementedError("This method must be overridden by subclasses.")
