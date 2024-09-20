## Lesson 4: Variables and lists 

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Variables and lists
- **What will you learn today:**
  - More data types: we will talk about lists
  - What is a coding standard and why you need to use it
  - How to introduce variables into your code

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

## Why coding standards are necessary

1. **Easier to Read**: It is much easier to someone else to understand your code
2. **Reduces Mistakes**: Following standards can prevent common errors
3. **Teamwork**: Coding style keeps everything organised when working in teams
4. **Reusing code**: It is easier to reuse clearly written code
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
- List items are indexed
  - The first item has index [0]
  - The second item has index [1] etc.
```python
my_list = ["animation", "effects", "games", "animation"]
print(my_list[2])
```

--

## The size of the list

- len() is used to get the length of the list
```python
list1 = []
list2 = ["animation", "effects", "games", "animation"]
print(len(list1))
print(len(list2))
```

--

## List elements

- List items can be of any data type
- A list can contain different data types
```python
list1 = ["animation", "effects", "games", "animation"]
list2 = [2, 0, 2, 4]
list3 = ["abc", 123, "Hello!", 3.14159]
```

--

## Accessing elements from the list

- Use the index operator [ ] to access an item in a list. 
- The index must be an integer.
- The minimal index is 0, the maximum index is len()-1

--

## Nested lists

- Lists can be elements of lists
  - We refer to them as **nested lists**
- Nested lists are accessed using nested indexing. 

```python
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
my_list = [['Computer', 'Animation'], ['VFX']]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(my_list[0][1])
print(my_list[1][0])
```

--

## Negative indexing

- In Python, negative sequence indexes represent positions from the end of the List.
  - *-1* refers to the last item, *-2* to the second last item etc
  
```python
my_list = ["computer", "animation", "and", "visual", "effects"]
print(my_list[-2])
```

---

## Using variables and lists

```python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (20, 20, 255)
points = [(0, 0), (100,0), (100,100), (0, 100)]
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[1], points[2]), draw_colour)
draw.line( ( points[2], points[3]), draw_colour)
draw.line( ( points[3], points[0]), draw_colour)
im.show()
```

--

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

--

```python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (20, 20, 255)
origin_x = 320
origin_y = 240
points = [(origin_x, origin_y), (origin_x+100,origin_y), (origin_x,origin_y+100), (origin_x-100, origin_y), (origin_x, origin_y-100)]
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[0], points[2]), draw_colour)
draw.line( ( points[0], points[3]), draw_colour)
draw.line( ( points[0], points[4]), draw_colour)
im.show()
```

---

## Geometric data

- In the previous example 
  - We defined **a list of points**
  - We also defined line segments from these points
- That is the first step for understanding how all the objects in computer graphics (animation, VFX) are defined
- We will revisit it later!

--

## How to simplify the code?

- Instead of 
```python
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[0], points[2]), draw_colour)
draw.line( ( points[0], points[3]), draw_colour)
draw.line( ( points[0], points[4]), draw_colour)
```

- You can use 
```python
#repeat four times
draw.line( ( points[0], points[number_of_iteration_starting_at_1]), draw_colour)
#end of repeat
```

---

# Conclusion

- **What have you learned today**
  - How we can use variables
  - How we can use lists
  - Why do we need to care about how we write as well as what we write
- **Homework**
  - Extend the last example to draw the simple object like a clipart of the crystal. 
<img style="border: 0;" src="images/crystal.png" width="20%">

--

# Next time

- **What will you learn next time**
  - Loops
  - What 'if' means in the world of geeks

--

# Q&A and discussion
- **Open Floor for Questions**
