import pygame
from states.BaseState import State

class MenuState(State):
    def enter_state(self):
        print("Entering Menu State")

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state("select_class")

    def draw(self, screen):
        screen.fill((0, 20, 0))  # Black background
        # Add more drawing code here


