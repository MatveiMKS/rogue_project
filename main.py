<<<<<<< HEAD
from utils import _find_getch
import theGame
from visuel import * 

theGame.theGame().play1()


=======
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

