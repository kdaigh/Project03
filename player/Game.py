import pygame
from pygame.locals import *
pygame.init()
from main import Ship

# setting window size
screen = pygame.display.set_mode((900, 600))
# label window
pygame.display.set_caption("Py Five")

bg = pygame.image.load("space.jpg")
screen.blit(bg, (0,0))

playing = Ship(450,410,64,64,screen,bg)
while 1:
    playing.controls()
