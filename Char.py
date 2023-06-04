''' This file contains the classes for the pygame sprites'''

import pygame

class Char(pygame.sprite.Sprite):
    ''' class for the elements of the game'''
    def __init__(self, image, hp=0):
        self.hp = hp
        self.image = image 
        self.rect = self.image.get_rect()


class Perso(Char):
    ''' class for the player'''
    def __init__(self, image, hp=0, x=0, y=0):
        super().__init__(image, hp)
 
        self.x = x
        self.y = y

    def deplace(self, direction):
        ''' moves the player 1 cell in the direction given'''
        if direction == "up":
            self.y -= 30 
        elif direction == "down":
            self.y += 30 
        elif direction == "right":
            self.x += 30 
        elif direction == "left":
            self.x -= 30 
