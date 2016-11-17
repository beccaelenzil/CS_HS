import random
import time
import pygame
from SegModelSimImpDislay import *

width = 50
height = 50
cell_size = 5
spacing = 1
Type1prob = .35
Type2prob = .35
TypeStoreprob = .16
Threshhold = .5
Storeradius = 5
Storethresh = (2*Storeradius)*(2*Storeradius-1.5)

# Define some colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
screen_width = height*(cell_size+spacing)
screen_height = width*(cell_size+spacing)

pygame.init()

# Set the width and height of the screen [width, height]
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Segregation Model")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def drawBoard(A):
    #A = createBoard(width,height)
    for row in range(height):
        x_pos = (cell_size*row)+(spacing*(row+1))
        for col in range(width):
            y_pos = (cell_size*col)+(spacing*(col+1))
            if A[row][col] == 1:
                pygame.draw.rect(screen, RED, [x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == 2:
                pygame.draw.rect(screen, BLUE,[x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == 3:
                pygame.draw.rect(screen, GREEN,[x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == 0:
                pygame.draw.rect(screen, WHITE,[x_pos,y_pos,cell_size,cell_size])
            elif A[row][col] == -1:
                pygame.draw.rect(screen, BLACK,[x_pos,y_pos,cell_size,cell_size])

A = randomCells(width,height,Type1prob,Type2prob,TypeStoreprob)
drawBoard(A)
pygame.display.flip()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    A = next_life_generation(A,Threshhold,Storeradius,Storethresh)
    drawBoard(A)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    #clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
