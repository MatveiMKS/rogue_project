import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self, hp):
        self.hp = hp
        self.image = pygame.image.load("assets/hero.png")
        self.rect = self.image.get_rect()