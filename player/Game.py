import pygame
from pygame.locals import *
pygame.init()
from Ship import Ship

# setting window size
screen = pygame.display.set_mode((900, 600))
# label window
pygame.display.set_caption("Py Five")

#setting the background to the starts
bg = pygame.image.load("space.jpg")
screen.blit(bg, (0,0))

#instantiating the ship, you have to put the current screen and the background
#in because the ships movements are covered with the background
playing = Ship(450,410,64,64,screen,bg)

while 1:
    #allows the user to control the ship that was placed
    playing.controls()
