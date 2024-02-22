import pygame

class Player:
    def __init__(self, image_path, start_pos, screen_size):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image =  pygame.transform.scale(self.original_image, (32,32)) # Load player sprite
        self.pos = start_pos
        self.speed = 5
        self.screen_size = screen_size
        self.lantern_size = 150  # Radius of the lantern light

    def move(self, dx=0, dy=0):
        # Update player position based on movement, ensuring the player doesn't go out of bounds
        self.pos[0] = max(0, min(self.screen_size[0] - self.image.get_width(), self.pos[0] + dx * self.speed))
        self.pos[1] = max(0, min(self.screen_size[1] - self.image.get_height(), self.pos[1] + dy * self.speed))

    def draw(self, screen):
        # Draw the player sprite
        screen.blit(self.image, self.pos)
        # Create a lighting effect for the lantern
        self.create_lantern_light(screen)
        

    def create_lantern_light(self, screen):
        # Create a "darkness" surface that covers the entire screen
        mask_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        mask_surface.fill((0, 0, 0, 180))  # Semi-transparent black

        # Create a "light" circle that will act as the hole in the mask
        light_surface = pygame.Surface((self.lantern_size*2, self.lantern_size*2), pygame.SRCALPHA)
        pygame.draw.circle(light_surface, (0, 0, 0, 0), (self.lantern_size, self.lantern_size), self.lantern_size)

        # Position the light circle on the mask
        mask_surface.blit(light_surface, (self.pos[0] + self.image.get_width()/2 - self.lantern_size, self.pos[1] + self.image.get_height()/2 - self.lantern_size), special_flags=pygame.BLEND_RGBA_MIN)

        # Apply the mask to the screen
        screen.blit(mask_surface, (0, 0))

