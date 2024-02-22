from abc import ABC, abstractmethod

class GameState(ABC):
    def __init__(self, game_engine):
        self.game_engine = game_engine

    @abstractmethod
    def update(self):
        """
        Update the state's logic.
        """
        pass

    @abstractmethod
    def draw(self, screen):
        """
        Draw the state's visuals to the screen.
        """
        pass

    def on_enter(self, **kwargs):
        """
        Called when transitioning into this state. Use this method to handle any
        initialization or setup required for the state, such as resetting variables,
        starting music, or placing the player character.

        :param kwargs: A dictionary of keyword arguments relevant to the state initialization,
                       allowing for flexible state setup based on dynamic context.
        """
        pass

    def on_exit(self):
        """
        Called when transitioning out of this state. Use this method to perform any necessary
        cleanup, such as saving state data, stopping music, or cleaning up resources.
        """
        pass
