import pygame

from states.base_state import BaseState

class SelectClassState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.classes = ["Wizard", "Warrior", "Mage"]
        self.current_selection = 0

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_selection = (self.current_selection - 1) % len(self.classes)
                elif event.key == pygame.K_DOWN:
                    self.current_selection = (self.current_selection + 1) % len(self.classes)
                elif event.key == pygame.K_RETURN:
                    # Logic to select the class and move to the next state
                    print(f"Class selected: {self.classes[self.current_selection]}")
                    self.game.state_manager.change_state("in_game")

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.SysFont(None, 40)
        for index, class_name in enumerate(self.classes):
            if index == self.current_selection:
                text = font.render(class_name, True, (255, 255, 0))
            else:
                text = font.render(class_name, True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, 150 + index * 50))
            screen.blit(text, text_rect)
