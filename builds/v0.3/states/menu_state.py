import pygame
from components.Buttons import Button
from states.state import State

class MenuState(State):
    def __init__(self, game):
        super().__init__(game)
        self.buttons = [
            Button("Start Game", (350, 200), (100, 50), self.start_game),
            Button("Load Game", (350, 260), (100, 50), self.load_game),
            Button("Quit", (350, 320), (100, 50), self.quit_game)
        ]

    def start_game(self):
        # Placeholder for starting the game
        print("Start Game")

    def load_game(self):
        # Placeholder for loading a game
        print("Load Game")

    def quit_game(self):
        pygame.quit()
        exit()

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.handle_event(event)

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        for button in self.buttons:
            button.draw(screen)

    def start_game(self):
        self.game.state_manager.change_state("story")