## Lesson 3: Algorithmic thinking and data

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Algorithmic thinking and data
- **What will you learn today:**
  - What the algorithm is
  - The importance of data

---

## Recap: Python syntax

- Python syntax refers to the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in the Python language.
```python
print("Hello, World!")
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

--

## Recap: Python libraries

- We use **import** keyword for importing the library
- We let Python know we are using the code from the library
- Import turtle graphics: 
```python
import turtle 
```

---

## Algorithms

- Humans can understand vague instructions, computers can't. 
- An **algorithm** describes the method for solving a task.
- It consists of a sequence of steps that will solve the given task if executed correctly.

--

## Algorithms

- How to create an instant coffee? 
  - According to WikiHow
  
<blockquote><small><p><ul><li>Heat up a mug of water</li><li>Add 1–2 teaspoons (2–4 g) of instant coffee to the mug</li><li>Stir your coffee into the mug of hot water</li><li>Mix in sugar, spices, milk, or cream if you want them</li></ul></p></small></blockquote>

Note:
  Note the new line and the Tabs

--

## Algorithms

- With a computer we need to plan and account for everything
<blockquote><small><p><ul><li>Pour drinking water into electric kettle, assuming you have a kettle</li><li>Plug electric kettle and wait for it to boil</li><li>While waiting, prepare the mug, assuming you have a mug</li><li>Repeat twice: using a teaspoon move the amount of instant coffee that a teaspoon can hold from the coffee jar to the mug</li><li>Check boiling water</li><li>If water is not boiled, continue and wait and refer to the previous step</li><li>If water is boiled, unplug kettle and pour water into cup</li><li>For each item in the following list [sugar, spices, milk, cream] repeat: if you want the item in your coffee, add it to the mug</li><li>Stir coffee mix</li></ul></p></small></blockquote>

--

## Algorithms

- The art of programming is the design of the algorithms that form the basis of our programs
- Algorithm design requires understanding of the problems that we want to solve

--

## Algorithms

- We look at the overall goal and figure out what steps need to be taken (and in what execution sequence)
- Each step is then examined individually and broken up further into smaller steps
- When developing programs, we deal with algorithms and data

---

## Program flow

- Look again at the example of drawing the square
- What is the sequence of operations here?
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


---

## Data types

- Python has 5 standard data types
  1. Numbers
  2. String
  3. List
  4. Tuple
  5. Dictionary

---

## Numbers

- Python supports 3 different numerical types:
  - **int** (signed integers)
  - **float** (floating point real values)
  - **complex** (complex numbers)

--

## Integers (recap)

- In Mathematics, **integers** are the collection of whole numbers and negative numbers. 

- integers are numbers that can be positive, negative or zero, but cannot be a fraction
- You can perform arithmetic operations on integers: 
  - Addition
  - Subtraction
  - Multiplication
  - Division

--

## Real numbers

- Real numbers is a combination of rational and irrational numbers
  - Rational numbers can be represented by a fraction (example: 1/2)
  - Irrational numbers cannot be represented by a fraction (example: sqrt(2))
- You can perform arithmetic operations on real numbers 

--

## Complex numbers

- Complex numbers are numbers that are represented in teh form of x+iy
  - 'i' is an imaginary number, the value of i is equal to the root of minus one
  - For example, 3+5i is a complex number, where 3 is the real number and 5i is imaginary.
- We will discuss complex numbers later!

--

## Numbers 
```python
integer_variable = 1  # note the names are not reserved words
float_variable = 1.2
complex_variable = 4 + 5j

print(f"{integer_variable} is of type {type(integer_variable)}")
print(f"{float_variable} is of type {type(float_variable)}")
print(f"{complex_variable} is of type {type(complex_variable)}")
```

--

## Arithmetic operations

```python
value = 10 + 3.14  # adding integer to float results in float
print(value)
value = value - -5
print(value);
value = value * 100
print(value)
value = value / 1000
print(value)
```

--

## Arithmetic operations in Python

- The simple operations are shown below

| operation | Result |
|--------|-------|
| ``` x+y``` | sum of x and y |
| ``` x-y``` | difference of x and y |
| ``` x*y``` | product of x and y |
| ``` x/y``` | quotient of x and y |
| ``` x//y``` | floored quotient of x and y |
| ``` -x``` | x negated |
| ``` x**y``` | x to the power y |

---

## Strings

- A String is a data structure that represents a sequence of characters.
- Strings in Python are surrounded by either single quotation marks, or double quotation marks.

```python
print("Hello")
print('Hello')
string_variable = 'Hello, world!'
print(string_variable)
print(type(string_variable)) 
```

--

## Strings 

- A single character is a string with a length of 1
- You can use quotes inside a string, as long as they don't match the quotes surrounding the string
```python
print("It's alright")
print("The unit is called 'Procedural Content Creation'")
print('The unit is called "Procedural Content Creation"') 
```

--

## Strings

- You can assign a multiline string to a variable by using three quotes
  - Both single quotes and double quotes work

```python
# Creating String with triple
# Quotes allows multiple lines
String1 = """Computer 
Animation
And
Visual
Effects"""
print("\nCreating a multiline String: ")
print(String1)
```

## Strings

- Strings in Python are arrays
- We are going to discuss arrays later in this course
- Now we come back to turtle graphics

---

## Drawing a square

- As we discussed, this program draws the square
- Can we draw something more complex?

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

## Turtle graphics

| Command | What it does |
|--------|-------|
| ``` forward(distance)``` | Move the turtle forward by the specified distance |
| ``` backward(distance)``` | Move the turtle backward by distance |
| ``` left(angle)``` | Turn turtle left by angle units (in degrees by default) |
| ``` right(angle)``` | Turn turtle right by angle units |
| ``` goto(x,y)``` | Move turtle to an absolute position (x,y). If the pen is down, draw line. |
| ``` teleport(x,y)``` | Move turtle to an absolute position, a line will not be drawn |
| ``` color()``` | set colour for pen and fill |

---

## Coordinate systems

- **Coordinate system** is a system that uses **coordinates** to **establish position** of the point in space
- Coordinates are represented by numbers
- Coordinate systems can have different dimensionalities
  - 1D, 2D, 3D, ...

Note: 
  We should expect them to know about coordinate systems from school, here is more like a recap
    
--

## Coordinates on a real number line

- The origin corresponds to 0
  - To the left of the origin are the negative real numbers
  - To the right of the origin are the positive real numbers 
- Distance between 0 and 1 determines the scale
- The real number associated with a point *P* is called the coordinate of *P*

--

## 2D Cartesian coordinates

- **Two orthogonal** real number lines
  - The horizontal line is the **x-axis**
  - The vertical line is the **y-axis**
  - The origin is the point of intersection
- Any point can be located by using an ordered pair (x, y) as coordinates of the perpendicular projections of the point onto two axes.

---

## Algorithms 

- Different algorithms can save the same problem
- Different programs can do things that are seemingly the same
  - Their efficiency might be different
  - The code might have different readability
  
--

## Another way to draw the square

```python
import turtle 
turtle.down()
turtle.goto(100,0)
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(0,0)
turtle.done()
```

--

## One more way to draw the square

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

---

# Conclusion

- **What have you learned today**
  - How to use algorithms to think like a computer
  - Data types: numbers and strings
  - There are different ways to solve the same problem
- **Homework**
  - Draw the first letter of your name using either turtle or PIL

--

# Next time

- **What will you learn next time**
  - Loops
  - What is Boolean logic

--

# Q&A and discussion
- **Open Floor for Questions**
