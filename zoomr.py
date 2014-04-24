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
GREEN = (50,155,0)
BLUE = (0,0,255)

class Enemy:
    def __init__(self, health, x, y):
        #self.x = random.randint(0,680)
        #self.y = random.randint(0,480)
        self.x = x
        self.y = y
        self.health = 100
        self.pos = pygame.Rect(x,y,10,10)
        
    def draw(self):
        print "o.draw has been run!"
        enemyRect = pygame.Rect(self.x, self.y, 10,10)
        pygame.draw.rect(DISPLAYSURF, BLUE, enemyRect)
        pygame.display.update()

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
    DISPLAYSURF.fill(GREEN)

    enemyObjects = []
    for x in range (3):
        x,y = getRandomCoords()
        o = Enemy(100,x,y)
        enemyObjects.append(o)
        
    for o in enemyObjects:
        o.draw()
        #pygame.display.update()


    # start at a random point
    playerStartx, playerStarty = getRandomCoords()
    drawPlayer(playerStartx, playerStarty)
    # start the bot at a random point
    botStartx, botStarty = getRandomCoords()
    drawBot(botStartx, botStarty)

    while True:
        #for o in enemyObjects:
        #    o.draw()
            #screen.blit(background, o.x, o.y)
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
                
        drawPlayer(playerStartx, playerStarty)
        botStartx, botStarty = moveBot(botStartx, botStarty)
        botStartx, botStarty = checkBounds(botStartx, botStarty)
        drawBot(botStartx, botStarty)
        pygame.display.update()

def checkBounds(x,y):
    if x > 680:
        x = 680
    if y > 480:
        y = 480
    if x <= 0:
        x = 0
    if y <= 0: 
        y = 0
    return(x,y)

def moveBot(x,y):
    direction = random.randint(0,3)
    if direction ==0:
        x-=1
        return(x,y)
    elif direction ==1: 
        x+=1 
        return(x,y)
    elif direction ==2:
        y-=1
        return(x,y)
    elif direction ==3:
        y+=1 
        return(x,y)
        
def getRandomCoords():
    x = random.randint(0,680)
    y = random.randint(0,480)
    return x, y

def drawPlayer(x,y):
    playerRect = pygame.Rect(x,y,10,10)
    pygame.draw.rect(DISPLAYSURF, WHITE, playerRect)


def drawBot(x,y):
    botRect = pygame.Rect(x,y,10,10)
    pygame.draw.rect(DISPLAYSURF, RED, botRect)

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

