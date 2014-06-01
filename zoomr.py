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
        x = random.randint(0,WINWIDTH-10)
        y = random.randint(0,WINHEIGHT-10)
        self.image = pygame.image.load("yellow.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x,self.y))


class Player(pygame.sprite.Sprite):
    """This represents the moving player"""
    def __init__(self, x,y):
        """Constructor"""
        self.alive = True
        pygame.sprite.Sprite.__init__(self)
        self.health= 30
        self.image = pygame.image.load("blue.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def update(self):
        """Move the player to where they need to be."""
        self.checkBounds()
        self.rect.move_ip([movex, movey])

    def checkBounds(self):
        """Need to make sure that I don't hit the edge of the screen. This method prevents that. """
        if self.rect.x >= 670:
            self.rect.x = 670
        elif self.rect.x <=0:
            self.rect.x = 0
        if self.rect.y >= 470:
            self.rect.y = 470
        elif self.rect.y<=0:
            self.rect.y=0

    def damage(self):
        """This method will damage the player because they hit an enemy. They will take some damage.
        If damage gets to zero, then the player will die."""
        self.health -= 10
        #print "Player health: " + str(self.health)
        if self.health <=0:
            self.alive=False
            #playerDies(enemy_list, player_list, goal_list)
            #setUpGame()
            #terminate()


class Enemy(pygame.sprite.Sprite):
    """This is a static block that I will try to avoid"""
    def __init__(self):
        """Constructor"""
        x = random.randint(0, WINWIDTH-10)
        y = random.randint(0, WINHEIGHT-10)
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.health = random.randint(0,100)
        self.image = pygame.image.load("red.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        
    def draw(self):
        """This draws the player."""
        #enemyRect = pygame.Rect(self.x, self.y, 10,10)
        #pygame.draw.rect(DISPLAYSURF, BLACK, enemyRect)
        #pygame.display.update()
        #print "I just drew an enemy"
        DISPLAYSURF.blit(self.i1, (self.x,self.y))

    def wobble(self):
        # if we get to a particular level, we will 'wobble' the enemies and they may kill each other off - experimental

        return()

enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
goal_list = pygame.sprite.Group()
score = 0
difficulty = 1


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, movex, movey, enemy, player, enemy_list, score, player_list, goal_list, difficulty
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Zoomr - where can you go today?')
    
    setUpGame(difficulty)
    while True:
        if player.alive == True:
            runGame()
        else:
            quitGame(enemy_list, player_list, goal_list)
            DISPLAYSURF.fill(GREEN)
            showGameOver()
            pygame.display.flip()
            setUpGame(difficulty)
hits = []


def runGame():
    global movex, movey, enemy, player, enemy_list, hits, DISPLAYSURF, score, player_list, goal_list, difficulty
    
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            if event.key == K_a:
               movex = -1  # playerStartx-=10
            if event.key == K_d:
                movex = 1  # playerStartx+=10
            if event.key == K_w:
                movey = -1  # playerStarty-=10
            if event.key == K_s:
                movey = 1  # playerStarty+=10
            
        if event.type == KEYUP:
            if event.key == K_a:
                movex = 0 
            if event.key == K_d:
                movex =0
            if event.key == K_w:
                movey = 0
            if event.key == K_s:
                movey=0

    # Just check what state the player is in - if he is not alive, then wait for a key press with game over on the screen
    if not player.alive:
        quitGame(enemy_list, player_list, goal_list)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Game Over", 1, (10,10,10))
        textpos = text.get_rect(centerx = DISPLAYSURF.get_width()/2)
        DISPLAYSURF.fill(BLUE)
        DISPLAYSURF.blit(text, textpos)
        pygame.time.wait(500)

        while True:
            if checkForKeyPress():
                pygame.event.get() # clear event queue
                return
                #setUpGame()

    # Let's start to draw everything back on the screen - always starting with the background
    DISPLAYSURF.fill(GREEN)
    
    enemy_list.update()
    player_list.update()

    enemy_list.draw(DISPLAYSURF)
    player_list.draw(DISPLAYSURF)
    goal_list.draw(DISPLAYSURF)
    displayScore(score)
    # Check for a collision
    # However, I'm so stupid, because these should never live above the DISPLAYSURF.fill
    #for o in enemy_list:
    #    if pygame.sprite.groupcollide(player_list, enemy_list, False, True):
    #        #print "careful " + str(player.health)
    for a in player_list:
        if pygame.sprite.groupcollide(player_list, enemy_list, False, True):
            a.damage()
    if pygame.sprite.groupcollide(player_list, goal_list, False, False):
        print "you win" 
        score +=1
        difficulty = difficulty + score * 20
        quitGame(enemy_list, player_list, goal_list)
        setUpGame(difficulty)
    pygame.display.flip()


def setUpGame(difficulty):
    """This will set up the screen to begin the game - we need to get this out of the loop so we can have difficulty
    rounds"""
    global enemy_list, score, DISPLAYSURF, BASICFONT, FPSCLOCK, player
    # Let's make the background green for now, and then draw everything afterwards. 
    DISPLAYSURF.fill(GREEN)
    
    # We need a goal to aim for - a yellow square
    goal = Goal()
    goal_list.add(goal)
    all_sprite_list.add(goal)
    
    # Here is the player - protagonist
    player = Player(WINWIDTH/2, WINHEIGHT/2)
    player_list.add(player)
    all_sprite_list.add(player)

    # And here are some enemies - -don't touch them (still to come)
    for x in range (difficulty):
        o = Enemy()
        enemy_list.add(o)
        #all_sprite_list.add(o)
        pygame.display.flip()      


def showGameOver():
    global score, difficulty
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render('Game Over', 1, (10,10,10))
    textpos = text.get_rect(centerx=DISPLAYSURF.get_width()/2, centery = DISPLAYSURF.get_height()/2)
    DISPLAYSURF.fill(GREEN)
    DISPLAYSURF.blit(text, textpos)
    pygame.display.flip()
    pygame.time.wait(2000)
    score = 0
    difficulty = 1
    return


def playerDies(enemies, player, goal):
    """The player has died. """
    # At the moment, I think this function is not being called. 
    global score
    # print "player dies called"
    quitGame(enemies, player, goal)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Game Over", 1, (10,10,10))
    textpos = text.get_rect(centerx = DISPLAYSURF.get_width()/2)
    checkForKeyPress()
    DISPLAYSURF.fill(GREEN)
    #DISPLAYSURF.blit(endGameSurf, endGameRect)
    DISPLAYSURF.blit(text, textpos)
    pygame.time.wait(500)
    check = checkForKeyPress()
    while check:
        check= checkForKeyPress()
        pygame.event.get()  # clear event queue
    return


def displayScore(score):
    displayScoreSurf = BASICFONT.render('Score: ' + str(score), True, BLACK)
    displayScoreRect = displayScoreSurf.get_rect()
    #displayScoreRect.topleft = (WINWIDTH -10, WINHEIGHT-10)
    DISPLAYSURF.blit(displayScoreSurf, displayScoreRect)


def quitGame(enemies, player, goal):
    # We are not ending the program, just the current game
    # We delete all the objects - cleaning up
    enemies.empty()  # delete the enemies in the enemies list
    player.empty()  # delete the player in the player list
    goal.empty()  # delete the goal in the goal list
    return 


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

