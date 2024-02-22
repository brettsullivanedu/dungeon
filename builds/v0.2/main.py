import pygame

from states.GameStateManager import GameStateManager
from states.MenuState import MenuState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.state_manager = GameStateManager()

        # Initialize all states
        self.state_manager.add_state("menu", MenuState(self))
        # Add other states here

        self.state_manager.change_state("menu")

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.state_manager.update(events)
            self.state_manager.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
