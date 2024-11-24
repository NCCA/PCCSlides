#!/usr/bin/env python3
import pygame  # we will need core pygame functionality
import pygame.draw  # this module will be needed for drawing on the screen
from bouncingball import BouncingBall as BouncingBall

pygame.init()  # this is an essential line to make pygame working

width = 640  # width of the game window
height = 480  # height of the game window
screen = pygame.display.set_mode((width, height))  # create the game window
clock = (
    pygame.time.Clock()
)  # use the clock to ensure we updating the window not too often
running = True  # the variable to ensure the game loop
white = (255, 255, 255)
black = (0, 0, 0)

ball1 = BouncingBall(20, (20,20), (10,0))
ball2 = BouncingBall(20, (620,20), (-100,100))
ball1.setBounds(0, 0, width, height)
ball2.setBounds(0, 0, width, height)

# the game loop
while running:
    screen.fill(
        black
    )  # clear the window by filling the space with the background colour
    # draw two lines
    deltaT = float(clock.get_time())/1000.0
    ball1.draw(screen, white)
    ball2.draw(screen, white)
    ball1.update(deltaT)
    ball2.update(deltaT)

    # event management
    for event in pygame.event.get():  # if we received an event
        if event.type == pygame.QUIT:  # if the event is "quit game"
            running = False  # then we set the variable allowing for the loop to stop
    pygame.display.flip()  # render
    clock.tick(30)  # wait until we run with 30 frames per second or less
# end of the program
