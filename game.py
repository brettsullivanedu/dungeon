import pygame
from characters.player import Player
from states.game_state_manager import GameStateManager
from states.intro_state import IntroState
from states.menu_state import MenuState
from states.select_class_state import SelectClassState
from states.in_game_state import InGameState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_manager = GameStateManager(self)

        # Initialize and add game states
        self.state_manager.add_state('intro', IntroState(self))
        self.state_manager.add_state('menu', MenuState(self))
        self.state_manager.add_state('select_class', SelectClassState(self))
        self.state_manager.add_state('in_game', InGameState(self))
        self.state_manager.change_state('intro')

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.state_manager.update(events)
            self.screen.fill((0, 0, 0))  # Clear the screen
            self.state_manager.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

