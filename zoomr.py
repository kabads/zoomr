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
    startx = random.randint(0,680)
    starty = random.randint(0,480)
    print ("x is " + str(startx) + " y is " + str(starty))
    drawbot(startx, starty)
    #player = Protagonist(
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate
            elif event.type == KEYDOWN:
                if event.key== K_ESCAPE:
                    terminate()
                elif event.key ==K_a:
                    startx-=10
                    drawbot(startx, starty)
                elif event.key==K_d:
                    startx+=10
                    drawbot(startx, startx)
                elif event.key==K_w:
                    starty-=10
                    drawbot(startx, starty)
                elif event.key==K_s:
                    starty+=10
                    drawbot(startx, starty)
        DISPLAYSURF.fill(BLACK)
        drawbot(startx, starty)
        pygame.display.update()
        
def moveLeft(x,y):
    x = x-1 
    drawbot(x,y)

def drawbot(x,y):
    botRect = pygame.Rect(x,y, 10,10)
    pygame.draw.rect(DISPLAYSURF, WHITE, botRect)
    #DISPLAYSURF.blit(DISPLAYSURF, botRect)
    print "I have drawn a square at " + str(x) + ", " + str(y)
    #return(x,y)



def terminate():
    pygame.quit()
    sys.exit()


#class Protaganist(pygame.sprite.Sprite):
#        def __init__(self, x, y):
#            pygame.init()
#            pygame.sprite.Sprite.__init__(self)
#            # Basic variables
#            self.speed = [2,2]

            # Sets up the image and Rect
#        self.bitmap.set_colorkey((0,0,0))
#        self.shipRect = self.bitmap.get_rect()
#        self.shipRect.topleft = [x,y]

#        def move(self, x, y):
#            self.shipRect.center = (x,y)

#def render(self):
#    screen.blit(self.bitmap, (self.shipRect))

if __name__ == '__main__':
    main()

