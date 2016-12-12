import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()
background_position = [0,0]
background_image = pygame.image.load("lake.jpg").convert()
player_image = pygame.image.load("fish.png").convert()
player_image.set_colorkey(BLACK)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background_image,background_position)
    screen.blit(player_image,pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
