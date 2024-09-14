## Lesson 4: Program flow 

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Program flow
- **What will you learn today:**
  - More data types
  - 

---

## Recap: Drawing the square using turtle

```python
import turtle 
turtle.down()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.done()
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

## Variables

- Variable is a **named storage location**
- It is a common practice to give a meaningful name
- Are names meaningful in this example?

```python
a = "Computer Animation & Visual Effects"
b = "2024"
print(a)
print(b) 
```

--

## Variables

- How about now?

```python
course = "Computer Animation & Visual Effects"
year = "2024"
print(course)
print(year) 
```

---

## Coding Style and Practice

- Coding standards are a set of guidelines and best practices that developers follow while writing code.
- They help ensure that all the code looks and works in a similar way, no matter who wrote it. 
- We will be periodically revisit coding standards in these lessons

--

## Coding Style and Practice

- Why coding standards are necessary
  1. **Easier to Read**: It is much easier to someone else to understand your code
  2. **Reduces Mistakes**: Following standards can prevent common errors
  3. **Teamwork**: If you are working on the same project in teams, coding style keeps everything organised
  4. **Reusing code**: It is easier to reuse code if it is written in a clear way
  5. **Saves time**: When code is easy to understand, it saves time during debugging and updating
  
---

##  Using variables

- Rewrite this code to improve its readability
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

## Using variables

- Can we further simplify this code?<!-- .element: class="fragment" -->
```python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (0, 255, 255)
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( (0, 0), (100,0)), draw_colour)
draw.line( ( (100, 0), (100,100)), draw_colour)
draw.line( ( (100, 100), (0,100)), draw_colour)
draw.line( ( (0, 100), (0,0)), draw_colour)
im.show()
```

---

## Data types

- Python has 5 standard data types
  1. Numbers <!-- .element: class="fragment highlight-red" -->
  2. String <!-- .element: class="fragment highlight-red" -->
  3. List
  4. Tuple
  5. Dictionary
  
---

## Lists

- Lists are used to store multiple items in a single variable
- Lists are created using square brackets
```python
my_list = ["animation", "effects", "games"]
print(my_list)
```

--

## Lists

- List items are ordered, changeable, and allow duplicate values
- List items are indexed, the first item has index [0], the second item has index [1] etc.
```python
my_list = ["animation", "effects", "games", "animation"]
print(my_list[2])
print(len(my_list))
```

--

## Lists

- List items can be of any data type
- A list can contain different data types
```python
list1 = ["animation", "effects", "games", "animation"]
list2 = [2, 0, 2, 4]
list3 = ["abc", 123, "Hello!", 3.14159]
```

---

## Using lists

```python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (0, 255, 255)
points = [(0, 0), (100,0), (100,100), (0, 100)]
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[1], points[2]), draw_colour)
draw.line( ( points[2], points[3]), draw_colour)
draw.line( ( points[3], points[0]), draw_colour)
im.show()
```
