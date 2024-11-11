#!/usr/bin/env python3
import math  # using floor function from this library
import os  # note previous lecture: this will be needed to get all the files in a directory

import pygame  # we will need core pygame functionality
import pygame.draw  # this module will be needed for drawing on the screen


def justifyPosition(x, y) -> tuple:
    # this function rounds the value to a multiple of 70 (the size of the sprite)
    # it divides by 70, finds closest smallest integer and multiplies back
    xCell = math.floor(x / 70)
    yCell = math.floor(y / 70)
    return (xCell * 70, yCell * 70)


pygame.init()  # this is an essential line to make pygame working

width = 700  # width of the game window, multiple of 70 because of the sprite size
height = 490  # height of the game window, multiple of 70 because of hte sprite size
screen = pygame.display.set_mode((width, height))  # create the game window
clock = (
    pygame.time.Clock()
)  # use the clock to ensure we updating the window not too often
running = True  # the variable to ensure the game loop
black = (0, 0, 0)
white = (255, 255, 255)

# loading all the sprites from directory candy
file_list = os.listdir("candy/")
sprites = []
for filename in file_list:
    try:
        loadedImage = pygame.image.load("candy/" + filename)
        sprites.append(loadedImage)
    except FileNotFoundError:
        print("Sprite " + filename + " is not loaded")

currentSprite = -1
sprite_count = len(sprites)

# this list will be used for sprites we keep on the screen
levelSprites = []

# the game loop
while running:
    screen.fill(
        black
    )  # clear the window by filling the space with the background colour

    for item in levelSprites:
        spriteImage = sprites[item[2]]
        screen.blit(spriteImage, (item[0], item[1]))

    mouse_pos = pygame.mouse.get_pos()
    posX = mouse_pos[0]
    posY = mouse_pos[1]
    posScreen = justifyPosition(posX, posY)
    posX = posScreen[0]
    posY = posScreen[1]

    if currentSprite >= 0:
        spriteImage = sprites[currentSprite]
        screen.blit(spriteImage, posScreen)
    else:
        pygame.draw.line(screen, white, (posX, posY), (posX + 70, posY + 70), 10)
        pygame.draw.line(screen, white, (posX + 70, posY), (posX, posY + 70), 10)

    # event management
    for event in pygame.event.get():  # if we received an event
        if event.type == pygame.QUIT:  # if the event is "quit game"
            running = False  # then we set the variable allowing for the loop to stop
        if (
            event.type == pygame.KEYUP
        ):  # we use event handling not key_pressed, because we need to check when the key is pressed AND released
            if event.key == pygame.K_RIGHT and currentSprite < (sprite_count - 1):
                currentSprite = currentSprite + 1
            if event.key == pygame.K_LEFT and currentSprite > 0:
                currentSprite = currentSprite - 1
            if event.key == pygame.K_SPACE and currentSprite >= 0:
                levelSprites.append((posX, posY, currentSprite))

    pygame.display.flip()  # render
    clock.tick(30)  # wait until we run with 30 frames per second or less
# end of the program
