## @file player.py
#  Source file for player object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

from actor import Actor


## @class Player
#  @brief Implements Actor base class as Player object
class Player(Actor):

    ## Constructor
    def __init__(self, image):
        Actor.__init__(self, self.image)
        self.alive = True
        self.reloading = False
        self.rect.centerx = WINDOW.centerx
        self.rect.bottom = WINDOW.bottom

    ## TO DO
    ## Moves player in a specific direction
    #  @param: direction, coordinates that represent desired move
    def move(self, direction):
        pass