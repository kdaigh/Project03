## @file enemy.py
#  Source file for enemy object
#
#  Project: Gallaga Clone
#  Author: Py Five
#  Created: 10/17/19

import pygame
import random
from actor import Actor


## @class Enemy
#  @brief Implements Actor base class as Enemy object
class Enemy(Actor):

    ## Constructor
    def __init__(self,x,y,width,height,screen,bg):
        ## postion with placeholder values that need to be set at run time
        self.pos_x = x
        self.pos_y = y
        self.width = 52
        self.height = 48
        ## defines if it is hit or not
        self.hit = False
        self.screen=screen
        self.screen_width = 900
        self.screen_height = 600
        self.bg=bg

        ## enemy image, place holder
        self.enemy_img = pygame.image.load("images/enemy_spaceship.png")
        self.rect = self.enemy_img.get_rect()



    def add_enemies(self):
        x_boarder = self.screen_width - self.width - 20
        y_boarder = int(self.screen_height /2)  - self.height - 20
        #while not self.hit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        #self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.bg, (0,0))
        for x in range(40, x_boarder, 75):
            for y in range(20, y_boarder, 70):
                self.pos_y = y
                self.pos_x = x
                self.screen.blit(self.enemy_img, (self.pos_x, self.pos_y))
        pygame.display.update()
        self.hit =False




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
