import pygame


class Ship():

    def __init__(self, game_display):
        self.game_display = game_display

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.game_display_rect = game_display.get_rect()

        self.rect.centerx = self.game_display_rect.centerx
        self.rect.bottom = self.game_display_rect.bottom

    def blitme(self):
        self.game_display.blit(self.image, self.rect)
