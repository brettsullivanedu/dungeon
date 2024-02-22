import pygame

from states.state import State


class StoryState(State):
    def __init__(self, game):
        super().__init__(game)
        self.text = """A long time ago in a dungeon far,\nfar away....

It is a period of civil war. Rebel\nspaceships, striking from a hidden\nbase, have won their first victory\nagainst the evil Galactic Empire.

During the battle, Rebel spies managed\nto steal secret plans to the Empire's\nultimate weapon, the PIG STAR, an\narmored space station with enough\npower to destroy an entire planet.

Pursued by the Empire's sinister agents,\nPrincess Leia races home aboard her\nstarship, custodian of the stolen plans\nthat can save her people and restore\nfreedom to the galaxy...."""
        self.text_pos_y = self.game.screen.get_height()
        self.font = pygame.font.Font(None, 36)
        self.skip_text = self.font.render("Press any key to skip...", True, (255, 255, 255))
        self.skip_text_pos = (10, self.game.screen.get_height() - 30)
        self.running = True

    def update(self, events):
        self.text_pos_y -= 0.5  # Speed of text scrolling
        if self.text_pos_y < -1000 or not self.running:  # Arbitrary end point or skip
            self.game.state_manager.change_state("select_class")
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.running = False  # Stop the scrolling to change state

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Clear screen with black
        rendered_text = self.render_fading_text(self.text, self.text_pos_y)
        for i, line in enumerate(rendered_text):
            screen.blit(line, (100, self.text_pos_y + i*40))
        screen.blit(self.skip_text, self.skip_text_pos)

    def render_fading_text(self, text, pos_y):
        """Render text with a fading effect based on its position."""
        lines = text.split('\n')
        rendered_lines = []
        for line in lines:
            alpha = 255
            # Adjust alpha based on position to create fading effect
            if pos_y < 200:
                alpha = max(0, int(255 * (pos_y / 200.0)))
            elif pos_y > self.game.screen.get_height() - 200:
                alpha = max(0, int(255 * ((self.game.screen.get_height() - pos_y) / 200.0)))
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_surface.set_alpha(alpha)
            rendered_lines.append(text_surface)
        return rendered_lines
