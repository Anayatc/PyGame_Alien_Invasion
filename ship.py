import pygame


class Ship():

    def __init__(self, game_display):
        self.game_display = game_display

        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.game_display_rect = game_display.get_rect()

        self.rect.center_x = self.game_display_rect.center_x
        self.rect.bottom = self.game_display_rect.bottom

    def blitme(self):
        self.game_display.blit(self.image, self.rect)
