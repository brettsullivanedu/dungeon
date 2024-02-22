import pygame

from states.state import State


class SelectClassState(State):
    def __init__(self, game):
        super().__init__(game)
        self.options = ["Wizard", "Warrior", "Mage"]
        self.current_selection = 0  # Index of the currently selected option
        self.font = pygame.font.Font(None, 48)

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.current_selection = (self.current_selection + 1) % len(self.options)
                elif event.key == pygame.K_UP:
                    self.current_selection = (self.current_selection - 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_class()

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        for i, option in enumerate(self.options):
            if i == self.current_selection:
                color = (255, 255, 0)  # Highlight the selected option
            else:
                color = (255, 255, 255)
            text_surf = self.font.render(option, True, color)
            text_rect = text_surf.get_rect(center=(screen.get_width() / 2, 100 + i * 60))
            screen.blit(text_surf, text_rect)

    def select_class(self):
        chosen_class = self.options[self.current_selection]
        print(f"Chosen class: {chosen_class}")
        # Here, proceed to the next state, e.g., the dungeon exploration state
        # This could be something like: self.game.state_manager.change_state("dungeon_exploration")
        self.game.state_manager.change_state("in_game")
