## Lesson 5: Basic programming constructs

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Basic programming constructs
- **What will you learn today:**
  - What is a loop
  - What is a conditional statement
  - Importance of indentation
  
---

## Recap: variables

- Variables are used to store data
- No need to declare data types explicitly
- Numbers, strings, lists, tuples

--

## Recap: lists and variables

```python
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[0], points[2]), draw_colour)
draw.line( ( points[0], points[3]), draw_colour)
draw.line( ( points[0], points[4]), draw_colour)
```

--

```python
import turtle 
turtle.down()
# repeat the following two lines four times
turtle.forward(100)
turtle.right(90)
# end of the code that we need to repeat four times
turtle.done()
```

---

## The three basic programming constructs

- Programs are designed using common building blocks
  - Also known as programming constructs
- There are three basic building blocks
  - Sequence
  - Selection
  - Iteration
  
---

## Sequence

- Sequence is the order in which instructions occur and are processed

```python
# Algorithm to find and print the mid-point of the line segment
# Step 0: Input the data
print('Enter x1:')
x1 = input()
print('Enter y1:')
y1 = input()
print('Enter x2:')
x2 = input()
print('Enter y2:')
y2 = input()
# Step 1: Calculate the x-coordinate of the midpoint
x_m = (x1 + x2) / 2  
# Step 2: Calculate the y-coordinate of the midpoint
y_m = (y1 + y2) / 2
# Step 3: Print the result
print(x_m)
print(y_m)
```

--

## Sequence

- Writing instruction in the wrong order is one of the most common programming errors
- What is wrong with the algorithm below (apart from lack of comments)?
```python
x_m = (x1 + x2) / 2  
draw.line( ( (x_m, y_m), (x2, y2)), draw_colour)
y_m = (y1 + y2) / 2

x1 = input()
y1 = input()
print('Enter x1:')
print('Enter y1:')
x2 = input()
y2 = input()
print('Enter x2:')
print('Enter y2:')
```

---

## Selection

- Selection determines which path a program takes when it is running
- How the computer decides what it should do next?
  - We use a **conditional** value to represent our decision
  - Also called a **Boolean** value

--

## Conditional operator

- **Definition**: A conditional operator allows the program to make decisions based on certain conditions.
- **Concept**: If a condition is true, the program performs one action; if it's false, it can perform another.
- **Real-life analogy**: "If it's raining, take an umbrella. Otherwise, go out without it."

--

## Syntax of the **if** Statement

```python
if condition:
    # Code to execute if the condition is True
```
- Components:
  - **if**: Keyword to start the condition.
  - **Condition**: An expression that evaluates to *True* or *False*.
  - **Colon (:)**: Indicates the start of an indented block of code.
  - **Indentation**: The block of code to be executed if the condition is true.

---

## Indentation and Code Blocks

- **Indentation**: Python uses indentation to define blocks of code.
  - Convention states we use **4** spaces for indentation
  - This might be inconvenient
  - This can lead to problem, especially when mixing tabs and spaces
  - Usually t his will follow a statement and the : operator
  
--

## Why indentation is important

- Consistent indentation is crucial for Python code to work correctly.

```python
if x > 5:
    print("x is greater than 5")
```

- Improper indentation causes syntax errors.
```python
if x > 5:
print("x is greater than 5")  # This will cause an error
```

---

## If statement: example
```python
x = 0.5

if x > 0:
    print("x is positive")
```

- Explanation: 
  - The condition checks if x is greater than 0.
  - If the condition is true (in this case, 0.5 > 0), the message "x is positive" is printed.
  - If the condition is false, the program moves on without executing the block.
  
--

## The else Statement

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

- **else** provides an alternative block of code to run when the condition is false.

--

## Using if-else: example

```python
x = 0.5
if x > 0:
    print("x is positive")
else:
    print("x is zero or negative")
```

---

## Comparison operators 

- Comparison operators are used to compare two values

| operator | meaning |
|--------|-------|
| ``` == ``` | equal to |
| ``` != ``` | not equal to |
| ``` > ``` | greater than |
| ``` < ``` | less than |
| ``` >= ``` | greater or equal to |
| ``` <= ``` | less or equal to |

--

## Comparison operators: example

```python
x = 10
y = 5

print(x > y)  # True
print(x == y)  # False
```

---

## Logical operators

- Logical operators combine multiple conditions into a single Boolean expression:
  - **and**: Returns *True* if both conditions are true
  - **or**: Returns *True* if at least one condition is true
  - **not**: Inverts the result (*True* becomes *False*, and vice versa)

--

## Logical operators: example

```python
x = 5
y = 10

print(x > 0 and y > 0)  # True (both conditions are True)
print(x > 0 or y < 0)   # True (one condition is True)
print(not (x > 0))      # False (inverts the True result)
```

--

## Logical operators: example

```python
x = 0.5
y = -0.5

if x >= 0 and y >= 0:
    print("Both values are non-negative")
```

---

## Iteration 
- Iteration is the process of repeating a block of code multiple times
- There are two types of iteration:
  - **for loop**: Iterates over a sequence of items
  - **while loop**: Repeats as long as a condition is true. 
  
---

## The **for** loop

- The for loop iterates over a sequence (such as a list, tuple, string, or range)

```python
keywords = ["computer", "animation", "visual", "effects"]

for keyword in keywords:
    print(keyword)
```

--

## for loop with range()

- range() generates a sequence of numbers, commonly used with for loops
  - start: starting number (default is 0)
  - stop: stopping point (not included)
  - step: step size (default is 1)
```python
for i in range(start, stop, step):
    # Code to execute for each number in the range
```

--

## for loop with range(): example

```python
import turtle 
turtle.down()
for i in range(4)
    turtle.forward(100)
    turtle.right(90)
turtle.done()
```

- Note the indentation!

---


## The **while** loop

- The **while** loop repeats a block of code as long as a condition remains True

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

--

## **break** statement

- The **break** statement is used to exit a loop before it completes all its iterations.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

--

## **continue** statement

- The continue statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

---

## Bringing it all together

```python
import turtle
running = True
while running:
    print('enter triangle, square, or exit:') entered = input()
    if entered == 'triangle':
	    for i in range(3):
            turtle.forward(100)
            turtle.right(120)
			continue
    if entered == 'square': 
	    for i in range(4):
            turtle.forward(100)
            turtle.right(90)
			continue
    if entered == 'exit': 
	    running = False
        print('exiting...') 
    else:
        print('not a command')
```

---

# Conclusion

- **What have you learned today**
  - Conditional operator **if**
  - The importance of indentation
  - The **for** loop and the **while** loop
- **Homework**
  - Extend the last program to draw one extra object, such as a hexagon (six sides, 60 degrees turn). 
  
--

# Next time

- **What will you learn next time**
  - Functions
  - How to embrace chaos with randomness

--

# Q&A and discussion
- **Open Floor for Questions**
