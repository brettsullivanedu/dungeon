import pygame

from states.state import State

class IntroState(State):
    def __init__(self, game):
        super().__init__(game)
        self.timer = 0  # Timer for the intro duration
        self.intro_duration = 1 * 1000  # 5 seconds

    def enter_state(self):
        self.timer = pygame.time.get_ticks()

    def update(self, events):
        current_time = pygame.time.get_ticks()
        if current_time - self.timer > self.intro_duration:
            self.game.state_manager.change_state("menu")

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        font = pygame.font.Font(None, 74)
        text = font.render("Intro Animation", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(text, text_rect)
