import pygame

pygame.init()

# Window
pygame.display.set_icon(pygame.image.load("assets/icone.png"))
pygame.display.set_caption("Window")

window = pygame.display.set_mode((1080, 720))

# Background
background = pygame.image.load("assets/bg.jpg")

running = True
while running:
    # Background
    window.blit(background, (0, 0))

    # Update
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user exits the window
            running = False