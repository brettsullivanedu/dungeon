import pygame

from game import Game

if __name__ == "__main__":
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)
    game = Game(screen)
    game.run()
