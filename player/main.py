import pygame
from pygame.locals import *
pygame.init()

class Ship(object):
    def __init__(self,x,y,width,height,screen,bg):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveCount = 0
        self.left=False
        self.right=False
        self.screen=screen
        self.bg=bg

        self.ship = pygame.image.load("ship.png")
        self.shipLeft = pygame.image.load("ship_left.png")
        self.shipRight = pygame.image.load("ship_right.png")

        #screen.blit(self.ship, (450, 410))
        #pygame.display.update()
    def move(self):
        #def walkLeft(self):
        if self.left:
            self.x=self.x-10
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.shipLeft, (self.x, self.y))
            #pygame.display.update()
        elif not self.left:
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.ship, (self.x, self.y))

        #def walkRight(self):
        if self.right:
            self.x=self.x+10
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.shipRight, (self.x, self.y))
            #pygame.display.update()

    def controls(self):
        done=False
        while not done:
            self.move()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left=True
                    if event.key == pygame.K_RIGHT:
                        self.right=True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left=False
                    if event.key ==pygame.K_RIGHT:
                        self.right=False

                if event.type == pygame.QUIT: sys.exit()
            pygame.display.update()
