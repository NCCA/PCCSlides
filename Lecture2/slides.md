## Lecture 2 : 
### Files, directories and libraries

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

## Session outline

- **What will you learn today:**
  - How to navigate, create and edit files and directories in Linux 
  - How to work with Python files
  - What is *a library* in the context of computing

---

## Recap: Loading Linux

- Restart your machine 
- Press F12 when you see the banner 
- In the menu select "Red Hat Boot Manager" 
- Use your student username (s123456) and password to log in

--

## Recap: Terminal

- The terminal is the gateway to the operating system. 
- You speak with the OS using Terminal
- When we open the terminal, it runs a program called a shell and awaits for your command

--

## Recap: the filesystem

- The filesystem is a tree structure with a root at the top
- The root is the top level of the filesystem and is represented by a ```/``` character.
- Under the root are a number of directories 
  - They are called folders in Windows. 
  - They can contain files and other directories

--

## Recap: files and directories

- Directories are separated by a ```/``` character (windows uses ```\```)
- Each of you have a home directory, in your case it will be /home/```[```iSTUDENT_NUMBER```]```
- Each file has a name and an additionally may have an extension separated by the . used to identify the file type.

---

## ```pwd```

- "print working directory"
- This command will show you where you are in the filesystem, think of it as your way of asking where am i?

<asciinema-player src="terminal/pwd.asc" cols=120 rows=10></asciinema-player>

--


## Linux commands: cd

- ```~``` is a linux shortcut for your *home folder*
- ```cd``` is a command that changes directory
- Change directory to where Maya is installed: (/opt/autodesk/maya) 

<asciinema-player src="terminal/cd.asc" cols=120 rows=10></asciinema-player>



--

## Linux commands: cd

- To go to the parent directory (up a level), type ```cd ..```
- Linux terminal allows for autocomplete using Tab key. 

<asciinema-player src="terminal/cd2.asc" cols=120 rows=10></asciinema-player>



---

## Create directories

- To create a new directory, we use ```mkdir```
- first we will make sure we are home by using ```cd``` with no arguments

<asciinema-player src="terminal/mkdir.asc" cols=120 rows=10></asciinema-player>


--

## Create files

- The **touch** command updates the access and modification times of each *file* to the current time. 
- If the file does not exist when passed on the command line an empty file will be created. 

<asciinema-player src="terminal/touch.asc" cols=120 rows=10></asciinema-player>



--

## Remove files and directories

- To remove a directory and , we use **mkdir**
- Try this commands:

```
mkdir to_delete
rmdir to_delete
``` 

-  There is no recycle bin in Linux terminal, so **once it is gone it is gone**

---

## Essential Linux directories

- Most linux environments have a similar directory structure.  
- The following is a list of the most important directories and their purpose.

| <small>Directory</small> | <small>Purpose</small> |
|-----------|---------|
| <small>/bin</small>      | <small>Essential user command binaries (for use by all users) </small>|
| <small>/boot</small>     | <small>Static files of the boot loader</small> |
| <small>/dev</small>      | <small>Device files</small> |
| <small>/etc </small>     | <small>Host-specific system configuration</small> |


--

| <small>Directory</small> | <small>Purpose</small> |
|-----------|---------|
| <small>/home </small>    | <small>User home directories (optional)</small> |
| <small>/lib /lib64 </small>     | <small>Essential shared libraries and kernel modules</small>|
| <small>/opt</small>      | <small>Add-on application software packages </small>|
| <small>/proc</small>     | <small>Virtual filesystem providing process and kernel information as files</small> |
| <small>/root </small>    | <small>Home directory for the root user (optional)</small> |

--

| <small>Directory</small> | <small>Purpose</small> |
|-----------|---------|
| <small>/sbin </small>    | <small>Essential system binaries</small> |
| <small>/tmp </small>     | <small>Temporary files</small> |
| <small>/usr </small>     | <small>Secondary hierarchy </small>|
| <small>/var </small>     | <small>Variable data: files whose content is expected to continually change during normal operation of the system </small>|

--

### NCCA Specific folders

- The ```/transfer``` folder is a mounted 1Tb local hard drive. 
  - This is shared with the windows partition and should be use for local work.
  - This is machine-specific and considered volatile
  - so work can be deleted at any time!

--

### NCCA Specific folders

- The ```/public``` folder is a network share when various things for teaching and learning are stored
  - ````/public/bin/2024```` is the folder where all the goScripts are stored. 
- ```/public/devel/24-25``` loads of extra programming tools and libraries are stored here.
- you have read only access to this.


---

## Editing Python scripts

- First, we will make a folder to put our scripts in
- I prefer to use my Desktop for this, but you can use any location

```bash
cd ~/Desktop
mkdir PCC
cd PCC
mkdir Week2
cd Week2
pwd
```

--

## Editing Python scripts

- Now we are in the Week2 directory, let's create a Python script

```bash
touch my_first_script.py
code my_first_script.py
```

- This will open the script in [Visual Studio Code](https://code.visualstudio.com/)

--


## Editing Python scripts

- In the editor modify the contents of *my_first_script.py* to 

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

--

## Running Python scripts

- Back to terminal, type

```bash
python my_first_script.py
```

- Wait, is it just drawing and then immediately disappearing?

--

## Modify the script to

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
- Can you see it now?

---

## Python syntax

- Python syntax refers to the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in the Python language.
- 
```python
print("Hello, World!")
```

--

## Python syntax

- in the REPL (Read-Eval-Print-Loop) we can type the following

```python
print("Hello, World!")
```
- In the above program we use **print** *function* to print the message
- The arguments for the function are whatever is inside the paretheses ()

--

## Python syntax

- Comments are the text that we can add to our program to make our code easier to understand
- The computer ignores comments 


```python
# This program prints the string 'Hello World'
print("Hello, World!")

""" 
We can also have longer multi
line comments using the triple quotes
"""
```

--

## Python variables

- Variables are names for storing data values
- A variable is created the moment you first assign a value to it

```python
x = 150
y = "Hello"
print(x)
print(y) 
```

--

## Python variables

- Python will try to figure out what type (more later) the variable is (unlike other languages)
- We will be talking about variables later!

```python
value = input("Enter the value")
print(value)
```

---

## Python libraries

- With a computer we can do everything
- But we do not want to create entire worlds from scratch
- We can leverage the work of other people through **Python libraries**

--

## Python libraries

- We use **import** keyword for importing the library
- We let Python know we are using the code from the library
- Import turtle graphics: 
```python
import turtle 
```

--

## Python libraries

- Various libraries do different things for example random number generation

```python
import random
print(random.randint(1, 100))
```

- This will print a random number between 1 and 100

--

## What does the . mean

- in the previous example we imported random
- this is a python module that contains functions for generating random numbers
- the . is used to access the functions in the module
- we are basically saying "use the randint function from the random module"

--

## Python libraries

- There are two ways to import a library

```python
import random
```

```python
from random import *
```

- we tend to use the first method as it is more explicit and can avoid complications later. 
- It would also bring in all of random and we don't need that
- this is why we need module name . function name

--

## Python libraries

- Python graphics libraries:
  - **Pillow**: image manipulation with Python
  - **Turtle**: turtle graphics
  - **Matplotlib**: data visualisation
  - **PyGame**: creating games with Python
  - **PyOpenGL**: OpenGL bindings for Python

---

## Creating an empty image

- Now put everything we discussed about the syntax together
- What is happening here?

```python
from PIL import Image  

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193) )
img.show()
```

--

## Time to play

- create an empty file called ```first_image.py```
- copy the previous code into the file
- now change things and see what happens, if it breaks ask for help (or try to fix it yourself)

---

# Conclusion

- **What have you learned today**
  - How to work with files and directories in Linux
  - How to run scripts from .py files
  - How to create an empty image
- **Homework**
  - Modify the code to create an empty image of a yellow colour

--

# Next time

- **What will you learn next time**
  - Introduction to *algorithmic thinking* and how to go with the program flow
  - Data and variables

--

# Q&A and discussion
- **Open Floor for Questions**
