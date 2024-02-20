import pygame
from states.GameState import GameState
from states.DungeonState import DungeonState
# Assuming GameState and other imports are correctly set

class MenuState(GameState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.options = ["Start Game", "Load Game", "Exit"]
        self.current_selection = 0

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_selection = (self.current_selection - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.current_selection = (self.current_selection + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.options[self.current_selection] == "Start Game":
            self.game_engine.to_dungeon()
        elif self.options[self.current_selection] == "Exit":
            pygame.quit()
            exit()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        for i, option in enumerate(self.options):
            text = font.render(option, True, (255, 255, 255) if i == self.current_selection else (100, 100, 100))
            screen.blit(text, (100, 50 + 30 * i))
