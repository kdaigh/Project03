## @file game.py
#  Source file for game class
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/14/19

import pygame


class Game:

    ## Constructor
    def __init__(self):
        pass

    ## Sets up the game
    def setup(self):

        # setting window size
        screen = pygame.display.set_mode((900, 600))

        # label window
        pygame.display.set_caption("Py Five")

        #setting the background to the starts
        bg = pygame.image.load('images/space.jpg')
        screen.blit(bg, (0, 0))

    ## Runs the game session
    def run(self):

        pygame.init()

        while 1:
            #added functionality to shot
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Shot.append(Shot(player))
