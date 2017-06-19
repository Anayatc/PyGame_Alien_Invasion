import sys
import pygame


def run_game():
    pygame.init()
    game_display = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

run_game()
