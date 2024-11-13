#!/usr/bin/env python3
import pygame  # we will need core pygame functionality
import pygame.draw  # this module will be needed for drawing on the screen
import random

pygame.init()  # this is an essential line to make pygame working

width = 700  # width of the game window
height = 700  # height of the game window
screen = pygame.display.set_mode((width, height))  # create the game window
clock = (
    pygame.time.Clock()
)  # use the clock to ensure we updating the window not too often
running = True  # the variable to ensure the game loop
black = (0, 0, 0)

sprites = [
    "liquidWater", #0
    "bridgeLogs",  #1
    "sandLeft",    #2
    "sandMid",     #3
    "sandRight",   #4
    "sandCenter",  #5
]

sprite_images = []
for spriteName in sprites:
    filename = "base/" + spriteName + ".png"
    try:
        loadedImage = pygame.image.load(filename)
        sprite_images.append(loadedImage)
    except FileNotFoundError:
        print("File base/liquidWater.png is not found")

grid = []
for x in range (10):
    gridrow = []
    for y in range(10):
        gridrow.append(0)
    grid.append(gridrow)

for i in range(10):
    posX = random.randint(0, 7) # 10-3 = 7
    posY = random.randint(0, 8) # 10-2 = 8
    if grid[posX][posY] == 0 and grid[posX+1][posY] == 0 and grid[posX+2][posY] == 0 and grid[posX][posY+1] == 0 and grid[posX+1][posY+1]==0 and grid[posX+2][posY+1]==0:
        #place the island only if the space has not been taken before
        grid[posX][posY] = 2
        grid[posX+1][posY] = 3
        grid[posX+2][posY] = 4
        grid[posX][posY+1] = 5
        grid[posX+1][posY+1] = 5
        grid[posX+2][posY+1] = 5

# the game loop
while running:
    screen.fill(
        black
    )  # clear the window by filling the space with the background colour

    for x in range (0, 10):
        for y in range (0, 10):
            screen.blit(sprite_images[0], (x*70, y*70))
            spriteID = grid[x][y]
            screen.blit(sprite_images[spriteID], (x*70, y*70))

    # event management
    for event in pygame.event.get():  # if we received an event
        if event.type == pygame.QUIT:  # if the event is "quit game"
            running = False  # then we set the variable allowing for the loop to stop
    pygame.display.flip()  # render
    clock.tick(30)  # wait until we run with 30 frames per second or less
# end of the program
