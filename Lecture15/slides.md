## Lesson 14: Procedural game content creation

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Procedural game content creation
- **What will you learn today:**
  - More insight about pygame library 
  - Procedural level design with Pygame

---

## Recap: Procedural content

- A procedure is the instruction or set of instructions to be executed
- Content can be anything we are presenting to the user
- In games the term is known as *Procedural Content Generation*

--

## Recap: Random numbers and random library

- Random module: *import random*
- *random.randint(a, b)*: Returns a random integer between a and b.
- *random.choice(list): Chooses a random element from a list.*

```python
import random
x = random.randint(0, 800)
y = random.randint(0, 600)
```

---

## Types of Procedural Content Generation
- **Random Generation**: Using random values to place objects and create unpredictable layouts.
- **Noise Functions**: Using noise for organic patterns (e.g. terrain generation).
- **Cellular Automata**: Algorithms that use cells to create complex systems (used in caves or dungeons).
- **Rule-Based Systems**: Predefined rules to create structured content.

---

## Recap: Pygame

[1_start.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture14/code/1_start.py)

```python
#!/usr/bin/env python3
import pygame  # we will need core pygame functionality
import pygame.draw  # this module will be needed for drawing on the screen

pygame.init()  # this is an essential line to make pygame working

width = 700  # width of the game window
height = 700  # height of the game window
screen = pygame.display.set_mode((width, height))  # create the game window
clock = (
    pygame.time.Clock()
)  # use the clock to ensure we updating the window not too often
running = True  # the variable to ensure the game loop
black = (0, 0, 0)

try:
    spriteWater = pygame.image.load("base/liquidWater.png")
except FileNotFoundError:
    print("File base/liquidWater.png is not found")

# the game loop
while running:
    screen.fill(
        black
    )  # clear the window by filling the space with the background colour

    for x in range (0, 700, 70):
        for y in range (0, 700, 70):
            screen.blit(spriteWater, (x, y))

    # event management
    for event in pygame.event.get():  # if we received an event
        if event.type == pygame.QUIT:  # if the event is "quit game"
            running = False  # then we set the variable allowing for the loop to stop
    pygame.display.flip()  # render
    clock.tick(30)  # wait until we run with 30 frames per second or less
# end of the program
```

---

## Grid-based random generation

- The screen is divided into a grid
  - Normally stored as a list of lists
- Obstacles, collectibles, etc are placed randomly

--

## Grid-based random generation, example

[2_random.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture14/code/2_random.py)

```python
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
        gridrow.append(random.choice(levelElements))
    grid.append(gridrow)

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
```

--

## Procedural object placement

- Place items / elements / etc in random locations
- Avoid clusters by checking proximity 

[3_sampling.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture14/code/3_sampling.py)

```python
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
```

--

## Adding prefabs

- Grid-based methods work for larger objects
  - Prefabs are predefined structures
- You modify more than one cell
- Prefabs do not have to be rectanular

```python
grid = []
for x in range (10):
    gridrow = []
    for y in range(10):
        gridrow.append(0)
    grid.append(gridrow)

for i in range(10):
    posX = random.randint(0, 7) # 10-3 = 7
    posY = random.randint(0, 8) # 10-2 = 8
    grid[posX][posY] = 2
    grid[posX+1][posY] = 3
    grid[posX+2][posY] = 4
    grid[posX][posY+1] = 5
    grid[posX+1][posY+1] = 5
    grid[posX+2][posY+1] = 5
```

--

### Modifying the code by adding extra conditions

- While placing objects randomly we might want to check if the place is not previously occupied

[3_prefabs.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture14/code/3_prefabs.py)

```python
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
```

---

## Noise-based procedural generation

- Noise *functions* interpolate random values
- Classic noise functions: *Perlin Noise*, *Simplex Noise*
- Noise functions create natural patterns:

<img style="border: 0;" src="images/terrain.png" width="30%">

---

## Cellular automata

- Cellular automata is a grid of cells, each in one of a finite number of states
- At each iteration, the cell can change its state based on some fixed rule
- Classic example is <a href = "https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's game of life</a>

<img style="border: 0;" src="images/gameoflife.gif" width="30%">

---

## Rule-based systems

- Cellular automata is an example of rule-based systems
- We define the rule, we follow the rule until we hit the stopping condition

--

## Drunkard walk algorithm

- Example of rule-based system
  - Start at a random cell
  - Randomly move in one direction
  - Stop when a predefined number of steps have been taken

--

### Drunkard walk algorithm example

[3_walk.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture14/code/3_walk.py)

```python
posX = random.randint(0, 10)
posY = random.randint(0, 10)
walkDirections = ["left", "right", "up", "down"]
canWalk = True
while canWalk:
    grid[posX][posY] = "island"
    newDirection = random.choice(walkDirections)
    if newDirection == "left":
        posX = posX - 1
    if newDirection == "right":
        posX = posX + 1
    if newDirection == "up":
        posY = posY - 1
    if newDirection == "down":
        posY = posY + 1
    if posX < 0 or posY < 0 or posX >= 10 or posY >= 10:
        canWalk = False
```

--

## More rule-based systems

- L-System (https://en.wikipedia.org/wiki/L-system) allows to describe fractal-like forms
- Used to generate plants
- But before let we learn one more data type in Python

---

## Data types

- Python has 5 standard data types
  1. Numbers
  2. String
  3. List
  4. Tuple
  5. **Dictionary**

--

## Dictionaries in Python

- A **dictionary** is a collection of key-value pairs where each key is associated with a specific value.
- Unlike lists, dictionaries are unordered and accessed by keys, not indices.

```python
student = {"name": "Alice", "age": 20, "courses": ["Animation", "Effects"]}
```

--

## Characteristics of dictionaries

- Keys must be unique and immutable (e.g., strings, numbers, or tuples).
- Values can be of any data type, including lists or other dictionaries.
- Create a dictionary: with curly braces {} or using the dict() function.

```python
 # Using {}
car = {"brand": "Toyota", "year": 2020}

 # Using dict()
car = dict(brand="Toyota", year=2020)
```

--

## Elements in dictionaries

- Access values using their key with square brackets [] or get() method.
- Use [] or update() to add a new key-value pair or update an existing one.
- Use del to remove by key or pop() to remove and return a value.
```python
print(car["brand"])      # Output: Toyota
print(car.get("year"))   # Output: 2020
car["colour"] = "blue"  # Add new key-value pair
car["year"] = 2021     # Update existing value
del car["brand"]
year = car.pop("year")
```

---

## L-systems

- **Lindenmayer System (L-System)**: A mathematical system to model the growth processes of plants and other natural forms.
- Key Components of an L-System:
  - **Alphabet**: Set of symbols used in the system.
  - **Axiom**: Initial string or starting point of the system.
  - **Rules**: Define how each symbol in the alphabet is replaced iteratively.

--

## How L-systems work
- Start with an axiom (initial string).
- Apply production rules iteratively to evolve the axiom into more complex forms.
- Example: Axiom: **A**, Rule: **A → AB** and **B → A**
- Iterations: 1. A,  2. AB, 3. ABA, 4. ABAAB

--

## L-systems: example

- Fern: 
  - Axiom = "X"  
  - Rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}  

--

## L-systems: Pygame example

[5_lsystem.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture14/code/3_lsystem.py)

```python
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

```

---

### Best practices for procedural game content generation

- Keep code modular for easier tweaks and testing
- Test generated content to ensure playability
- Experiment with different algorithms
  - The same task can be solved with a different algorithm!

--

## Next steps in PCG

- Explore more algorithms
  - http://pcg.wikidot.com/start
- Combine algorithms

---

# Conclusion

- **What have you learned today**
  - Dictionary data type
  - Various algorithms for procedural game content generation
- **Homework**
  - Can use L-systems for generating something grid-based?
  - In generak, the material from previous and this lessons is enough to kick-off with the coursework. 

--

# Next time

- **What will you learn next time**
  - Structuring the code with classes
  - Project management

--

# Q&A and discussion
- **Open Floor for Questions**

