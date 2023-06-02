import pygame
from Char import Char
from Char import Perso 
from Element import Element 
from Stairs import Stairs
from Coord import Coord 
from Map import Map
import const
import sys

def afficher(sol, fenetre, player, elem_type):
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
    affiche_inventory(player, fenetre, elem_type)
    afficher_hp(player, fenetre)

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
            
def affiche_inventory(hero, fenetre, elem_type):
    num_case = 197
    image_inventaire = pygame.transform.scale(pygame.image.load("assets/barre_inventaire.jpg").convert(), (716,104))
    fenetre.blit(image_inventaire ,(180,600))
    for object in hero._inventory:
        image = pygame.transform.scale(Char(pygame.image.load(elem_type[object.name]).convert()).image, (75,75))
        fenetre.blit(image, (num_case,617))
        num_case += 103

def afficher_hp(hero, fenetre):
    image_coeur = pygame.transform.scale(pygame.image.load("assets/coeur.jpg").convert(), (40,40))
    image_coeur_vide = pygame.transform.scale(pygame.image.load("assets/coeur_vide.jpg").convert(), (40,40))
    for heart in range(15):
        if heart + 1 <= hero.hp:
            fenetre.blit(image_coeur, (10, 20 + (heart)*40))
        else:
            fenetre.blit(image_coeur_vide, (10, 20 +(heart)*40))

        


