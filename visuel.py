import pygame
from Char import Char
from Char import Perso 
from Element import Element 
from Stairs import Stairs
from Coord import Coord 
from Map import Map
import const
import sys
import random
import copy


def afficher(sol, fenetre, player, elem_type):
    floor_1 = Char(pygame.image.load(const.image_sol).convert())
    floor_2 = Char(pygame.image.load(const.image_sol_2).convert())
    floor_3 = Char(pygame.image.load(const.image_sol_3).convert())
    floor_4 = Char(pygame.image.load(const.image_sol_4).convert())
    floor = {1: [floor_1], 2: [floor_1], 3: [floor_2, floor_3, floor_4]}
    hero = Char(pygame.image.load(const.image_hero).convert())
    num_ligne = 0
    for ligne in sol._mat:
        num_case = 0
        for sprite in ligne:
            x = num_case * 30
            y = num_ligne * 30
            if sprite == '.' and (sol.pos(player).distance(Coord(x/30,y/30)) < 5):
                random.seed((x**y)*(x+y))
                indx = random.randint(1,3)   
                fenetre.blit(random.choice(floor[indx]).image, (x+240, y+15))
            elif sprite == player :
                fenetre.blit(hero.image, (x+240, y+15))
            elif isinstance(sprite, Element) and (sol.pos(player).distance(Coord(x/30,y/30)) < 5):
                fenetre.blit(Char(pygame.image.load(elem_type[sprite.name]).convert()).image, (x+240, y+15))
                
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
    num_case = 120
    image_inventaire = pygame.image.load("assets/barre_inventaire.jpg").convert()
    fenetre.blit(image_inventaire, (900,116))
    for object in hero._inventory:
        image = pygame.transform.scale(Char(pygame.image.load(elem_type[object.name]).convert()).image, (72,72))
        fenetre.blit(image, (904 if num_case < (6 *80 +120) else 948, num_case))
        num_case += 80

def afficher_hp(hero, fenetre):
    image_coeur = pygame.transform.scale(pygame.image.load("assets/coeur.png").convert_alpha(), (40,40))
    image_coeur_vide = pygame.transform.scale(pygame.image.load("assets/coeur_vide.png").convert_alpha(), (40,40))
    image_coeur = Char(image_coeur).image
    image_coeur_vide =Char(image_coeur_vide).image
    for heart in range(hero.hp_max):
        if heart + 1 <= hero.hp:
            fenetre.blit(image_coeur, (10, 20 + (heart)*40))
        else:
            fenetre.blit(image_coeur_vide, (10, 20 +(heart)*40))
