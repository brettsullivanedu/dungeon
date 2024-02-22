import pygame
from characters.player import Player
from dungeon.dungeon import Dungeon
from states.base_state import BaseState
from ui.button import Button


class InGameState(BaseState):
    def __init__(self, game):
        """Initialize the in-game state, setting up the dungeon, player, and UI components."""
        super().__init__(game)
        self.initialize_state()

    def initialize_state(self):
        """Initializes the game state components."""
        self.dungeon = Dungeon(5)
        self.player = Player(
            "assets/sprites/hero.jpg", (0, 0), self.game.screen.get_size()
        )
        self.current_room_pos = [0, 0]
        self.font = pygame.font.Font(None, 36)
        self.load_assets()
        self.setup_ui()

    def load_assets(self):
        """Loads necessary assets for the game state."""
        self.arrow_images = {
            "right": pygame.image.load("assets/ui/arrow_right.png").convert_alpha(),
            "left": pygame.image.load("assets/ui/arrow_left.png").convert_alpha(),
            "up": pygame.image.load("assets/ui/arrow_up.png").convert_alpha(),
            "down": pygame.image.load("assets/ui/arrow_down.png").convert_alpha(),
        }

    def setup_ui(self):
        """Sets up UI components including action buttons and directional arrows."""
        self.setup_ui_buttons()
        self.setup_directional_arrows()

    def setup_ui_buttons(self):
        self.ui_buttons = [
            Button(
                (100, self.game.screen.get_height() * 2 // 3 + 50),
                (200, 50),
                "Explore",
                self.explore_action,
            ),
            Button(
                (100, self.game.screen.get_height() * 2 // 3 + 110),
                (200, 50),
                "Inventory",
                self.inventory_action,
            ),
            Button(
                (100, self.game.screen.get_height() * 2 // 3 + 170),
                (200, 50),
                "Rest",
                self.rest_action,
            ),
        ]

    def setup_directional_arrows(self):
        room_height = self.game.screen.get_height() * 2 // 3
        arrow_size = (50, 50)
        self.directional_buttons = {
            "right": Button(
                (self.game.screen.get_width() - arrow_size[0] - 10, room_height // 2),
                arrow_size,
                "",
                self.move_right,
                image=self.arrow_images["right"],
            ),
            "left": Button(
                (10, room_height // 2),
                arrow_size,
                "",
                self.move_left,
                image=self.arrow_images["left"],
            ),
            "up": Button(
                (self.game.screen.get_width() // 2, 10),
                arrow_size,
                "",
                self.move_up,
                image=self.arrow_images["up"],
            ),
            "down": Button(
                (self.game.screen.get_width() // 2, room_height - arrow_size[1] - 10),
                arrow_size,
                "",
                self.move_down,
                image=self.arrow_images["down"],
            ),
        }

    def explore_action(self):
        print("Exploring the room...")
        room = self.dungeon.get_room(*self.current_room_pos)
        room.interact(self.player)

    def inventory_action(self):
        print("Opening inventory...")

    def rest_action(self):
        print("Resting...")

    def move_right(self):
        self.move_player(1, 0)

    def move_left(self):
        self.move_player(-1, 0)

    def move_up(self):
        self.move_player(0, -1)

    def move_down(self):
        self.move_player(0, 1)

    def move_player(self, dx, dy):
        """Updates the player's position in the dungeon grid."""
        new_x = self.current_room_pos[0] + dx
        new_y = self.current_room_pos[1] + dy
        if 0 <= new_x < self.dungeon.size and 0 <= new_y < self.dungeon.size:
            self.current_room_pos = [new_x, new_y]
            self.explore_action()  # Automatically interact with the new room

    def update(self, events):
        """Processes events and updates the game state."""
        for event in events:
            if event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                self.handle_event(event)

    def handle_event(self, event):
        """Handles a single event."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_buttons = self.ui_buttons + list(self.directional_buttons.values())
            for button in all_buttons:
                button.handle_event(event)

    def draw(self, screen):
        """Draws the game state to the screen, including the room, player, and UI."""
        top_section_height = int(screen.get_height() * 2 / 3)
        bottom_section_height = screen.get_height() - top_section_height

        self.draw_current_room(screen, top_section_height, bottom_section_height)
        self.draw_ui(screen, top_section_height, bottom_section_height)

    def draw_current_room(self, screen, top_section_height, bottom_section_height):
        # Draw the room's background scaled to the top two-thirds of the screen
        room = self.dungeon.get_room(*self.current_room_pos)
        room_background_scaled = pygame.transform.scale(
            room.background_image, (screen.get_width(), screen.get_height())
        )
        screen.blit(room_background_scaled, (0, 0))
        # Draw the player at the center of the top section
        player_x = screen.get_width() // 2 - self.player.image.get_width() // 2
        player_y = top_section_height // 2 - self.player.image.get_height() // 2
        self.player.draw(screen, (player_x, player_y))

    def draw_ui(self, screen, top_section_height, bottom_section_height):
        # Draw a white rectangle for the UI in the bottom third
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (0, top_section_height, screen.get_width(), bottom_section_height),
        )

        """Draws UI components."""
        for button in self.ui_buttons + list(self.directional_buttons.values()):
            button.draw(screen)

    def handle_input(self, event):
        # Handle keyboard input for non-UI actions here
        pass
