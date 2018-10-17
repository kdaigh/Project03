import pygame
from pygame.locals import *
from Enemy.Enemy import Enemy
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
        self.hitbox1 = (self.x + 16, self.y, 77, 90)
        self.hitbox2 = (self.x - 3, self.y, 80, 115)

        #where the ship is being loaded, left and right are for when it moves
        self.ship = pygame.image.load("images/player_ship.png")
        self.shipLeft = pygame.image.load("images/player_ship_left.png")
        self.shipRight = pygame.image.load("images/player_ship_right.png")
        #pygame.display.update()
        self.screen.blit(self.ship, (self.x, self.y))




    #this is called when left and right arrow keys are pressed or held
    #self.screen.blit(self.bg, (0,0)) wipes out previous position of ship
    def move(self):
        #creating left bounds for ship
        if self.left:
            if self.x > 15:
                self.x=self.x-10
                self.screen.blit(self.bg, (0,0))
                self.screen.blit(self.shipLeft, (self.x, self.y))
                #creating hitbox for ship when moving left
                self.hitbox1 = (self.x, self.y, 77, 90)
                self.hitbox2 = (self.x - 3, self.y + 80, 115, 85)
                # temporary red box around ship to visualize hitbox, will eventually be reomved
                pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox1, 2)
                pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox2, 2)

        #so the ship displays upright when you are not pressing a key
        elif not self.left:
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.ship, (self.x, self.y))
            #creating hitbox for ship when not moving
            self.hitbox1 = (self.x + 16, self.y, 77, 90)
            self.hitbox2 = (self.x - 3, self.y + 90, 115, 85)
            #temporary red box around ship to visualize hitbox, will eventually be reomved
            pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox1, 2)
            pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox2, 2)

        if self.right:
            #creating right bounds for ship
            if self.x < 780:
                self.x=self.x+10
                self.screen.blit(self.bg, (0,0))
                self.screen.blit(self.shipRight, (self.x, self.y))
                #creating hit box for ship when moving right
                self.hitbox1 = (self.x + 30, self.y, 77, 90)
                self.hitbox2 = (self.x - 3, self.y + 80, 115, 85)
                #temporary red box around ship to visualize hitbox, will eventually be reomved
                pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox1, 2)
                pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox2, 2)

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
