#!/usr/bin/python3
import pygame   #we will need core pygame functionality
import pygame.draw #this module will be needed for drawing on the screen

sprites = ["lollipopFruitGreen", "lollipopFruitRed", "lollipopFruitYellow", "lollipopGreen", "lollipopRed", "lollipopWhiteGreen", "lollipopWhiteRed"]

pygame.init()   #this is an essential line to make pygame working

width = 640     #width of the game window
height = 480    #height of the game window
screen = pygame.display.set_mode((width, height)) #create the game window
clock = pygame.time.Clock() #use the clock to ensure we updating the window not too often 
running = True  #the variable to ensure the game loop
black = (0,0,0)

sprite_images = []
for spriteName in sprites:
    filename = "candy/"+spriteName+".png"
    loadedImage = pygame.image.load(filename)
    sprite_images.append(loadedImage)

#the game loop
while running:
    screen.fill(black) #clear the window by filling the space with the background colour
    
    x = 0
    y = 0
    for spriteImage in sprite_images:
        screen.blit(spriteImage, (x, y))
        x = x+80
        y = y+50

    #event management
    for event in pygame.event.get(): #if we received an event
        if event.type == pygame.QUIT: #if the event is "quit game"
            running = False         #then we set the variable allowing for the loop to stop
    pygame.display.flip()       #render
    clock.tick(30)              #wait until we run with 30 frames per second or less
#end of the program    