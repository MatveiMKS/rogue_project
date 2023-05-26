import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self, hp, image):
        self.hp = hp
        self.image = image 
        self.rect = self.image.get_rect()