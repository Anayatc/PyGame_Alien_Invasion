import sys
import pygame
from settings import Settings


def run_game():
    pygame.init()
    game_display = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (100, 100, 100)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        game_display.fill(bg_color)
        pygame.display.update()

run_game()
