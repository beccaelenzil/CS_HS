import pygame
pygame.init()
import math
BLACK    = (   0,   0,   0)
GREY     = ( 100, 100, 100)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (750,500)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLUE)
    pygame.draw.rect(screen,GREY,[0,300,750,500],0)
    a = 0
    while a < 700:
        h = int(130*(math.sin(a)))
        pointlist1 = [[a+20,185+h],[a+23,185+h],[a+23,190+h],[a+20,190+h]]
        pointlist2 = [[a+23,187+h],[a+26,187+h],[a+26,185+h],[a+26,190+h],[a+26,187+h],[a+27,187+h]]
        pygame.draw.ellipse(screen,BLUE,[a+10,250,175,100],0)
        pygame.draw.rect(screen,RED,[a+15,180+h,3,15])
        pygame.draw.circle(screen,BLACK,[a+14,185+h],2)
        pygame.draw.circle(screen,BLACK,[a+14,190+h],2)
        pygame.draw.lines(screen,GREEN,False,pointlist1,1)
        pygame.draw.lines(screen,GREEN,False,pointlist2,1)
        pygame.draw.circle(screen,GREEN,[a+29,187+h],2)
        a += 185
    clock.tick(60)
    pygame.display.flip()
