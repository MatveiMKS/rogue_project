import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self, image, hp=0):
        self.hp = hp
        self.image = image 
        self.rect = self.image.get_rect()


class Perso(Char):

    def __init__(self, image, hp=0, x=0, y=0):
        super().__init__(image, hp)
        
        self.x = x
        self.y = y

    def deplace(self, direction):

        if direction == "up":
            self.y -= 30 
        if direction == "down":
            self.y += 30 
        if direction == "right":
            self.x += 30 
        if direction == "left":
            self.x -= 30 
