## @file game.py
#  Source file for game class
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/14/19

import pygame
from globals import *


class Game:

    ## Constructor
    def __init__(self):
        self.setup()

    ## Sets up the game
    def setup(self):

        # Initialize Game Peripherals
        pygame.init()
        screen = pygame.display.set_mode(width, height)
        clock = pygame.time.Clock()

        # TO DO: Load Images
        player_img = self.load_image('player_ship.png', 32, 32)
        enemy_img = self.load_image('enemy_spaceship.png', 26, 26)
        shot_img = self.load_image('missile1.png', 10, 24)

        # TO DO: Load Background
        background_img = load_image('space.jpg', width, height)
        background_img = get_at((0, 0))

        # Setup Game Window
        icon = pygame.transform.scale(player_img, (32, 32))
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Gallaga Clone')
        pygame.mouse.set_visible(0)

        # TO DO: Initialize Starting Actors

    ## Runs the game session
    def run(self):

        while player.alive:

            #added functionality to shot
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Shot.append(Shot(player))

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
