# /bin/bash python2 
# Zoomr - a pygame platform
# (c) 2014 A Cripps
# See README and LICENSE for more information 

import pygame, random, sys
from pygame.locals import * 

# set up some constant variables
FPS = 15 
WINWIDTH = 680 
WINHEIGHT = 480 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Zoomr')


    while True:
        runGame()

def runGame():
    # start at a random point
    startx = random.randint(0,680)
    starty = random.randint(0,480)
    print ("x is " + str(startx) + " y is " + str(starty))
    drawbot(startx, starty)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate
            elif event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    terminate()

def drawbot(x,y):
    print "now running drawbot"
    botRect = pygame.Rect(x,y, 10,10)
    pygame.draw.rect(DISPLAYSURF, WHITE, botRect)
    print "I have drawn a square at " + str(x) + ", " + str(y)

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

