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
    def __init__(self):
        # TO DO: call to Actor constructor
        self.alive = True
        self.reloading = False
        # TO DO: set initial coordinates

    ## TO DO
    ## Moves player in a specific direction
    #  @param: direction, coordinates that represent desired move
    def move(self, direction):
        pass