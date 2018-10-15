import pygame
from pygame.locals import *
pygame.init()
import random, os.path


class Enemy(object):
    ## Constructor
    def __init__(self,x,y,width,height,screen,bg):
        ## postion with placeholder values that need to be set at run time
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        ## defines if it is hit or not
        self.hit = False
        self.screen=screen
        #self.bg=bg

        ## enemy image, place holder
        self.enemy_img = pygame.image.load("images/enemy_spaceship.png")


    def add_enemies(self):
        while not self.hit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    pygame.quit()
                    quit()
            #self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.enemy_img, (self.pos_x, self.pos_y))
            pygame.display.update()


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
