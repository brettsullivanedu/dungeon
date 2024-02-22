# Assuming pygame is already imported and initialized
import pygame


class Room:
    def __init__(self, room_type):
        self.room_type = room_type
        self.background_image = pygame.image.load(self.get_background_path())

    def get_background_path(self):
        # Define the path for each room type's background image
        background_paths = {
            'treasure': 'assets/backgrounds/treasure1.jpg',
            'trap': 'assets/backgrounds/trap1.jpg',
            'enemy': 'assets/backgrounds/encounter1.jpg',
            'empty': 'assets/backgrounds/empty1.jpg',
            'boss': 'assets/backgrounds/exit.jpg',
        }
        return background_paths.get(self.room_type, 'assets/backgrounds/empty.jpg')

    def draw(self, screen, position):
        # Draw the background image to the screen
        screen.blit(self.background_image, position)

    def interact(self, player):
        if self.room_type == 'treasure':
            print("You found a treasure! It's added to your inventory.")
            # Add treasure to the player's inventory (to be implemented)
        elif self.room_type == 'trap':
            print("Oh no, it's a trap! You lose some health.")
            # Deduct health from the player (to be implemented)
        elif self.room_type == 'enemy':
            print("An enemy appears! Time for combat.")
            # Initiate combat (to be implemented)
        elif self.room_type == 'boss':
            print("The boss room! Brace yourself for a tough fight.")
            # Initiate boss fight (to be implemented)
        else:
            print("An empty room. Take a moment to rest.")
        # Mark the room as visited or trigger any other state changes