import pygame
from states.state import State  # Assuming you have a base State class

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)  # Draw the wall with white color


class InGameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.game.player.pos = [20, game.screen.get_height() - 60]  # Bottom left position
        self.walls = [
            Wall(100, 100, 200, 20),
            Wall(300, 200, 20, 100),
            # Add more walls here to create your maze
        ]

    def enter_state(self):
        # Any setup needed when entering the in-game state
        pass

    def exit_state(self):
        # Any cleanup or saving before leaving this state
        pass

    def update(self, events):
        # Update game logic, player movement, etc.
        for event in events:
            if event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                
                # Predict the player's next position
                next_pos = self.game.player.pos.copy()
                next_pos[0] += dx * self.game.player.speed
                next_pos[1] += dy * self.game.player.speed
                
                # Check if the next position collides with any wall
                next_rect = self.game.player.image.get_rect(topleft=next_pos)
                if not any(wall.rect.colliderect(next_rect) for wall in self.walls):
                    self.game.player.move(dx, dy)


    def draw(self, screen):
        screen.fill((0, 0, 0))  # Fill screen with black
        # Temporary surface to apply lantern effect
        temp_surface = pygame.Surface(screen.get_size())
        temp_surface.fill((0,0,0))
        temp_surface.set_colorkey((0,0,0))
        for wall in self.walls:
            wall.draw(temp_surface)  # Draw the wall
        self.game.player.draw(temp_surface)  # Draw the player on the temp surface

        # Apply lantern effect
        lantern_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.circle(lantern_surface, (0, 0, 0, 255), (int(self.game.player.pos[0] + self.game.player.image.get_width()/2), int(self.game.player.pos[1] + self.game.player.image.get_height()/2)), self.game.player.lantern_size)
        temp_surface.blit(lantern_surface, (0,0), special_flags=pygame.BLEND_RGBA_SUB)
        
        screen.blit(temp_surface, (0,0))  # Draw the player on the screen
