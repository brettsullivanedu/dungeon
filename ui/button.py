import pygame


class Button:
    def __init__(self, position, size, text, callback, image = None):
        self.position = position
        self.size = size
        self.text = text
        self.callback = callback
        self.image = image  # Store the image
        if self.image:
            # Scale the image to fit the button size
            self.image = pygame.transform.scale(self.image, self.size)

    def draw(self, screen):
        if self.image:
            # If an image is provided, blit it at the button's position
            screen.blit(self.image, self.position)
        else:
            # Fallback to drawing a rectangle and text if no image is provided
            pygame.draw.rect(screen, (100, 100, 200), (*self.position, *self.size))
            if self.text:
                font = pygame.font.SysFont(None, 32)
                text_surf = font.render(self.text, True, (255, 255, 255))
                text_rect = text_surf.get_rect(center=(self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] // 2))
                screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.position[0] <= event.pos[0] <= self.position[0] + self.size[0] and \
               self.position[1] <= event.pos[1] <= self.position[1] + self.size[1]:
                self.callback()  # Trigger the callback function