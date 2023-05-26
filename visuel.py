import pygame
from Char import Char
import const

def afficher(sol, fenetre):
    mur = pygame.image.load(const.image_sol).convert()
    num_ligne = 0
    for ligne in sol:
        num_case = 0
        for sprite in ligne:
            x = num_case * 30
            y = num_ligne * 30
            if sprite == '.':		   
                fenetre.blit(mur, (x,y))
            num_case += 1
        num_ligne += 1



# Window
pygame.display.set_icon(pygame.image.load("assets/icone.png"))
pygame.display.set_caption("Window")

window = pygame.display.set_mode((1080, 720))

# Background
background = pygame.image.load("assets/bg.jpg")

# Hero
hero = Char(10, pygame.image.load("assets/hero.png"))
