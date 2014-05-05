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

class Player(pygame.sprite.Sprite):
    """This represents the moving player"""
    def __init__(self, x,y):
        """Constructor"""
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health= 100
        self.pos = pygame.Rect(x,y,10,10)
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.i1 = pygame.image.load("blue.jpg")

    def draw(self):
        #playerRect = pygame.Rect(self.x, self.y, 10,10)
        #pygame.draw.rect(DISPLAYSURF, RED, playerRect)
        DISPLAYSURF.blit(self.i1, (self.x,self.y))

    def checkBounds(self):
        if self.x >= 670:
            self.x = 670
        elif self.x <=0:
            self.x = 0
        if self.y >= 470:
            self.y = 470
        elif self.y<=0:
            self.y=0


    def damage(self):
        self.health -= 10
        #"you're hit"
        #if self.health <=0:
            #print "you died"
            #terminate()




class Enemy(pygame.sprite.Sprite):
    """This is a static block that I will try to avoid"""
    def __init__(self):
        """Constructor"""
        self.x = random.randint(0,680-10)
        self.y = random.randint(0,480-10)
        pygame.sprite.Sprite.__init__(self)
        self.health = random.randint(0,100)
        self.pos = pygame.Rect(self.x,self.y,10,10)
        self.image = pygame.Surface([10,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.i1 = pygame.image.load("red.jpg")

    def draw(self):
        #enemyRect = pygame.Rect(self.x, self.y, 10,10)
        #pygame.draw.rect(DISPLAYSURF, BLACK, enemyRect)
        #pygame.display.update()
        #print "I just drew an enemy"
        DISPLAYSURF.blit(self.i1, (self.x,self.y))

    #def checkHit(self):
    #    if 

enemy_list = pygame.sprite.Group()

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, movex, movey, enemy, player, enemy_list
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Zoomr - where can you go today?')
    
    # Let's make the background green for now, and then draw everything afterwards. 
    DISPLAYSURF.fill(GREEN)
    
    # Here is the player - protagonist
    player = Player(680/2, 480/2)
    player.draw()

    # And here are some enemies - -don't touch them (still to come)
    for x in range (20):
        o = Enemy()
        o.draw()
        enemy_list.add(o)
        all_sprite_list.add(o)
        pygame.display.flip()   
    while True:
        runGame()
hits = []
def runGame():
    global movex, movey, enemy, player, enemy_list, hits
    
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

    # Let's start to draw everything back on the screen - always starting with the background
    DISPLAYSURF.fill(GREEN)

    # Draw the enemies and check for a collision
    # However, I'm so stupid, because these should never live above the DISPLAYSURF.fill
    for o in enemy_list:
        o.draw()
        if pygame.sprite.collide_rect(player, o)==True:
            print "careful " + str(player.health)
            player.damage()
    #hits = pygame.sprite.spritecollide(player, enemy_list, True)
        #print "collision"
    #for i in hits:
    #    player.damage()
    
    player.x += movex
    player.y += movey
    player.checkBounds()

    player.draw()
    for o in enemy_list:
        o.draw
    #hits = pygame.sprite.spritecollide(player, enemy_list, True)
    #print "hits is this long: " + str(len(hits))
    #for i in hits:
    #    player.damage()
    # update the whole shebang
    pygame.display.flip()
        
def getRandomCoords():
    x = random.randint(0,680)
    y = random.randint(0,480)
    return x, y

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

