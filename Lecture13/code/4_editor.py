#!/usr/bin/python3
import pygame   #we will need core pygame functionality
import pygame.draw #this module will be needed for drawing on the screen

def draw_shape(screen, x, y, colour):
    pygame.draw.line(screen, colour, (x,y), (x+20,y+20), 10) 
    pygame.draw.line(screen, colour, (x+20,y+0), (x+0,y+20), 10)

pygame.init()   #this is an essential line to make pygame working

width = 640     #width of the game window
height = 480    #height of the game window
screen = pygame.display.set_mode((width, height)) #create the game window
clock = pygame.time.Clock() #use the clock to ensure we updating the window not too often 
running = True  #the variable to ensure the game loop
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

posX = 0
posY = 0

cursorList = []

#the game loop
while running:
    screen.fill(black) #clear the window by filling the space with the background colour
    
    for item in cursorList:
        draw_shape(screen, item[0], item[1], white)

    #set position of the cross to be the position of the mouse cursor
    mouse_pos = pygame.mouse.get_pos()
    posX = mouse_pos[0]
    posY = mouse_pos[1]

    #if left mouse button is pressed, change the drawing colour to red
    key = pygame.mouse.get_pressed()
    if key[0]:
        cursorList.append((posX, posY))
        draw_shape(screen, posX, posY, red)
    else:
        draw_shape(screen, posX, posY, white)

    #event management
    for event in pygame.event.get(): #if we received an event
        if event.type == pygame.QUIT: #if the event is "quit game"
            running = False         #then we set the variable allowing for the loop to stop
    pygame.display.flip()       #render
    clock.tick(30)              #wait until we run with 30 frames per second or less
#end of the program    