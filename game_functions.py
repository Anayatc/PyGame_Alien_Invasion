import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, game_display, ship):
    game_display.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.update()