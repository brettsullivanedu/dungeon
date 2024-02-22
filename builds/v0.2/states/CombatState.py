import pygame
from states.BaseState import State

class CombatState(State):
    def enter_state(self):
        print("Entering Combat State")

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state("combat_state")

    def draw(self, screen):
        screen.fill((20, 50, 0))  # Black background
        # Add more drawing code here
    
