import pygame
import random


class Enemy:
    ## Constructor
    def __init__(self):
        ## postion with placeholder values that need to be set at run time
        self.pos_x = 0
        self.pos_y = 0
        ## enemy image, place holder
        self.enemy_art = pygame.image.load("Placeholder.png")
        ## defines if it is hit or not
        self.hit = False

    ## defines random movements
    def enemy_movement(self):
        if(random.randint(1,5) == 5):
            for x in range(10):
                self.pos_x = self.pos_x + 1
        if(random.randint(1,5) == 4):
            for x in range(10):
                self.pos_y = self.pos_y + 1
        if(random.randint(1,5) == 2):
            for x in range(10):
                self.pos_y = self.pos_y + 1
                self.pos_x = self.pos_x + 1

    ## defines shooting needs a function call for shooting
    def enemy_shooting(self):
        if(random.randint(1,20) == 1):
            pass
