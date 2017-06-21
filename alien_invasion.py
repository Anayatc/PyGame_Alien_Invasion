import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    game_display = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(game_display)

    while True:
        gf.check_events()
        game_display.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.update()

run_game()
