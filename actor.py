## @file actor.py
#  Source file for actor base class
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

import pygame


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

    ## Loads and scales object/game image
    #  @author: Kristi
    #  @pre: image exists
    #  @param: filename, name of image to be loaded
    #  @param: width, desired width of image
    #  @param: height, desired height of image
    #  @returns: Surface object
    def load_image(self, filename, width, height):
        filename = os.path.join('assets/images', filename)
        img = pygame.image.load(filename)
        img = pygame.transform.scale(img, (width, height))
        return img.convert()

