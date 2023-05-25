import pygame
from Char import Char

pygame.init()

# Window
pygame.display.set_icon(pygame.image.load("assets/icone.png"))
pygame.display.set_caption("Window")

window = pygame.display.set_mode((1080, 720))

# Background
background = pygame.image.load("assets/bg.jpg")

# Hero
hero = Char(10)

running = True
while running:
    # Background
    window.blit(background, (0, 0))

    # Hero
    window.blit(hero.image, hero.rect)

    # Update
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user exits the window
            running = False
    
    press = pygame.key.get_pressed()
    if press[pygame.K_RIGHT]:
        hero.rect.x += 0.5

#