import pygame
from Char import Char
from Char import Perso 
from Creature import Creature
from Stairs import Stairs
import const
import sys

def afficher(sol, fenetre, player):
    floor = Char(pygame.image.load(const.image_sol).convert())
    hero = Char(pygame.image.load(const.image_hero).convert())
    monster = Char(pygame.image.load(const.image_monsters).convert())
    stairs = Char(pygame.image.load(const.image_stairs).convert())
    num_ligne = 0
    for ligne in sol:
        num_case = 0
        for sprite in ligne:
            x = num_case * 30
            y = num_ligne * 30
            if sprite == '.':		   
                fenetre.blit(floor.image, (x,y))
            elif sprite == player :
                fenetre.blit(hero.image, (x,y))
            elif isinstance(sprite, Creature):
                fenetre.blit(monster.image, (x,y))
            elif isinstance(sprite, Stairs):
                fenetre.blit(stairs.image, (x,y))

            num_case += 1
        num_ligne += 1

def initialisation():
    pygame.init()
    # Background
    background = pygame.image.load("assets/bg.jpg")

    # Window
    pygame.display.set_icon(pygame.image.load("assets/icone.png"))
    pygame.display.set_caption("Window")

    window = pygame.display.set_mode((1080, 720))

    return window, background

def refresh(window, background):
    running = True
        # Background
    window.blit(background, (0, 0))

    # Update
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user exits the window
            running = False
    
   


    return running


def interact():
    
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        

        elif event.type == pygame.KEYDOWN:
            return event.unicode
            
            
    

    

    




