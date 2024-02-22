
import pygame
from states.state import State


class CombatState(State):
    def __init__(self, game, state_manager):
        super().__init__(game)
        self.state_manager = state_manager  # Store the state_manager reference

    def enter_state(self):
        print("Entering Combat State")

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state_manager.change_state("menu")  # Use state_manager to change states

    def draw(self, screen):
        screen.fill((222, 0, 0))  # Black background
        # Add more drawing code here
