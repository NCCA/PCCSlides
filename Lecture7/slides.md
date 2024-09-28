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

![](images/Desc1.png)
![](images/Picture1.png)
![](images/Desc2.png)
![](images/Picture2.png)
![](images/Desc3.png)
![](images/Picture3.png)

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
- You cannot do mathematical operations such as addition over two points, but you can over vectors

![Position Vector](images/PositionVector.png)

--

## Algebraic and geometric vectors

- We are going to work with vectors in two ways
  - Geometric vectors: a directed line segment
  - Algebraic vectors: a tuple of scalar numbers
  
---

## Vector: an algebraic definition

- Let *A* and *B* be two points with coordinates `$$ (a_x, a_y) $$` and `$$ (b_x, b_y) $$`
- We denote the vector from *A* to *B* as `$$ \overrightarrow{AB} $$`
- Its values are `$$ (b_x-a_x, b_y-a_y) $$`

--

## Length of the vector

- The length of the directed line segment *AB* is the distance between *A* and *B*
- We denote it as `$$ \left\| \overrightarrow{AB} \right\| $$`
- The value is `$$ \sqrt{(b_x-a_x)^2+(b_y-a_y)^2} $$`

---