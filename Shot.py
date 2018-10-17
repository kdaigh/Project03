## @file shot.py
#  Source file for shot object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

import pygame
from pygame.locals import *
from player.Ship import Ship
pygame.init()

##The shots from the enemy and player ships
class Shot(object):
    ##Constructor
    def __init__(self):
        self.rect.centerx = Ship.rect.centerx
        self.rect.top = Ship.rect.top - 5

        ##Loading shot image, needs an image
        self.shot = pygame.image.load("images/player_ship.png")

    #updates the shot as it moves upward across the screen, speed can be moved.
    def update(self):
        self.rect.top = self.rect.top - 10