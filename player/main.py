import pygame
from pygame.locals import *
pygame.init()

class Ship(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveCount = 0
        self.left=False
        self.right=False

        self.ship = pygame.image.load("ship.png")
        screen.blit(self.ship, (450, 410))
        #pygame.display.update()
    def move(self,left,right):
        #def walkLeft(self):
        if left:
            self.x=self.x-10
            screen.blit(bg, (0,0))
            screen.blit(self.ship, (self.x, self.y))
            #pygame.display.update()

        #def walkRight(self):
        if right:
            self.x=self.x+10
            screen.blit(bg, (0,0))
            screen.blit(self.ship, (self.x, self.y))
            #pygame.display.update()

# setting window size
screen = pygame.display.set_mode((900, 600))
# label window
pygame.display.set_caption("Py Five")

bg = pygame.image.load("space.jpg")
screen.blit(bg, (0,0))

#pygame.display.update()
#screen.fill(0,0,255)
playing = Ship(450,410,64,64)
left=False
right=False
while 1:
    playing.move(left,right)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left=True
            if event.key == pygame.K_RIGHT:
                right=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left=False
            if event.key ==pygame.K_RIGHT:
                right=False


        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_LEFT:
        #        playing.walkLeft()
        #    elif event.key == pygame.K_RIGHT:
        #        playing.walkRight()
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()
