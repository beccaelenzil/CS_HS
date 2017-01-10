import pygame
import random
import math
pygame.init()
BLACK = [0,0,0]
WHITE = [255,255,255]
screen = pygame.display.set_mode([800,600])

fish = pygame.image.load("graphics/fish.png").convert()
background_image = pygame.image.load("graphics/lake.jpg").convert()
fish.set_colorkey(BLACK)
clock = pygame.time.Clock()
done = False
fx = 400
fy = 300
count = 200

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    linethick = int((1000-math.sqrt(fx**2+fy**2))/100)
    count += 1
    if fx >= 759 or fy >= 559 or fx <= 1 or fy <= 1:
        direct = random.randint(0,359)
    if count >= 200:
        count = 0
        direct = random.randint(0,359)
    fx += math.cos(direct)
    fy += math.sin(direct)
    screen.blit(background_image,[0,0])
    pygame.draw.circle(screen,WHITE,[0,0],20)
    pygame.draw.line(screen,WHITE,[0,0],[fx,fy],linethick)
    screen.blit(fish,[fx-40,fy-40])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
