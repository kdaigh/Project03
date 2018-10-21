## @file player.py
#  Source file for player object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

from actor import Actor
from globals import *
import constants as const


## @class Player
#  @brief Implements Actor base class as Player object
class Player(Actor):

    ## Constructor
    def __init__(self, image):
        Actor.__init__(self, image)
        self.alive = True
        self.reloading = False
        self.rect.centerx = screen.centerx
        self.rect.bottom = screen.bottom

    ## Moves player in a specific direction
    #  @param: direction, coordinates that represent desired move
    def move(self, direction):
        self.rect = self.rect.move(direction * const.PLAYER_SPEED, 0).clamp(screen)
