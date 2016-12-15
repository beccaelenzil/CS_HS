import pygame
pygame.init()
BLACK = [0,0,0]
WHITE = [255,255,255]
screen = pygame.display.set_mode([800,600])

def draw_log(screen,x,y):
    pygame.draw.circle(screen,WHITE,[x-15,y],5,2)
    pygame.draw.circle(screen,WHITE,[x+15,y],5,2)
    pygame.draw.line(screen,WHITE,[x-15,y-5],[x+15,y-5],2)
    pygame.draw.line(screen,WHITE,[x-15,y+3],[x+15,y+3],2)

def draw_tree(screen,x,y):
    pointlist1 = [[x,y+10],[x,y],[x-4,y+4],[x+4,y+4],[x,y]]
    pointlist2 = [[x-4,y],[x+4,y],[x,y-5]]
    pygame.draw.lines(screen,WHITE,False,pointlist1,2)
    pygame.draw.lines(screen,WHITE,True,pointlist2,2)
tx = 200
ty = 200
xspeed = 0
yspeed = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yspeed += -1
            elif event.key == pygame.K_a:
                xspeed += -1
            elif event.key == pygame.K_d:
                xspeed += 1
            elif event.key == pygame.K_s:
                yspeed += 1
    screen.fill(BLACK)
    if tx >= 795 and xspeed > 0:
        xspeed = xspeed*-1
    if tx <= 5 and xspeed < 0:
        xspeed = xspeed*-1
    if ty >= 590 and yspeed > 0 :
        yspeed = yspeed*-1
    if ty <= 5 and yspeed < 0 :
        yspeed = yspeed*-1
    tx += xspeed
    ty += yspeed
    draw_tree(screen,tx,ty)
    pos = pygame.mouse.get_pos()
    lx = pos[0]
    ly = pos[1]
    draw_log(screen,lx,ly)
    pygame.mouse.set_visible(False)
    pygame.display.flip()

pygame.quit()
