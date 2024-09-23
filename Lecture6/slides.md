## Lesson 6: Functions and random numbers

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Functions and random numbers
- **What will you learn today:**
  - How to define and use functions for modular code
  - What is a random number generator
  
---

## Recap: indentation

- Python uses indentation to define blocks of code.
- Convention states we use **4** spaces for indentation
- Consistent indentation is crucial for Python code to work correctly.

```python
if x > 5:
    print("x is greater than 5")
```

--

## Recap: the **for** loop

- range() generates a sequence of numbers, commonly used with for loops

```python
for i in range(5):
    print(i)
```

--

## Recap: Drawing the square using Pillow

```python
from PIL import Image, ImageDraw

im = Image.new('RGB', (640, 480), (255, 255, 20))
draw = ImageDraw.Draw(im)
draw.line( ( (0, 0), (100,0)), (0, 255, 255))
draw.line( ( (100, 0), (100,100)), (0, 255, 255))
draw.line( ( (100, 100), (0,100)), (0, 255, 255))
draw.line( ( (0, 100), (0,0)), (0, 255, 255))
im.show()
```

--

## Recap: Python variables

- Variables are containers for storing data values
- A variable is created the moment you first assign a value to it
```python
a = "Computer Animation & Visual Effects"
b = "2024"
print(a)
print(b) 
```

---

### Is there a way to simplify the code?

```python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (20, 20, 255)
origin_x = 0
origin_y = 0
points = [(origin_x, origin_y), (origin_x+100,origin_y), (origin_x+100,origin_y+100), (origin_x, origin_y+100)]
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[1], points[2]), draw_colour)
draw.line( ( points[2], points[3]), draw_colour)
draw.line( ( points[3], points[0]), draw_colour)
im.show()
```

---

## Pillow library and ImageDraw

- **Pillow** is an easy-to-use **Python Imaging Library** (PIL) fork for opening, manipulating, and saving images.
- **ImageDraw** is a module in the Pillow library that allows you to draw shapes, lines, and text on images.

--

## Drawing lines with line()

- The line() function is used to draw straight lines on an image.
- More specifically, it draws a polyline or line strip
- Syntax:

```python
draw.line(coordinates, line_colour, line_width)
```

--

## Example: line()

```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 300
w = 100
h = 50
draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), (255, 255, 0))
im.show()
```

--

## Drawing polygons with polygon()

- The polygon() function draws a closed shape by connecting multiple points
- Syntax:

```python
draw.polygon(coordinates, fill_colour, linecolour)
```

--

## Example: polygon() 

```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 300
w = 100
h = 50
draw.polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)), (100, 0, 20), (255, 255, 0))
im.show()
```

--

## Example: polygon() 

```python
from PIL import Image, ImageDraw

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 300
w = 100
h = 50
lc = (255, 255, 0) #Line colour
fc = (100, 0, 20) #Fill colour
draw.polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)), fc, lc)
im.show()
```

---

## Functions

- A **function** is a reusable block of code that performs a specific task.
  - Reduces redundancy by allowing you to define code once and use it multiple times.
- Analogy: Like a recipe – once you know how to make a dish, you can follow the same steps each time without reinventing it.

--

## Defining a Function

```python
def function_name(parameters):
    # Code block
    return result
```

- **def**: Keyword to define a function.
- **function_name**: The name of the function.
- **parameters**: Optional input values.
- **return**: Optional statement to return a value.

--

## Defining a Function: example

```python
def greet(name):
    return "Hello, " + name
```

- What it does?

--

## Calling a function

- To execute a function, you need to call it by its name.

```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))  # Output: Hello, Alice
```

--

## Function Parameters

- Parameters are variables that a function uses as input. When calling a function, arguments are passed to these parameters.

```python
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))  # Output: 8
```

- a and b are parameters, and 3 and 5 are the arguments passed during the function call.

--

## Return Statement

- The return statement sends a result back to the caller.
- A function can return multiple values as a tuple.

```python
def get_name_and_age():
    return "Alice", 30

name, age = get_name_and_age()
print(name, age)  # Output: Alice 30
```

---

## Using functions	

```python
from PIL import Image, ImageDraw

def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 300
w = 100
h = 50
drawBox(im, x, y, h, w, (255, 255, 0))
x = x + 10
y = y + 10
h += 1
w += 1
drawBox(im, x, y, h, w, (0, 255, 0))
x = x + 10
y = y + 10
h += 1
w += 1
drawBox(im, x, y, h, w, (0, 255, 255))

im.show()
```

--- 

## Loops and functions 1

```python
from PIL import Image, ImageDraw

def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 300
w = 100
h = 50
for x in (300, 320, 340, 360):
    drawBox(im, x, y, h, w, (255, 255, 0))
im.show()
```

--

## Loops and functions 2

```python
from PIL import Image, ImageDraw

def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 100
w = 100
h = 50
for x in (300, 320, 340, 360):
    y += 50
    h += 12
    w += 18
    drawBox(im, x, y, h, w, (255, 255, 0))
im.show()
```

--

## Loops and functions 3

```python
def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
w = 50
h = 50
y = 200
for x in range(1, 5):
    drawBox(im, x * 100, y, h, w, (255, 255, 0))
im.show()
```

--

## Loops and functions 4

```python
from PIL import Image, ImageDraw

def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
w = 50
h = 50
y = 200
for x in range(1, 5):
    for y in range(1, 5):
        drawBox(im, x * 100, y * 100, h, w, (255, 255, 0))
im.show()

```

---

## Recap: Procedural

- Procedural content creation implies the content is generated by an **algorithm**
- Content can be handcrafted or procedural
  - Handcrafted is more expensive, but more controllable
  - Procedural is cheaper for large scale, but designing algorithm for anything non-trivial is hard

--

## Procedural content in games

- Procedural content generation has been a part of videogames for many years
  - Level generation was an early feature of games when memory and storage were limited
  - Random generation as a tradeoff between memory and processor

--

## Pseudo-random

- **Pseudo-random number generator** algorithm creates sequence of numbers that are "close enough" to random
- The "randomness" of the sequence depends on the **seed**
  - The first number in the sequence
- Most algorithms produce the sequence of **integers**
  - Other types can be obtained by using extra maths on top of the sequence

---

## Random numbers in Python

- the **random** module: a set of functions that generate or manipulate random numbers
- **random()** function generates a random float number between 0.0 and 1.0
```python
from random import random
num = random()
print(num)
```

--

## Random numbers in Python

- **uniform(a,b)**: Return a floating point random number between *lower* and *upper*
- **randint(a, b)**: Returns a random integer N such that `$$a <= N <= b $$`.
- **choice(arg)**: Returns a random item from a list, tuple or string *arg*

```python
from random import random

# Random integer between 1 and 10 (inclusive)
random_int = randint(1, 10)
print(random_int)
```

---

## Loops and functions and random 1

```python
from PIL import Image, ImageDraw
from random import randint

def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
for x in range(1, 5):
    for y in range(1, 5):
        h = randint(20, 60)
        w = randint(20, 60)
        drawBox(im, x * 100, y * 100, h, w, (255, 255, 0))
im.show()
```

--

## Loops and functions and random 2

```python
from PIL import Image, ImageDraw
from random import randint

def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
for x in range(1, 5):
    for y in range(1, 5):
        h = randint(20, 60)
        w = randint(20, 60)
        c = (randint(0, 256), randint(0, 256), randint(0, 256))
        drawBox(im, x * 100, y * 100, h, w, c)
im.show()
```

--

## Loops and functions and random 3

```python
ffrom PIL import Image, ImageDraw
from random import randint

def drawHollowBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

def drawSolidBox(im, x, y, h, w, c):
    draw.polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)), c, c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
for x in range(1, 5):
    for y in range(1, 5):
        h = randint(20, 60)
        w = randint(20, 60)
        c = (randint(0, 256), randint(0, 256), randint(0, 256))
        drawSolidBox(im, x * 100, y * 100, h, w, c)
im.show()
```

---

## Bringing it all together
```python
from PIL import Image, ImageDraw
from random import randint

def drawHollowBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)

def drawSolidBox(im, x, y, h, w, c):
    draw.polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)), c, c)

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
for x in range(1, 5):
    for y in range(1, 5):
        h = randint(20, 60)
        w = randint(20, 60)
        c = (randint(0, 256), randint(0, 256), randint(0, 256))
        selector = randint(0,1)
        if selector == 1:
            drawSolidBox(im, x * 100, y * 100, h, w, c)
        else:
            drawHollowBox(im, x * 100, y * 100, h, w, c)
im.show()
```

---

# Conclusion

- **What have you learned today**
  - Functions from Pillow library allowiing to draw lines and polygons
  - How to define functions
  - **random** module for procedural content creation
- **Homework**
  - Can you generate multiple triangles? How about other shapes? 
  
--

# Next time

- **What will you learn next time**
  - Vectors and why they are important in graphics


--

# Q&A and discussion
- **Open Floor for Questions**
