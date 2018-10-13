import pygame
from pygame.locals import *
pygame.init()

class Ship(object):
    def __init__(self,x,y,width,height,screen,bg):
        #variables for ship itself
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveCount = 0
        self.left=False
        self.right=False
        self.screen=screen
        self.bg=bg

        #where the ship is being loaded, left and right are for when it moves
        self.ship = pygame.image.load("ship.png")
        self.shipLeft = pygame.image.load("ship_left.png")
        self.shipRight = pygame.image.load("ship_right.png")

    #this is called when left and right arrow keys are pressed or held
    #self.screen.blit(self.bg, (0,0)) wipes out previous position of ship
    def move(self):
        if self.left:
            self.x=self.x-10
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.shipLeft, (self.x, self.y))

        #so the ship displays upright when you are not pressing a key
        elif not self.left:
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.ship, (self.x, self.y))

        if self.right:
            self.x=self.x+10
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.shipRight, (self.x, self.y))

    #the method that monitors for when left and right keys are pressed
    #eventually it will also look for space to fire
    def controls(self):
        done=False
        while not done:
            self.move()
            for event in pygame.event.get():
                #for when key is being pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left=True
                    if event.key == pygame.K_RIGHT:
                        self.right=True

                #for when key is no longer being pressed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left=False
                    if event.key ==pygame.K_RIGHT:
                        self.right=False

                #you're done playing so this exits it for you
                if event.type == pygame.QUIT :
                    pygame.quit()
                    quit()
            #updates where the rocket is
            pygame.display.update()
