import pygame
from player import Player
from states.combat_state import CombatState
from states.ingame_state import InGameState
from states.intro_state import IntroState
from states.menu_state import MenuState
from states.select_class_state import SelectClassState

from states.state_manager import GameStateManager
from states.story_state import StoryState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.state_manager = GameStateManager()
        self.player = Player("hero.jpg", [700, 500], self.screen.get_size())

        # Initialize all states
        self.state_manager.add_state("intro", IntroState(self))
        self.state_manager.add_state("menu", MenuState(self))
        self.state_manager.add_state("story", StoryState(self))
        self.state_manager.add_state("select_class", SelectClassState(self))
        self.state_manager.add_state("in_game", InGameState(self))
        self.state_manager.add_state("combat", CombatState(self, self.state_manager))
        # Add other states here

        self.state_manager.change_state("intro")
    
    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                            # Inside your game loop
                keys = pygame.key.get_pressed()  # Get the state of all keyboard buttons
                dx, dy = 0, 0
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    dx -= 1
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    dx += 1
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    dy -= 1
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    dy += 1

                self.player.move(dx, dy)

            self.state_manager.update(events)
            self.state_manager.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    
            

if __name__ == "__main__":
    game = Game()
    game.run()
