import sys
import random
import pygame

from Char import Char
from Char import Perso 
from Element import Element 
from Stairs import Stairs
from Coord import Coord 
from Map import Map
import theGame
import const

def afficher(sol, fenetre, player, elem_type):
    ''' shows the game on the screen'''
    ##chargement des images
    background = Char(pygame.image.load("assets/bg.jpg").convert())
    fenetre.blit(background.image, (0,0))
    floor_1 = Char(pygame.image.load(const.image_sol).convert())
    floor_2 = Char(pygame.image.load(const.image_sol_2).convert())
    floor_3 = Char(pygame.image.load(const.image_sol_3).convert())
    floor_4 = Char(pygame.image.load(const.image_sol_4).convert())
    floor = {1: [floor_1], 2: [floor_1], 3: [floor_2, floor_3, floor_4]}
    hero = Char(pygame.image.load(const.image_hero).convert_alpha())


    images_hero = const.hero_images_f if theGame.theGame().layout == 'f' else const.hero_images_e
    for num_ligne, ligne in enumerate(sol._mat):
        num_case = 0
        for sprite in ligne:
            x = num_case * 30
            y = num_ligne * 30

            pile = []
            for room in sol._rooms: #check if the player is in the room
                if sol.pos(player) in room and Coord(x/30, y/30) in room:
                    pile.append((x,y))

            if (sol.pos(player).distance(Coord(x/30,y/30)) < 4) or (x,y) in pile or (x,y) in sol.loaded:
                if sprite != ' ':
                    random.seed((x**y)*(x+y))
                    indx = random.randint(1,3)
                    fenetre.blit(random.choice(floor[indx]).image, (x+240, y+15))
                if sprite == player:
                    if player.sens in (['z','q', 's', 'd'] if theGame.theGame().layout == 'f' else ['w','a', 's', 'd']):

                        fenetre.blit(pygame.image.load(images_hero[player.sens]).convert_alpha(), (x+240, y+15))
                    else:
                        fenetre.blit(hero.image, (x+240, y+15))

                elif isinstance(sprite, Element) and ((x,y) in pile or (x,y) in sol.loaded):
                    fenetre.blit(Char(pygame.image.load(elem_type[sprite.name]).convert_alpha()).image, (x+240, y+15))
                sol.loaded.append((x,y))
                
            num_case += 1
        num_ligne += 1
    affiche_inventory(player, fenetre, elem_type)
    afficher_hp(player, fenetre)
    afficher_messages(fenetre, theGame.theGame()._messages)
    afficher_armure(fenetre, player)
    afficher_arme(fenetre, player)

def initialisation():
    ''' initializes the window and the background'''
    pygame.init()
    # Background
    background = pygame.image.load("assets/bg.jpg")

    # Window
    pygame.display.set_icon(pygame.image.load("assets/icone.png"))
    pygame.display.set_caption("Window")
    window = pygame.display.set_mode((1080, 720))
    return window, background

def refresh(window, background):
    ''' refreshes the window'''
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
    ''' waits for the user to press a key and returns the key pressed'''
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            return event.unicode

def affiche_inventory(hero, fenetre, elem_type):
    ''' shows the inventory on the screen'''
    image_inventaire = pygame.image.load("assets/barre_inventaire.jpg").convert()
    fenetre.blit(image_inventaire, (900,116))
    for num_case, elements in enumerate(hero._inventory):
        image = pygame.transform.scale(Char(pygame.image.load(elem_type[elements.name]).convert_alpha()).image, (72,72))
        fenetre.blit(image, (904 if num_case < 6 else 948, 120 + num_case*80))

def afficher_hp(hero, fenetre):
    ''' shows the hp on the screen'''
    image_coeur =\
    pygame.transform.scale(pygame.image.load("assets/coeur.png").convert_alpha(), (40,40))

    image_coeur_vide =\
    pygame.transform.scale(pygame.image.load("assets/coeur_vide.png").convert_alpha(), (40,40))
    image_coeur = Char(image_coeur).image
    image_coeur_vide =Char(image_coeur_vide).image
    for heart in range(hero.hp_max):
        if heart + 1 <= hero.hp:
            fenetre.blit(image_coeur, (10, 20 + (heart)*40))
        else:
            fenetre.blit(image_coeur_vide, (10, 20 +(heart)*40))

def afficher_messages(fenetre, messages):
    ''' shows the messages on the screen'''
    size = 20 if len(messages) < 3 else 15
    font = pygame.font.Font(None, size)
    for i, el in enumerate(messages):
        text = font.render(el, 1, (255, 255, 255))
        fenetre.blit(text, (290, 660 + i*15))

def afficher_armure(fenetre, hero):
    ''' shows the armor on the screen'''
    image_armure = const.images_armure
    for armure in hero.armors:
        image = image_armure[armure][hero.armors[armure][1]]
        #image_armure[armure] => dictionary of the armor piece
        #[hero.armors[armure][1]] => its material
        fenetre.blit(pygame.image.load(image).convert_alpha(), (125, 20 if armure == 'head'
                             else 85 if armure == 'chest'
                             else 160 if armure == 'legs'
                             else 240))
    afficher_armure_points(fenetre, hero)
        
def afficher_armure_points(fenetre, hero):
    '''show the armor points on the screen'''
    image_armure = pygame.transform.scale(pygame.image.load(const.image_armure_points).convert_alpha(), (40,40))
    for armure in range(hero.armor):
        fenetre.blit(image_armure, (70, 20 + (armure)*40))

def afficher_arme(fenetre, hero):
    '''show the weapons used on the screen'''
    if hero.equipments != "barehands":
        image_weapon = \
            pygame.transform.scale(pygame.image.load(const.elem_type[hero.equipments]).convert_alpha(), (70,70))
        fenetre.blit(image_weapon, (125, 310))


