## Lesson 7: Vector and lines

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Vector and lines
- **What will you learn today:**
  - What is a vector
  - Why we need to know vectors to draw lines

---

## Recap: functions

- A **function** is a reusable block of code that performs a specific task.
- Parameters are variables that a function uses as input. When calling a function, arguments are passed to these parameters.

```python
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))  # Output: 8
```

--

## Recap: loops

- The for loop iterates over a sequence (such as a list, tuple, string, or range)
- range() generates a sequence of numbers, commonly used with for loops

```python
for i in range(5):
    print(i)
```

--

## Recap: data types

- Python has 5 standard data types
  1. **Numbers**: 1, 0.5, -3.14
  2. **String**: "Hello, students"
  3. **List**: ["animation", "effects", "games", "animation"]
  4. Tuple
  5. Dictionary

---

## Tuples

- Python **tuple** is a collection of objects separated by commas.
- It is similar to lists, but not the same!
```python
var = ("Computer", "Animation", "Visual", "Effects")
print(var)
```

--

## Tuple with one item

- In case your generating a tuple with a single element, make sure to add a comma after the element. 

```python
#One-item tuple
mytuple = ("Animation",)
print(type(mytuple))
 
#NOT a tuple
mytuple = ("Animation")
print(type(mytuple))
```

--

## Tuple vs List

- Tuples are **ordered** and **immutable**
  - You cannot add items to a tuple once it is created.
  - You can only read elements, not change them
  - You cannot remove items from tuple once it is created.
  
```python
var = ("Computer", "Animation", "Visual", "Effects")
print(var[1]) # prints Animation
var[1]="Graphics" # generates error
```

--

## Accessing values in tuples

- There are two ways to access the elements of a tuple: 
  - Using a positive index
  - Using a negative index

```python
var = ("Computer", "Animation", "Visual", "Effects")
print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[1] = ", var[2])
print("Value in Var[2] = ", var[3])
print("Value in Var[-1] = ", var[-1])
print("Value in Var[-2] = ", var[-2])
print("Value in Var[-3] = ", var[-3])
print("Value in Var[-3] = ", var[-4])
```

---

## Tuples in graphics

```python
from PIL import Image, ImageDraw
image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
canvas.line(((100, 100), (250, 50)), (0, 255, 255))
image.show()
```

- We already used tuples: image resolution, colours, coordinates

---

# Vectors

- Did you have vectors at school?

<iframe width="100%" height="800" src="https://immersivemath.com/ila/ch02_vectors/ch02.html#fig_vec_breakout"></iframe>

--

## Vector: a definition

- A **vector** is a quantity that has length and direction
- A geometric vector is defined by a directed line segment

<img style="border: 0;" src="images/Desc1.png" width="15%">
<img style="border: 0;" src="images/Picture1.png" width="15%">
<img style="border: 0;" src="images/Desc2.png" width="15%">
<img style="border: 0;" src="images/Picture2.png" width="15%">
<img style="border: 0;" src="images/Desc3.png" width="15%">
<img style="border: 0;" src="images/Picture3.png" width="15%">

--

## Vector: properties

- A **vector** is a quantity that has length and direction
  - Vectors are not defined by starting position
  - Vectors are essentially displacements
- Vectors with the same direction are parallel line segments

--

## Position vs direction

- A point defines the location
  - Defined by coordinates
- A vector defines the direction
  - For example, direction from the origin to another point

![Position Vector](images/PositionVector.png)

--

## Position vs direction

- You cannot do mathematical operations such as addition over two points, but you can over vectors
- To define the vector you need two points

![Position Vector](images/PositionVector.png)

--

## Algebraic and geometric vectors

- We are going to work with vectors in two ways
  - Geometric vectors: a directed line segment
  - Algebraic vectors: a tuple of scalar numbers

---

## Vector: an algebraic definition

- Let *A* and *B* be two points with coordinates $ (a_x, a_y) $ and $ (b_x, b_y) $
- We denote the vector from *A* to *B* as $ \overrightarrow{AB} $
- Its values are $ (b_x-a_x, b_y-a_y) $
  - Note we are doing subtractions per coordinate (vector component)

--

## Length of the vector

- The length of the directed line segment *AB* is the distance between *A* and *B*
- We denote it as $ \left\| \overrightarrow{AB} \right\| $
- The value is $ \sqrt{(b_x-a_x)^2+(b_y-a_y)^2} $

---

## Visualising vectors

- A geometric vector is defined by a directed line segment

<iframe width="640" height="360" frameborder="0" src="https://www.shadertoy.com/embed/l32yzd?gui=true&t=10&paused=true&muted=false" allowfullscreen></iframe>

--

## Visualising vectors with Python

- vector = endpoint - startpoint 
- endpoint = startpoint + vector
  - for the line segment we call this vector **a direction vector**

```python
from PIL import Image, ImageDraw
def draw_segment(canvas, start, direction, colour) -> None:
    canvas.line(((start[0], start[1]), (start[0] + direction[0], start[1]+direction[1])), colour)

image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
draw_segment(canvas, (100, 50), (-100, 50), (255, 255, 0))
image.show()
```

--

## Position vs direction

[lines1.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture7/code/lines1.py)

```python
def draw_segment(canvas, start, direction, colour) -> None:
    canvas.line(((start[0], start[1]), (start[0] + direction[0], start[1]+direction[1])), colour)
```

- **start** is a position (location)
- *direction** is a vector (displacement)
- Both represented by the same data structure: **a tuple**

--

## Equal vectors

- If two vectors are equal, their components are equal as well
- Vectors with the same values are parallel line segments of the same length

```python
from PIL import Image, ImageDraw
def draw_segment(canvas, start, direction, colour) -> None:
    canvas.line(((start[0], start[1]), (start[0] + direction[0], start[1]+direction[1])), colour)

image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
draw_segment(canvas, (100, 50), (-100, 50), (255, 255, 0))
draw_segment(canvas, (150, 70), (-100, 50), (255, 255, 0))
draw_segment(canvas, (200, 70), (-100, 50), (255, 255, 0))
image.show()
```

---

## Vector operations

