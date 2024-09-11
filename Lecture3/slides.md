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
- How can we design it more efficiently?
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

## Program flow

- We don't know some concepts yet, but the program has the following logic: 
```python
import turtle 
turtle.down()
# repeat the following two lines four times
turtle.forward(100)
turtle.right(90)
# end of the code that we need to repeat four times
turtle.done()
```

- Let we discuss some important parts of the Python language first

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
  
## Real numbers

- Real numbers is a combination of rational and irrational numbers
  - Rational numbers can be represented by a fraction (example: 1/2)
  - Irrational numbers cannot be represented by a fraction (example: sqrt(2))
  
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

  
---

