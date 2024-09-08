## Lecture 1: Introduction to Procedural Content Creation

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 


---

# Session outline

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation
- **Title:** Introduction
- **Lecturers:** Jon Macey, Ian Stephenson, Oleg Fryazinov 

---

# Unit overview

- PCG runs in the first semester
- 12 weeks, 2 sessions each week
- Sessions can be more theoretical (lectures) or practical (workshops)
  - All the sessions in the computer labs, as we have practical elements during each session

--

##  Unit aims
 
- Develop the skill of computational thinking
- Apply it to the production of animation and visual effects.  

Note:
  The notes keyword is used to add speaker notes to a slide. 
  These notes are not visible to the audience.
  Note the new line and the Tabs
  
--

## What will you learn 

- How to create assets using code / scripting
- How to speak with computer using Python language
- Why blending arts and science can be fun
  
--  

## Assignment

- In the end of the semester 
- Scripting project with several options to choose
  - We will discuss it during one of the latter sessions
- 100% mark

---

# What is Procedural Content Creation?

- The unit name is three words: **procedural**, **content** and **creation**
- We are going to **create** assets that can be used for computer animation and visual effects pipeline (**content**) **procedurally**

--

## What is procedural

- What is the difference between **procedural** and **manual**?
  - We are going to write procedure and then computer will create the asset by following the procedure
  - We are going to write **the script** and the computer is going to **run** the script
  
--

## Context

- You are studying the subject of **computer** animation
  - We are all using computers
  - Your phone and even drawing tablet is a computer

--

## Applications

- **Computer Animation**
  - Rigging
  - Procedural animation (crowds, flocking, etc.)
- **Visual Effects**
  - Simulations: fluid, smoke, shattering, cloth...
  - Procedural Modelling
- **Art**
  - Generative art

-- 

# Why creating content procedurally?

- The ability to write new software gives extra power to go beyond the capabilities of the software
- Efficiency
  - You can create some assets quicker than manually
- Variety
  - Different assets can be created using the same procedure

--

## Programming sounds too technical

- "*I think only a mathematically minded people can ever write programs*" - **wrong**.  
- Process of creating art is similar to the process of creating programs
  - Starting software with sketches, tiny programs that just do one thing
  - Refine ideas through trial and error (and abstraction)
- Writing scripts is easier than you think
  - More about that later this session
  
--

# The creative process of computing
- As you go through the unit, you might encounter some points you might not really understand what is happening
- Do not be shy to ask questions as we are going along
- In these sessions we are going stress important parts that cannot be skipped
- Perfection comes with practice
- There is no "right way" or "wrong way" when it comes to programming
  - Similar to art!
  - The only "right direction" in programming is to ensure the program is doing what is supposed to do

--

# Learning to speak with computer

- Let we try to understand computers
- We are going to use **Linux** operating system. 
  - Have you heard about Linux?
- Most of the Digital Content Creation (DCC) tools were developed under Unix or Linux 
  - Unix is the family of computer operating systems. 
  - If you are using Mac, Macos is Unix
  - Linux is Unix as well
  
---

## Loading Linux

- **Why Linux?**
  - Lots of software work under Linux in the same way as for other operating systems
  - Stable
  - Secure
  - Controllable
  - User-friendly
  - Build for software development
- It is important to use / understand Linux for production as most big studios use Linux

--

## Loading Linux

* Restart your machine <!-- .element: class="fragment highlight-red" -->
* Press F12 when you see the banner <!-- .element: class="fragment highlight-red" -->
* In the menu select "Red Hat Boot Manager" <!-- .element: class="fragment highlight-red" -->

---

## Loading Linux

* Use your student username (s123456) and password to log in <!-- .element: class="fragment highlight-red" -->
* Locate Terminal in the menu on top <!-- .element: class="fragment highlight-red" -->

---

## Terminal

- The terminal is the most powerful tool you have on your computer. 
- It is the gateway to the operating system. 
- Terminal allows you to do things that are not possible with a GUI
- You speak with the OS using Terminal

---

## Terminal 

- The first thing we need to do is to get a terminal open
- When we open the terminal, it runs a program called a shell and awaits for your command
- Try these commands
<blockquote><small><p>~<br>pwd<br>echo "Hello World"</p></small></blockquote>
- What do they do?
  -```~``` command shows your *home folder*
  - **pwd** command shows where you are now

--

# The filesystem 

- Most of the work we do is based on a filesystem and navigating 
- The filesystem is a tree structure with a root at the top
- The root is the top level of the filesystem and is represented by a **/** character.
- Under the root are a number of directories 
  - They are called folders in Windows. 
  - They can contain files and other directories

--

## The filesystem: directories
- Each of you have a home directory, in your case it will be /home/```[```iSTUDENT_NUMBER```]```
-```~``` command shows your *home folder*
- What else is in your folder?

--

## The filesystem: files

- Each file has a name and an extension
- The file type is defined by its extension
- For example, .mb files are Maya binaries and can be opened by Maya
- We will come back to files and folder in a later session.

---

# Why Python
- Python is a language that allows read and run programs
- It reads programs line by line executing each instruction
  - We can have our programs run as we type
  - For beginners it makes starting with Python less frustrating!
- **Python in the industry**
  - Scripting in Maya, Houdini, Blender and many others
  
--

## Examples of Python in DCC

Note: 
  Include some images here from Technical Arts Production or similar

--

# Python scripts

- Often we use the term *script*. 
- What is the script in filmmaking?

<blockquote><small><p>A movie script is a written document that details all of the narrative and visual elements for a feature-length or short movie. This document includes very specific formatting, namely action paragraphs, character dialogue, and in some cases, visual and sound cues. </p></small></blockquote>

- Movie script explains what happens in the shot 
- Script in programming explains what happens in the program

--

# ["hello world" in Python](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)

- In the terminal type the command **python3** and press enter
- You will enter the Python environment
  - Python shell
- Start with writing this code:

```python
print("Hello World!")
```
- After you press "Enter" you should see *Hello World* in your shell
- You just wrote your first Python program!

--

## Explanation of the code
```python
print("Hello World")
```
- This code has only one command.
  - It tells the Python shell to **print** the string "Hello World"
  - Brackets are used to indicate the string is *the argument* for the command
  
- Now try to output your own string in the Python shell

--

# Creating graphics with Python

- Now try the following code 
  - Note we have graphics window appearing

```python
import turtle 
turtle.down()
```

--

## Creating graphics with Python (cont)

- Extend the code

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
```

---

## Creating graphics with Python: explanation

- **import** command imports the *library* turtle
  - Turtle Graphics
- **down** command puts the *pen* down
- **forward** command moves the pen a number of pixels forward
- **right** command turns the pen right given a certain degree
  
Note: 
  Insert image here 

---

## Creating graphics with Python (cont)

- The following code draws the square
- Can you draw other shapes like triangle?

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
```

--- 

# Conclusion

- **What have you learned today**
  - Your (probably) first two hours in Linux
  - Your first script in Python that draws a square
- **Homework**
  - Modify the code to draw a cross (or letter X)

--

# Next time

- **What will you learn next time**
  - Files and directories in Linux**
  - *Getting out of the Python shell* 
    - Working with .py scripts
  - Learning more about *libraries*

--

# Q&A and discussion
- **Open Floor for Questions**
