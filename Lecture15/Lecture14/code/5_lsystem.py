#!/usr/bin/env python
import pygame  # we will need core pygame functionality
import pygame.draw  # this module will be needed for drawing on the screen

import random
import math

def generate_rule_string(axiom: str, rules: dict[str, str], iterations: int) -> str:
    """
    Generates a rule string based on the given axiom, rules, and number of iterations.

    Args:
        axiom (str): The initial string to start the generation process.
        rules (dict[str, str]): A dictionary where keys are characters in the axiom and values are the replacement strings.
        iterations (int): The number of iterations to apply the rules.

    Returns:
        str: The generated rule string after applying the rules for the specified number of iterations.
    """
    derived = [axiom]  # this is the first seed
    for _ in range(iterations):  # now loop for each iteration
        next_sequence = derived[-1]  # grab the last rule
        next_axiom = [
            rule(char, rules) for char in next_sequence
        ]  # for each element in the rule expand
        derived.append(
            "".join(next_axiom)
        )  # append to the list, we will only need the last element
    return derived


def rule(sequence: str, rules: dict[str, str]) -> str:
    """
    Applies the given rules to the sequence.

    Args:
        sequence (str): The initial string to which the rules will be applied.
        rules (dict[str, str]): A dictionary where keys are characters in the sequence and values are the replacement strings.

    Returns:
        str: The resulting string after applying the rules to the sequence.
    """
    if sequence in rules:
        return rules[sequence]
    return sequence


def draw_lsystem(screen, position: tuple, orientation: float, commands: str, length: float, angle: float) -> None:
    """
    Draws an L-system based on the given commands.

    Args:
        turtle (Turtle): The turtle object used to draw the L-system.
        commands (str): The string of commands to control the turtle.
        length (float): The length of each step the turtle takes.
        angle (float): The angle by which the turtle turns.

    Returns:
        None
    """
    stack = []
    for command in commands:
        if command in ["F", "G", "R", "L", "A"]:  # forward rules for some l system grammars
            directionX = math.cos(orientation)*length
            directionY = math.sin(orientation)*length
            newPosition = (position[0]+directionX, position[1]+directionY)
            pygame.draw.line(screen, (255, 255, 255), position, newPosition, 1)
            position = newPosition
        elif command in ["f", "B"]:
            directionX = math.cos(orientation)*length
            directionY = math.sin(orientation)*length
            newPosition = (position[0]+directionX, position[1]+directionY)
            position = newPosition
        elif command == "+":
            orientation += angle
        elif command == "-":
            orientation -= angle
        elif command == "[":
            stack.append((position, orientation))  # save turtle values
        elif command == "]":
            position, orientation = stack.pop()


# F -> Forward
# X -> A place holder for movements
# [ push position and direction onto stack
# ] pop position and direction back to turtle
# + Turn Left
# - Turn Right

pygame.init()   #this is an essential line to make pygame working

width = 640     #width of the game window
height = 480    #height of the game window
screen = pygame.display.set_mode((width, height)) #create the game window
clock = pygame.time.Clock() #use the clock to ensure we updating the window not too often 
running = True  #the variable to ensure the game loop
white = (255,255,255)
black = (0,0,0)

max_iterations = 8
iterations = 1 

axiom = "X"  # start
rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}  # fern

#the game loop
while running:
    screen.fill(black) #clear the window by filling the space with the background colour
    #draw two lines
    length = 8/iterations  
    angle = math.radians(25)  # change this to make different shapes
    g = generate_rule_string(axiom, rules, iterations)
    draw_lsystem(screen, (320, 470), math.radians(-90), g[-1], length, angle)
    if iterations < max_iterations:
        iterations += 1 
    #event management
    for event in pygame.event.get(): #if we received an event
        if event.type == pygame.QUIT: #if the event is "quit game"
            running = False         #then we set the variable allowing for the loop to stop
    pygame.display.flip()       #render
    clock.tick(1)              #wait until we run with 30 frames per second or less
#end of the program

