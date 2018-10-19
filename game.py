## @file game.py
#  Source file for game class
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/14/19

import pygame
import os.path
from player import Player
from enemy import Enemy
from shot import Shot
from globals import *


class Game:

    ## Constructor
    def __init__(self):
        pass


    ## Loads and scales object/game image
    #  @author: Kristi
    #  @pre: image exists
    #  @param: filename, name of image to be loaded
    #  @param: width, desired width of image
    #  @param: height, desired height of image
    #  @returns: Surface object
    def load_image(self, filename, file_width, file_height):
        filename = os.path.join('assets/images', filename)
        img = pygame.image.load(filename)
        img = pygame.transform.scale(img, (file_width, file_height))
        return img.convert()


    ## TO DO: Project 4
    ## Sets up the game
    def setup(self):
        pass


    ## Runs the game session
    def run(self):

        # Initialize Game Peripherals
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()

        # TO DO: Load Images
        player_img = self.load_image('player_ship.png', 32, 32)
        enemy_img = self.load_image('enemy_spaceship.png', 26, 26)
        shot_img = self.load_image('missile1.png', 10, 24)

        # TO DO: Load Background
        background_img = pygame.image.load('assets/images/space.jpg')
        background_img.get_at((0, 0))
        background_img = pygame.Surface((width, height))
        screen.blit(background_img, (0, 0))
        pygame.display.flip()

        # Setup Game Window
        icon = pygame.transform.scale(player_img, (32, 32))
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Gallaga Clone')
        pygame.mouse.set_visible(0)

        # TO DO: Initialize Starting Actors
        player = Player(player_img)
        enemy = [Enemy(enemy_img)]

        # Running loop
        while player.alive:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            #added functionality to shot
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Shot.append(Shot(player))

            #added functionality to move
            move = pygame.K_a - pygame.K_d
            player.move(move)