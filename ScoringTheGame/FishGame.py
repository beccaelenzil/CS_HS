import pygame
import random
import math
pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
pygame.init()
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
screen = pygame.display.set_mode([800,600])

font = pygame.font.SysFont("Calibri",25)

menutext = font.render("Menu",1,WHITE)
instructionstext = font.render("Instructions",1,WHITE)
playagaintext = font.render("Play Again",1,WHITE)

tf = "highscore.txt"

#images
background_image1 = pygame.image.load("graphics/abovelake.jpg").convert()
background_image2 = pygame.image.load("graphics/belowlake.jpg").convert()
fishmansit = pygame.image.load("graphics/fishmansitting.png").convert()
fishmancast1 = pygame.image.load("graphics/fishmancast1.png").convert()
fishmancast2 = pygame.image.load("graphics/fishmancast2.png").convert()
castboxborder = pygame.image.load("graphics/castboxborder.jpg").convert()
fishmanfish = pygame.image.load("graphics/fishmanfish.png").convert()
menubackground = pygame.image.load("graphics/menu.png").convert()

fishmansit.set_colorkey(WHITE)
fishmancast1.set_colorkey(WHITE)
fishmancast2.set_colorkey(WHITE)
fishmanfish.set_colorkey(WHITE)

#sounds
themeair = pygame.mixer.Sound("sounds/themeair.ogg")
themewater = pygame.mixer.Sound("sounds/themewater.ogg")
linewater = pygame.mixer.Sound("sounds/linewater.ogg")
linesnap = pygame.mixer.Sound("sounds/linesnap.ogg")
water = pygame.mixer.Sound("sounds/water.ogg")
reeling = pygame.mixer.Sound("sounds/reeling.ogg")
reelingsoft = pygame.mixer.Sound("sounds/reelingsoft.ogg")
victory = pygame.mixer.Sound("sounds/victory.ogg")

clock = pygame.time.Clock()
done = False


class fishman:
    #player
    def __init__(self,name):
        self.name = name
        self.posx = 40
        self.posy = 100
        self.mode = "sit"
        self.action = "in"
class lure(object):
    #worm
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.movex = 0
        self.omovey = -10
        self.movey = -10
        self.grav = 1
        self.image = pygame.image.load("graphics/worm.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = pygame.Rect(self.posx,self.posy,self.image.get_rect()[0],self.image.get_rect()[1])
class fish(object):
    #fish
    def __init__(self):
        self.image = pygame.image.load("graphics/fish.png").convert()
        self.image.set_colorkey(BLACK)
        self.mode = "free"
        self.movecounter = 0
        self.posx = 400
        self.posy = 400
        self.force = 2
        self.direct = math.pi/4
        self.lineforce = 1
        self.stretchfish = 0
        self.stretchfactor = 0
        self.OL = 0
        self.CL = 0
        self.rect = pygame.Rect(self.posx,self.posy,self.image.get_rect()[0],self.image.get_rect()[1])
        self.posxo = 0
        self.posx0 = 0
    def uncaughtmove(self):
        #movement while not hooked
        self.posx += self.force*math.cos(self.direct)
        self.posy += -1*self.force*math.sin(self.direct)
        self.movecounter += 1
    def move(self):
        #movement while hooked
        self.posx0 = self.posx - 170
        self.posy0 = self.posy - 47
        self.posx0 += math.cos(self.direct)*f.force*2
        self.posy0 += -math.sin(self.direct)*f.force*2
        a = math.atan(self.posy0/self.posx0)
        b = 2*math.pi*self.direct
        self.stretchfish = f.force*math.cos(b-a)
        self.stretchfactor += (self.lineforce + self.stretchfish)/20
        if self.stretchfactor < 10:
            self.CL = self.OL + self.stretchfactor
        elif self.stretchfactor < 15:
            self.CL = self.OL + 9 + math.sqrt(self.stretchfactor-9)
        dist = math.sqrt(self.posx0**2+self.posy0**2)
        compress = self.CL/dist
        self.posx0 = self.posx0*compress
        self.posy0 = self.posy0*compress
        self.posx = self.posx0 + 170
        self.posy = self.posy0 + 47

gamestage = "menu"
gameon = 0
menuselect = 0


#play both musics so can switch between when go underwater
themeair.play(loops=-1)
themewater.play(loops=-1)
themewater.set_volume(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gamestage == "sitting":
                    gamestage = "castingselect"
                elif gamestage == "castingselect":
                    worm.movex = int(castcounter/5)
                    worm.posx = player.posx
                    worm.posy = player.posy
                    gamestage = "casting"
                    castanimatecounter = 0
                elif gamestage == "menu":
                    if menuselect == 0:
                        f = fish()
                        f.mode = "free"
                        f.movecounter = 0
                        f.posx = 400
                        f.posy = 400
                        f.force = 2
                        f.direct = math.pi/4
                        f.lineforce = 1
                        f.OL = math.sqrt(f.posx**2+f.posy**2)
                        f.CL = f.OL
                        f.rect = pygame.Rect(f.posx,f.posy,f.image.get_rect()[2],f.image.get_rect()[3])
                        f.stretchfactor = 0

                        #defining player
                        player = fishman("player")
                        player.posx = 110
                        player.posy = 25
                        player.mode = "sit"
                        player.action = "none"

                        #defining lure
                        worm = lure()
                        worm.rect = pygame.Rect(worm.posx,worm.posy,worm.image.get_rect()[2],worm.image.get_rect()[3])

                        #bunch of variables
                        castboxposx = 200
                        castboxposy = 44

                        castcounter = 1
                        castcounterchange = 1

                        castanimatecounter = 0
                        playagainselect = 0
                        score = 0
                        gamestage = "sitting"
                        gameon = 1
                        water.play(-1)
                        start_ticks = pygame.time.get_ticks()
                    elif menuselect == 1:
                        gamestage = "instructions"
                elif gamestage == "catching":
                        f = fish()
                        f.mode = "free"
                        f.movecounter = 0
                        f.posx = random.randint(300,700)
                        f.posy = random.randint(300,500)
                        f.force = 2
                        f.direct = math.pi/4
                        f.lineforce = 1
                        f.OL = math.sqrt(f.posx**2+f.posy**2)
                        f.CL = f.OL
                        f.rect = pygame.Rect(f.posx,f.posy,f.image.get_rect()[2],f.image.get_rect()[3])
                        f.stretchfactor = 0

                        #defining player
                        player = fishman("player")
                        player.posx = 110
                        player.posy = 25
                        player.mode = "sit"
                        player.action = "none"

                        #defining lure
                        worm = lure()
                        worm.rect = pygame.Rect(worm.posx,worm.posy,worm.image.get_rect()[2],worm.image.get_rect()[3])

                        #bunch of variables
                        castboxposx = 200
                        castboxposy = 44

                        castcounter = 1
                        castcounterchange = 1

                        castanimatecounter = 0

                        gamestage = "sitting"
                        gameon = 1
                elif gamestage == "finished":
                    if playagainselect == 0:
                        gamestage = "menu"
                    elif playagainselect == 1:
                        f = fish()
                        f.mode = "free"
                        f.movecounter = 0
                        f.posx = 400
                        f.posy = 400
                        f.force = 2
                        f.direct = math.pi/4
                        f.lineforce = 1
                        f.OL = math.sqrt(f.posx**2+f.posy**2)
                        f.CL = f.OL
                        f.rect = pygame.Rect(f.posx,f.posy,f.image.get_rect()[2],f.image.get_rect()[3])
                        f.stretchfactor = 0

                        #defining player
                        player = fishman("player")
                        player.posx = 110
                        player.posy = 25
                        player.mode = "sit"
                        player.action = "none"

                        #defining lure
                        worm = lure()
                        worm.rect = pygame.Rect(worm.posx,worm.posy,worm.image.get_rect()[2],worm.image.get_rect()[3])

                        #bunch of variables
                        castboxposx = 200
                        castboxposy = 44

                        castcounter = 1
                        castcounterchange = 1

                        castanimatecounter = 0
                        playagainselect = 0
                        score = 0
                        gamestage = "sitting"
                        gameon = 1
                        water.play(-1)
                        start_ticks = pygame.time.get_ticks()
            elif event.key == pygame.K_DOWN:
                if gamestage == "failed" or gamestage == "sink":
                    gamestage = "reeling"
                    reelingsoft.play(-1)
                elif gamestage == "fight":
                    player.action = "in"
                    reeling.play(-1)
                elif gamestage == "menu":
                    if menuselect == 0:
                        menuselect = 1
                    elif menuselect == 1:
                        menuselect = 0
                elif gamestage == "finished":
                    if playagainselect == 0:
                        playagainselect = 1
                    elif playagainselect == 1:
                        playagainselect = 0
            elif event.key == pygame.K_UP:
                if gamestage == "fight":
                    player.action = "out"
                    reeling.play(-1)
                if gamestage == "menu":
                    if menuselect == 0:
                        menuselect = 1
                    elif menuselect == 1:
                        menuselect = 0
                elif gamestage == "finished":
                    if playagainselect == 0:
                        playagainselect = 1
                    elif playagainselect == 1:
                        playagainselect = 0
        elif event.type == pygame.KEYUP:
            if gamestage == "fight":
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.action = "none"
                    reeling.stop()


    #what to do when not in game portion
    if gameon == 0:
        screen.blit(menubackground,[0,0])

    #what to do when in game portion
    elif gameon == 1:
        f.rect.x = f.posx
        f.rect.y = f.posy
        worm.rect.x = worm.posx
        worm.rect.y = worm.posy
        #what to do if fish not hooked
        if worm.rect.colliderect(f.rect):
            if gamestage == "sink" or gamestage == "reeling" or gamestage == "failed":
                f.OL = math.sqrt((f.posx0-170)**2+(f.posy-47)**2)
                f.CL = f.OL
                f.stretchfactor = 0
                f.lineforce = 0
                f.force = random.random()*3+.5
                iforce = f.force
                f.direct = random.random()*math.pi/2+3*math.pi/2
                hookchoice = [1,5,25]
                hooklevel = random.choice(hookchoice)
                player.action = "none"
                reelingsoft.stop()
                gamestage = "fight"
        if f.mode == "free":
            f.uncaughtmove()
            if f.movecounter >= 100 or f.posx >= 720 or f.posx <= 120 or f.posy >= 520 or f.posy <= 120:
                if f.posx >= 500 and f.posy <= 280:
                    f.direct = random.random()*math.pi/2+math.pi
                elif f.posx < 200 and f.posy <= 280:
                    f.direct = random.random()*math.pi/4+math.pi*7/4
                elif f.posx >= 500 and f.posy > 360:
                    f.direct = random.random()*math.pi/2+math.pi/2
                elif f.posx < 200 and f.posy > 360:
                    f.direct = random.random()*math.pi/4
                else:
                    f.direct = random.random()*math.pi*2
                f.movecounter = 0
        #what to do if fish hooked
        elif f.mode == "caught":
            if player.action == "in":
                f.OL += -1
                f.lineforce = 1
            elif player.action == "out":
                f.OL += 1
                f.lineforce = -2
            elif player.action == "none":
                if f.stretchfactor > 5:
                    f.lineforce = -.5
                else:
                    f.lineforce = 0
            f.move()
            f.movecounter += 1
            if f.movecounter >= 25:
                f.direct += random.random()*math.pi/2-math.pi/4
                f.movecounter = 0
                if f.force > 0:
                    f.force += -.05
            if f.posx >= 720 or f.posx <= 120 or f.posy >= 520 or f.posy <= 120:
                if f.posx >= 350 and f.posy <= 320:
                    f.direct = random.random()*math.pi/2+math.pi
                elif f.posx < 350 and f.posy <= 320:
                    f.direct = random.random()*math.pi/2+3/2*math.pi
                elif f.posx >= 350 and f.posy > 320:
                    f.direct = random.random()*math.pi/2+math.pi/2
                elif f.posx < 350 and f.posy > 320:
                    f.direct = random.random()*math.pi/2
                movecounter = 0
                #print [f.posx,f.posy,f.direct]
            if f.CL - f.OL > 14:
                linesnap.play()
                gamestage = "end"
            if f.CL - f.OL < -3:
                if random.randint(0,100) <=  hooklevel:
                    gamestage = "end"
            if f.CL - f.OL < -7:
                if random.randint(0,50) <= hooklevel:
                    gamestage = "end"
            if f.CL <= 5:
                score += 1
                reeling.stop()
                victory.play()
                gamestage = "catching"
            #print [f.OL,f.CL,f.stretchfactor,f.lineforce,f.force,f.direct,f.stretchfish]

        #blitting screen parts
        screen.blit(background_image1,[0,0])
        screen.blit(background_image2,[0,100])
        screen.blit(f.image,[f.posx,f.posy])
        if player.mode == "sit":
            screen.blit(fishmansit,[player.posx,player.posy])
        elif player.mode == "cast1":
            screen.blit(fishmancast1,[player.posx,player.posy])
        elif player.mode == "cast2":
            screen.blit(fishmancast2,[player.posx,player.posy])
        elif player.mode == "fishing":
            screen.blit(fishmanfish,[player.posx,player.posy])

        #rendering and blitting score and timer
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        timedisp = font.render("Score:"+str(score)+"   Time:"+str(50-seconds),1,BLACK)
        screen.blit(timedisp,[550,20])
        if seconds == 50:
            gameon = 0
            gamestage = "finished"
            themeair.set_volume(1)
            themewater.set_volume(0)
            reeling.stop()
            reelingsoft.stop()
            water.stop()
            hs = open(tf,'r')
            hs.seek(0)
            currhighscore = int(hs.read())
            hs.close()
    #defining actions for various gamestages
    if gamestage == "menu":
        if menuselect == 0:
            pygame.draw.rect(screen,WHITE,[290,190,220,70])
        elif menuselect == 1:
            pygame.draw.rect(screen,WHITE,[290,340,220,70])
        pygame.draw.rect(screen,BLACK,[300,200,200,50])
        pygame.draw.rect(screen,BLACK,[300,350,200,50])
        screen.blit(menutext,[370,215])
        screen.blit(instructionstext,[340,365])
    elif gamestage == "sitting":
        player.mode = "sit"
        castcounter = 1
        castcounterchange = 1
        worm.movey = worm.omovey
    elif gamestage == "castingselect":
        castcounter += castcounterchange
        if castcounter > 100 or castcounter < 1:
            castcounterchange = castcounterchange * -1
        screen.blit(castboxborder,[castboxposx,castboxposy])
        pygame.draw.rect(screen,WHITE,[castboxposx+10,castboxposy+10,castcounter,20])
    elif gamestage == "casting":
        castanimatecounter += 1
        if castanimatecounter < 20:
            player.mode = "cast1"
        else:
            player.mode = "cast2"
            worm.posx += worm.movex
            worm.posy += worm.movey
            worm.movey += worm.grav
            screen.blit(worm.image,[worm.posx,worm.posy])
            pygame.draw.line(screen,WHITE,[player.posx+60,player.posy+10],[worm.posx+10,worm.posy+20])
            if worm.posy >= 50:
                sound2 = pygame.mixer.Channel(5)
                if not sound2.get_busy():
                    sound2.play(linewater)
            if worm.posy >= 100:
                themeair.set_volume(0)
                themewater.set_volume(1)
                gamestage = "sink"
    elif gamestage == "sink":
        player.mode = "fishing"
        worm.posy += worm.movey/6
        screen.blit(worm.image,[worm.posx,worm.posy])
        pygame.draw.line(screen,WHITE,[player.posx+60,player.posy+23],[worm.posx+10,worm.posy+20])
        if worm.posy > 560:
            gamestage = "failed"
    elif gamestage == "failed":
        screen.blit(worm.image,[worm.posx,worm.posy])
        pygame.draw.line(screen,WHITE,[player.posx+60,player.posy+23],[worm.posx+10,worm.posy+20])
    elif gamestage == "reeling":
        wormxdist = worm.posx - player.posx
        wormydist = worm.posy - player.posy
        wormdist = math.sqrt(wormxdist**2+wormydist**2)
        worm.posx += -int(5*wormxdist/wormdist)
        worm.posy += -int(5*wormydist/wormdist)
        screen.blit(worm.image,[worm.posx,worm.posy])
        pygame.draw.line(screen,WHITE,[player.posx+60,player.posy+23],[worm.posx+10,worm.posy+20])
        if worm.posy <= 90 and worm.posx <= 150:
            gamestage = "sitting"
            themeair.set_volume(1)
            themewater.set_volume(0)
            reelingsoft.stop()
    elif gamestage == "fight":
        f.mode = "caught"
        pygame.draw.line(screen,WHITE,[player.posx+60,player.posy+23],[f.posx+20,f.posy+30])
        screen.blit(castboxborder,[castboxposx,castboxposy])
        if f.CL > f.OL:
            pygame.draw.rect(screen,RED,[castboxposx+10+50,castboxposy+10,int((f.CL-f.OL)*50/14),20])
        elif f.CL < f.OL:
            pygame.draw.rect(screen,GREEN,[castboxposx+10+50,castboxposy+10,int((f.CL-f.OL)*50/14),20])
        pygame.draw.rect(screen,BLACK,[f.posx,f.posy,50,15])
        pygame.draw.rect(screen,RED,[f.posx+5,f.posy+5,f.force/iforce*40,5])
    elif gamestage == "catching":
        f.posx = 120
        f.posy = 30
        f.mode = "landed"
    elif gamestage == "end":
        reeling.stop()
        f = fish()
        f.mode = "free"
        f.movecounter = 0
        f.force = 2
        f.direct = math.pi/4
        f.lineforce = 1
        f.OL = math.sqrt(f.posx**2+f.posy**2)
        f.CL = f.OL
        f.rect = pygame.Rect(f.posx,f.posy,f.image.get_rect()[2],f.image.get_rect()[3])
        f.stretchfactor = 0

        #defining player
        player = fishman("player")
        player.posx = 110
        player.posy = 25
        player.mode = "sit"
        player.action = "none"

        #defining lure
        worm = lure()
        worm.rect = pygame.Rect(worm.posx,worm.posy,worm.image.get_rect()[2],worm.image.get_rect()[3])

        #bunch of variables
        castboxposx = 200
        castboxposy = 44

        castcounter = 1
        castcounterchange = 1

        castanimatecounter = 0

        gamestage = "sitting"
        gameon = 1
        themeair.set_volume(1)
        themewater.set_volume(0)
    elif gamestage == "finished":
        endtext = font.render("Yourscore:"+str(score),1,BLACK)
        if playagainselect == 0:
            pygame.draw.rect(screen,WHITE,[290,290,220,70])
        elif playagainselect == 1:
            pygame.draw.rect(screen,WHITE,[290,440,220,70])
        pygame.draw.rect(screen,BLACK,[300,300,200,50])
        pygame.draw.rect(screen,BLACK,[300,450,200,50])
        screen.blit(menutext,[370,315])
        screen.blit(playagaintext,[350,462])
        if currhighscore < score:
            hightext = font.render("NEW HIGHSCORE!",1,BLACK)
            hschange = open(tf,'w+')
            hschange.write(str(score))
            hschange.close()
        elif currhighscore >= score:
            hightext = font.render("Highscore:"+str(currhighscore),1,BLACK)
        screen.blit(hightext,[290,100])
        screen.blit(endtext,[290,130])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
