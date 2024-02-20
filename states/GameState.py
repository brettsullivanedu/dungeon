from abc import ABC, abstractmethod

class GameState(ABC):
    def __init__(self, game_engine):
        self.game_engine = game_engine

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
