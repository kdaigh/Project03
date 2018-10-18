## @file actor.py
#  Source file for actor base class
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

import pygame
import os.path
import constants as const


## @class Actor
#  @brief Abstract base class for game actors
class Actor:

    ## Constructor
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()

    ## Abstract method; Updates actor in frame
    def update(self):
        pass

    ## TO DO
    ## Draws the actor into the screen
    def draw(self, screen):
        pass

    ## TO DO
    ## Removes the actor from the screen
    def erase(self, screen, background):
        pass


