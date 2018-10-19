## @file globals.py
#  File containing game globals
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/18/19

import pygame
import constants as const
from pygame.locals import *


# Game Globals
clock = None
#cant have none types so setting a random screen rectangle
screen = Rect(0, 0, 640, 480)
bg = None
dirtyrects = []

# Window Dimensions
width, height = const.WIDTH, const.HEIGHT
screen_size = const.SCREEN_SIZE
