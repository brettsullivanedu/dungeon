import pygame


class Player:
    def __init__(self, image_path, start_pos, screen_size):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            self.original_image, (32, 32)
        )  # Load player sprite
        self.pos = list(start_pos)  # Convert tuple to list for mutability
        self.screen_size = screen_size
        self.speed = 5
        self.inventory = []  # Example attribute for the player's inventory
        self.health = 100  # Example attribute for the player's health
        self.lantern_size = 150

    def move(self, dx=0, dy=0):
        # Update the player's position, ensuring they stay within bounds
        self.pos[0] += dx * self.speed
        self.pos[1] += dy * self.speed
        self.pos[0] = max(
            0, min(self.screen_size[0] - self.image.get_width(), self.pos[0])
        )
        self.pos[1] = max(
            0, min(self.screen_size[1] - self.image.get_height(), self.pos[1])
        )

    def draw(self, screen, position=None):
        # Implement the lantern light effect around the player
        # Note: This requires the revised lighting effect approach discussed earlier
        # Draw the player
        draw_pos = position if position else self.pos
        screen.blit(self.image, draw_pos)

    def add_to_inventory(self, item):
        # Add an item to the player's inventory
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        # Remove an item from the player's inventory if it exists
        if item in self.inventory:
            self.inventory.remove(item)

    def take_damage(self, amount):
        # Reduce the player's health by the given amount
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        # Handle the player's death
        print("You have died.")
        # Here you can add logic for game over or respawning
