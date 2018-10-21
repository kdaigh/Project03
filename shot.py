## @file shot.py
#  Source file for shot object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

import pygame
from actor import Actor

## @class Shot
#  @brief Implements Actor base class as Shot object
class Shot(Actor):

    ##Constructor
    def __init__(self, image, player):
        Actor.__init__(self, image)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top - 5

    #updates the shot as it moves upward across the screen, speed can be moved.
    def update(self):
        self.rect.top = self.rect.top - 10

    ## Checks for collisions
    def collision_check(self, actor):
        return self.rect.colliderect(actor.rect)