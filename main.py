import pygame
import sys
from gameengine import GameEngine

# Initialize PyGame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dungeon Crawler')

def main():
    clock = pygame.time.Clock()
    game_engine = GameEngine(screen)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_engine.update()
        game_engine.draw()

        pygame.display.flip()
        clock.tick(60)  # FPS

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
