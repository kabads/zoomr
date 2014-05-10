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
rounds = 0 # This will count the number of rounds a player has had. 

class Goal(pygame.sprite.Sprite):
    """This is what the player will be pursuing"""
    def __init__(self):
        """Constructor"""
        pygame.sprite.Sprite.__init__(self)
        x = random.randint(0,680)
        y = random.randint(0,480)
        self.image = pygame.image.load("yellow.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x,self.y))

class Player(pygame.sprite.Sprite):
    """This represents the moving player"""
    def __init__(self, x,y):
        """Constructor"""
        pygame.sprite.Sprite.__init__(self)
        self.health= 30
        self.image = pygame.image.load("blue.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]


    def update(self):
        self.checkBounds()
        self.rect.move_ip([movex, movey])

    def checkBounds(self):
        if self.rect.x >= 670:
            self.rect.x = 670
        elif self.rect.x <=0:
            self.rect.x = 0
        if self.rect.y >= 470:
            self.rect.y = 470
        elif self.rect.y<=0:
            self.rect.y=0


    def damage(self):
        self.health -= 10
        print "Player health: " + str(self.health)
        if self.health <=0:
            print "you died"
            terminate()


class Enemy(pygame.sprite.Sprite):
    """This is a static block that I will try to avoid"""
    def __init__(self):
        """Constructor"""
        x = random.randint(0,680-10)
        y = random.randint(0,480-10)
        pygame.sprite.Sprite.__init__(self)
        self.health = random.randint(0,100)
        self.image = pygame.image.load("red.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        
    def draw(self):
        #enemyRect = pygame.Rect(self.x, self.y, 10,10)
        #pygame.draw.rect(DISPLAYSURF, BLACK, enemyRect)
        #pygame.display.update()
        #print "I just drew an enemy"
        DISPLAYSURF.blit(self.i1, (self.x,self.y))



enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
goal_list = pygame.sprite.Group()
score = 0
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, movex, movey, enemy, player, enemy_list, score
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Zoomr - where can you go today?')
    
    setUpGame()
    while True:
        runGame()
hits = []
def runGame():
    global movex, movey, enemy, player, enemy_list, hits, DISPLAYSURF, score
    
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
    displayScore(score)
    enemy_list.update()
    player_list.update()

    enemy_list.draw(DISPLAYSURF)
    player_list.draw(DISPLAYSURF)
    goal_list.draw(DISPLAYSURF)
    # Check for a collision
    # However, I'm so stupid, because these should never live above the DISPLAYSURF.fill
    for o in enemy_list:
        if pygame.sprite.groupcollide(player_list, enemy_list, False, True):
            #print "careful " + str(player.health)
            for a in player_list:
                a.damage()
    if pygame.sprite.groupcollide(player_list, goal_list, False, False):
        print "you win" 
        score +=1
        quitGame(enemy_list, player_list, goal_list)
        setUpGame()
    pygame.display.flip()

def setUpGame():
    """This will set up the screen to begin the game - we need to get this out of the loop so we can have difficulty rounds"""
    global enemy_list, score, DISPLAYSURF, BASICFONT, FPSCLOCK
    # Let's make the background green for now, and then draw everything afterwards. 
    DISPLAYSURF.fill(GREEN)
    
    # We need a goal to aim for - a yellow square
    goal = Goal()
    goal_list.add(goal)
    all_sprite_list.add(goal)
    
    # Here is the player - protagonist
    player = Player(680/2, 480/2)
    player_list.add(player)
    all_sprite_list.add(player)

    # And here are some enemies - -don't touch them (still to come)
    for x in range (100):
        o = Enemy()
        enemy_list.add(o)
        all_sprite_list.add(o)
        pygame.display.flip()      

def displayScore(score):
    #print "display score has been called: " + str(BASICFONT)  + " display surf: " + str(DISPLAYSURF)
    displayScoreSurf = BASICFONT.render('Score: ' + str(score), True, BLACK)
    displayScoreRect = displayScoreSurf.get_rect()
    #displayScoreRect.topleft = (WINWIDTH -10, WINHEIGHT-10)
    DISPLAYSURF.blit(displayScoreSurf, displayScoreRect)

def quitGame(enemies, player, goal):
    enemies.empty()
    player.empty()
    goal.empty()
    DISPLAYSURF.fill(GREEN)
    runGame()
        
def getRandomCoords():
    x = random.randint(0,680)
    y = random.randint(0,480)
    return x, y

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

