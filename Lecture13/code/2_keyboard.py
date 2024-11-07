#!/usr/bin/python3
import pygame   #we will need core pygame functionality
import pygame.draw #this module will be needed for drawing on the screen

pygame.init()   #this is an essential line to make pygame working

width = 640     #width of the game window
height = 480    #height of the game window
screen = pygame.display.set_mode((width, height)) #create the game window
clock = pygame.time.Clock() #use the clock to ensure we updating the window not too often 
running = True  #the variable to ensure the game loop
white = (255,255,255)
black = (0,0,0)

posX = 0
posY = 0

#the game loop
while running:
    screen.fill(black) #clear the window by filling the space with the background colour
    #draw two lines
    pygame.draw.line(screen, white, (posX,posY), (posX+20,posY+20), 10) 
    pygame.draw.line(screen, white, (posX+20,posY+0), (posX+0,posY+20), 10)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        posY = posY - 1
    if key[pygame.K_DOWN]:
        posY = posY + 1
    if key[pygame.K_RIGHT]:
        posX = posX + 1
    if key[pygame.K_LEFT]:
        posX = posX - 1
    #event management
    for event in pygame.event.get(): #if we received an event
        if event.type == pygame.QUIT: #if the event is "quit game"
            running = False         #then we set the variable allowing for the loop to stop
    pygame.display.flip()       #render
    clock.tick(30)              #wait until we run with 30 frames per second or less
#end of the program    