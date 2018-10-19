## @file enemy.py
#  Source file for enemy object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

from actor import Actor
from globals import *
import random
import constants as const

## @class Enemy
#  @brief Implements Actor base class as Enemy object
class Enemy(Actor):

    ## TO DO
    ## Constructor
    def __init__(self, image):
        Actor.__init__(self, image)
        self.hit = False
        self.direction = random.randrange(-1, 2) * const.ENEMY_SPEED
        if self.direction > 0:
            self.rect.left = screen.left
        else:
            self.rec.right = screen.right
        # For now we are not letting enemies reload



    ## TO DO
    ## Function to update the enemy
    def update(self):
        self.rect[0] = self.rect[0] + self.direction
        if not screen.contains(self.rect):
            self.direction = - self.direction
            self.rect.top = self.rect.bottom + 10
            self.rect = self.rect.clamp(screen)
