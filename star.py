import pygame
from pygame.sprite import Sprite
from random import randint
random_number = randint(-1,1)

class Star(Sprite):
    def __init__(self, ai_game):
        """set the beginning position of the stars initially"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # loading stars and set the rect properties
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # every star be in the left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # horizon of star
        self.x = float(self.rect.x)
