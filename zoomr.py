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
movex, movey=0,0
all_sprite_list = pygame.sprite.Group()

playerStartx = 0 
playerStarty = 0




class Player(pygame.sprite.Sprite):
    """This represents the moving player"""
    def __init__(self, x,y):
        """Constructor"""
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y 
        self.pos = pygame.Rect(x,y,10,10)
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()


class Enemy(pygame.sprite.Sprite):
    """This is a static block that I will try to avoid"""
    def __init__(self, health, x, y):
        """Constructor"""
        #self.x = random.randint(0,680)
        #self.y = random.randint(0,480)
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health = health
        self.pos = pygame.Rect(self.x,self.y,10,10)
        self.image = pygame.Surface([10,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
    def draw(self):
        enemyRect = pygame.Rect(self.x, self.y, 10,10)
        pygame.draw.rect(DISPLAYSURF, BLACK, enemyRect)
        #pygame.display.update()

    def checkBounds(self):
        if self.x >= 670:
            self.x = 670
        elif self.x <=0:
            self.x = 0
        if self.y >= 470:
            self.y = 470
        elif self.y<=0:
            self.y=0

#enemy_list = pygame.sprite.Group()
enemy = Enemy(100,100,100) 
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, movex, movey, enemy
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Zoomr')
    DISPLAYSURF.fill(GREEN)
       
    while True:
        runGame()

def runGame():
    global movex, movey, enemy
    
    #DISPLAYSURF.fill(GREEN)
    #player = Player(680/2,480/2)
    #all_sprite_list.add(player)
    #enemyObjects = []
    #for x in range (8):
    #    x,y = getRandomCoords()
    #    o = Enemy(100,x,y)
    #    enemy_list.add(o)
    #    all_sprite_list.add(o)
   
    #for o in enemyObjects:
    #    o.draw(draw)
    #all_sprite_list.draw(DISPLAYSURF)
    #pygame.display.update()
    #enemy_list.draw(DISPLAYSURF)
    pygame.display.flip()

    # start at a random point
    #playerStartx, playerStarty = getRandomCoords()
    #drawPlayer(playerStartx, playerStarty)
    # start the bot at a random point
    #botStartx, botStarty = getRandomCoords()
    #drawBot(botStartx, botStarty)
    #enemy.draw()
    #all_sprite_list.draw(DISPLAYSURF)
 
            
    
        #for o in enemyObjects:
        #    o.draw()
            #screen.blit(background, o.x, o.y)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key== K_ESCAPE:
                terminate()
            if event.key ==K_a:
               movex = -1 #playerStartx-=10
            if event.key==K_d:
                movex = 1 #playerStartx+=10
            if event.key==K_w:
                movey = -1 #playerStarty-=10
            if event.key==K_s:
                movey = 1 #playerStarty+=10
            
            
        if (event.type==KEYUP):
            if (event.key==K_a):
                movex = 0 
            if (event.key==K_d):
                movex =0
            if (event.key==K_w):
                movey = 0
            if (event.key==K_s):
                movey=0
                
    enemy.x += movex
    enemy.y += movey
    DISPLAYSURF.fill(GREEN)
    enemy.checkBounds()
    enemy.draw()
    pygame.display.flip()

               
        #drawPlayer(playerStartx, playerStarty)
        #botStartx, botStarty = moveBot(botStartx, botStarty)
        #botStartx, botStarty = checkBounds(botStartx, botStarty)
        #drawBot(botStartx, botStarty)
        #pygame.display.update()
        #DISPLAYSURF.fill(GREEN)

        # Somewhere here, I think I need to create a background based on the DISPLAYSURF.
        #for o in enemyObjects:
        #    o.draw()
        # Perhaps I need to differentiate between screen (DISPLAYSURF) and a background (a graphic)
        



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

