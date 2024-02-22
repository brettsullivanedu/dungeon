import pygame
from states.base_state import BaseState

class MenuState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.options = ["Start Game", "Load Game", "Quit"]
        self.current_option = 0

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.current_option == 0:
                        self.game.state_manager.change_state("select_class")
                    elif self.current_option == 2:
                        pygame.quit()
                        exit()

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.SysFont(None, 40)
        for index, option in enumerate(self.options):
            if index == self.current_option:
                text = font.render(option, True, (255, 255, 0))
            else:
                text = font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, 150 + index * 50))
            screen.blit(text, text_rect)
