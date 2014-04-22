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
    DISPLAYSURF.fill(BLACK)

    while True:
        runGame()

def runGame():
    # start at a random point
    playerStartx, playerStarty = getRandomCoords()
    drawPlayer(playerStartx, playerStarty)
    # start the bot at a random point
    botStartx, botStarty = getRandomCoords()
    drawBot(botStartx, botStarty)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate
            elif event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    terminate()
                elif event.key ==K_a:
                    playerStartx-=10
                elif event.key==K_d:
                    playerStartx+=10
                elif event.key==K_w:
                    playerStarty-=10
                elif event.key==K_s:
                    playerStarty+=10
            elif event.type ==KEYUP: 
                break
                
        DISPLAYSURF.fill(BLACK)
        drawPlayer(playerStartx, playerStarty)
        drawBot(botStartx, botStarty)
        pygame.display.update()
        
def getRandomCoords():
    x = random.randint(0,680)
    print "x is " + str(x)
    y = random.randint(0,480)
    print "y is " + str(y)
    return x, y

def drawPlayer(x,y):
    playerRect = pygame.Rect(x,y,10,10)
    pygame.draw.rect(DISPLAYSURF, WHITE, playerRect)


def drawBot(x,y):
    botRect = pygame.Rect(200,200,10,10)
    pygame.draw.rect(DISPLAYSURF, RED, botRect)

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

