## @file enemy.py
#  Source file for enemy object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

from actor import Actor
from globals import *
import constants

## @class Enemy
#  @brief Implements Actor base class as Enemy object
class Enemy(Actor):

    ## TO DO
    ## Constructor
    def __init__(self, image):
        Actor.__init__(self, image)
        self.hit = False
        # For now we are not letting



    ## TO DO
    ## Function to update the enemy
    def update(self):
        global screen
        if not screen.contains(self.rect):
            self.rect = self.rect.clamp(screen)
