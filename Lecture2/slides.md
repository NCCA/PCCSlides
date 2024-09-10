## Lecture 2: Files, directories and libraries

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Files, directories and libraries
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
- The root is the top level of the filesystem and is represented by a **/** character.
- Under the root are a number of directories 
  - They are called folders in Windows. 
  - They can contain files and other directories

--

## Recap: files and directories

- Directories are separated by a **/** character
- Each of you have a home directory, in your case it will be /home/```[```iSTUDENT_NUMBER```]```
- Each file has a name and an extension

---

## Linux commands: cd

- ```~``` command shows your *home folder*
- **cd** is a command that changes directory
- Change directory to where Maya is installed:
<blockquote><small><p>cd /opt/autodesk/maya</p></small></blockquote>
- Change directory to your home folder:
<blockquote><small><p>cd ~</p></small></blockquote>

--

## Linux commands: cd

- To go to the parent directory, type
<blockquote><small><p>cd ..</p></small></blockquote>
- Linux terminal allows for autocomplete using Tab key. 
  - To go into Documents folder I can start typing 
<blockquote><small><p>cd Doc</p></small></blockquote>
  - Then press Tab to autocomplete to 
<blockquote><small><p>cd Documents/</p></small></blockquote>

---

## Create directories

- To create a new directory, we use **mkdir**
- Try this commands:
<blockquote><small><p>cd ~<br>cd /Documents<br>mkdir py_scripts</p></small></blockquote>
- What these commands do?

--

## Create files

- The **touch** command updates the access and modification times of each *file* to the current time. 
- If the file does not exist when passed on the command line an empty file will be created. 
<blockquote><small><p>cd py_scripts<br>touch test.py</p></small></blockquote>
- What these commands do?

--

## Remove files and directories

- To remove a directory and , we use **mkdir**
- Try this commands:
<blockquote><small><p>mkdir to_delete<br>rm to_delete</p></small></blockquote>
-  There is no recycle bin in Linux terminal, so **once it is gone it is gone**

---

## Essential Linux directories

Most linux environments have a similar directory structure.  The following is a list of the most important directories and their purpose.

| Directory | Purpose |
|-----------|---------|
| /bin      | Essential user command binaries (for use by all users) |
| /boot     | Static files of the boot loader |
| /dev      | Device files |
| /etc      | Host-specific system configuration |
| /home     | User home directories (optional) |
| /lib /lib64      | Essential shared libraries and kernel modules |
| /opt      | Add-on application software packages |
| /proc     | Virtual filesystem providing process and kernel information as files |
| /root     | Home directory for the root user (optional) |
| /sbin     | Essential system binaries |
| /srv      | Data directory for services provided by this system |
| /tmp      | Temporary files |
| /usr      | Secondary hierarchy |
| /var      | Variable data: files whose content is expected to continually change during normal operation of the system |

--

## NCCA Specific folders

- The ```/transfer``` folder is a mounted 1Tb local hard drive. 
  - This is shared with the windows partition and should be use for local work.
  - This is machine-specific!
- The ```/public``` folder is a network share when various things for teaching and learning are stored
  - ````/public/bin/2023```` is the folder where all the goScripts are stored. 
  - These scripts set up the environments for the various DCC tools to run.

---

## Editing Python scripts

- First, we will make a folder to put our scripts in
<blockquote><small><p>cd ~<br>mkdir scripts<br>cd scripts<br>touch my_first_script.py</p></small></blockquote>
- Now edit the file using *gedit*
<blockquote><small><p>gedit my_first_script.py</p></small></blockquote>
- This will run the text editor *gedit* and wait until you close the application

--

## Async start for programs

- For async start of the application add **&** in the end, for example
<blockquote><small><p>gedit &</p></small></blockquote>
- or
<blockquote><small><p>gedit my_first_script.py&</p></small></blockquote>

--

## Editing Python scripts

- In **gedit**, modify the contents of *my_first_script.py* to 

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
<blockquote><small><p>python3 my_first_script.py</p></small></blockquote>
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

- Various libraries do different things

```python
import keyword
print(keyword.kwlist)
```

--

## Python libraries
```python
import keyword
print(keyword.kwlist)
```

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del',
 'elif', 'else', 'except', 'finally', 'for', 'from',
 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
 'with', 'yield']
```

--

## Python libraries

- Python graphics libraries:
  - **Pillow**: image manipulation with Python
  - **Turtle**: turtle graphics
  - **Matplotlib**: data visualisation
  - **PyGame**: creating games with Python

--

## Python libraries

- There are two ways of working with libraries:
  - **import X**: imports the library X, and you can refer to things defined in module X, but using the module path <blockquote><small><p>X.name</p></small></blockquote> or <blockquote><small><p>python3 X.attribute</p></small></blockquote>
  - **from X import ***: import everything from the library X, but you should use plain (unqualified name) to refer to things 
  
---

## Python syntax

- Python syntax refers to the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in the Python language.
```python
print("Hello, World!")
```