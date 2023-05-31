import pygame
from Char import Char
from Char import Perso 
from Element import Element 
from Stairs import Stairs
from Coord import Coord 
from Map import Map
import const
import sys

def afficher(sol, fenetre, player):
    elem_type = {"Goblin" : const.image_monsters,
                 "Blob" : const.image_monsters,
                 "Bat" : const.image_monsters,
                 "Ork" : const.image_monsters,
                 "Dragon" : const.image_monsters,
                 "small potion": const.image_potion,
                 "medium potion": const.image_potion,
                 "big potion": const.image_potion,
                 "gold": const.image_gold,
                 "Stairs": const.image_stairs,
                 "bow": const.image_bow}
    
    floor = Char(pygame.image.load(const.image_sol).convert())
    hero = Char(pygame.image.load(const.image_hero).convert())
    num_ligne = 0
    for ligne in sol._mat:
        num_case = 0
        for sprite in ligne:
            x = num_case * 30 
            y = num_ligne * 30
            if sprite == '.' and (sol.pos(player).distance(Coord(x/30,y/30)) < 5):		   
                fenetre.blit(floor.image, (x,y))
            elif sprite == player :
                fenetre.blit(hero.image, (x,y))
            elif isinstance(sprite, Element) and (sol.pos(player).distance(Coord(x/30,y/30)) < 5):
                fenetre.blit(Char(pygame.image.load(elem_type[sprite.name]).convert()).image, (x,y))
                
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
            
#def inventory(hero):
    #for object 


    

    

    




