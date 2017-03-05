import pygame
pygame.init()
pygame.mixer.init()
water = pygame.mixer.Sound('sounds/themeair.ogg')
screen=pygame.display.set_mode((400,400),0,32)
done = False
water.play()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True

