from utils import _find_getch
import theGame
from visuel import * 


getch = _find_getch()
theGame.theGame().play2()

pygame.init()

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

    if press[pygame.K_DOWN]:
        hero.rect.y += 0.5
