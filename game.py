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
from pygame.locals import *
import constants as const


class Game:

    ## Constructor; Initializes game components
    def __init__(self):
        # Initialize game
        pygame.init()

        # Setup Game Window
        icon = pygame.image.load('assets/images/player_ship.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Gallaga Clone')
        self.screen = pygame.display.set_mode(const.SCREENRECT.size, 0)
        pygame.mouse.set_visible(0)

        # Initialize clock
        self.clock = pygame.time.Clock()


    ## Loads and scales object/game image
    #  @author: Kristi
    #  @pre: image exists
    #  @param: filename, name of image to be loaded
    #  @param: width, desired width of image
    #  @param: height, desired height of image
    #  @returns: Surface object
    def load_image(self, filename, file_width, file_height):
        # Load image
        filename = os.path.join('assets/images', filename)
        img = pygame.image.load(filename)

        # Scale image
        img = pygame.transform.scale(img, (file_width, file_height))

        # Make transparent
        img.set_colorkey(img.get_at((0,0)), RLEACCEL)

        return img.convert()


    ## Runs the game session
    def run(self):

        # Load Images
        background_img = pygame.image.load('assets/images/space.jpg')
        player_img = self.load_image('player_ship.png', 45, 65)
        enemy_img = self.load_image('enemy_spaceship.png', 26, 26)
        # shot_img = self.load_image('missile1.png', 10, 24)

        # Load Background
        background = pygame.Surface(const.SCREENRECT.size)
        for x in range(0, const.SCREENRECT.width, background_img.get_width()):
            background.blit(background_img, (x, 0))
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

        # Initialize Starting Actors
        player = Player(player_img)
        enemy = Enemy(enemy_img)
        dirtyrects = []

        # Running loop
        while player.alive:

            self.clock.tick(const.FPS)

            # Call event queue
            pygame.event.pump()

            # Quit condition
            if pygame.event.peek(QUIT):
                break

            # Clear screen and Update actors
            for actor in [player] + [enemy]:
                render = actor.erase(self.screen, background)
                dirtyrects.append(render)
                actor.update()

            # Process input
            key_presses = pygame.key.get_pressed()
            right = key_presses[pygame.K_RIGHT]
            left = key_presses[pygame.K_LEFT]

            # Move the player
            x_dir = right - left
            player.move(x_dir)

            # HOLD: Postponing shooting functionality until player moves
            # #added functionality to shot
            #     elif event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_SPACE:
            #             Shot.append(Shot(player))

            # Draw actors
            for actor in [player] + [enemy]:
                render = actor.draw(self.screen)
                dirtyrects.append(render)

            # Update actors
            pygame.display.update(dirtyrects)
            dirtyrects = []

        pygame.time.wait(50)