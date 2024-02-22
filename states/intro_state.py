import pygame
from characters.player import Player
from states.base_state import BaseState

class IntroState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.timer = pygame.time.get_ticks()
        self.duration = 1000  # Duration of the intro in milliseconds
        
    def update(self, events):
        if pygame.time.get_ticks() - self.timer > self.duration:
            self.game.state_manager.change_state("menu")

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.SysFont(None, 55)
        text = font.render("Welcome to the Dungeon Crawler", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        screen.blit(text, text_rect)
