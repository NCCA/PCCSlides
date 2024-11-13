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
    "liquidWater",
    "bridgeLogs",
]

sprite_images = []
for spriteName in sprites:
    filename = "base/" + spriteName + ".png"
    try:
        loadedImage = pygame.image.load(filename)
        sprite_images.append(loadedImage)
    except FileNotFoundError:
        print("File base/liquidWater.png is not found")

levelElements = ["water", "island"]
grid = []
for x in range (10):
    gridrow = []
    for y in range(10):
        gridrow.append("water")
    grid.append(gridrow)

for i in range(10):
    posX = random.randint(0, 10)
    posY = random.randint(0, 10)
    grid[posX][posY] = "island"

# the game loop
while running:
    screen.fill(
        black
    )  # clear the window by filling the space with the background colour

    for x in range (0, 10):
        for y in range (0, 10):
            screen.blit(sprite_images[0], (x*70, y*70))
            if (grid[x][y] == "island"):
                screen.blit(sprite_images[1], (x*70, y*70))

    # event management
    for event in pygame.event.get():  # if we received an event
        if event.type == pygame.QUIT:  # if the event is "quit game"
            running = False  # then we set the variable allowing for the loop to stop
    pygame.display.flip()  # render
    clock.tick(30)  # wait until we run with 30 frames per second or less
# end of the program
