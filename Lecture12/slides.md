## Lesson 12 : Files and Meshes

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Files and Meshes
- **What will you learn today:**
  - Opening and closing files
  - Reading and writing text files
  - context managers and exceptions
  - How meshes are stored and written 
  - The obj file format


---

## What is file I/O?

- I/O stands for Input/Output 
- It is the process of reading data from and writing data to files on a computer. 
- In Python, file I/O is done using file objects 

--

## File Objects

- File objects represent files on the computer's file system.
- We open a file using the [```open```](https://docs.python.org/3/library/functions.html#open) function, typically for either reading or writing.
- open takes two arguments, the name of the file and the mode in which to open the file.


--

## File Modes

| Character | Meaning |
|-----|--------|
| 'r' | open for reading (default) |
| 'w' | open for writing, truncating the file first |
| 'x' | open for exclusive creation, failing if the file already exists |
| 'a' | open for writing, appending to the end of file if it exists |


--

## File Modes

| Character | Meaning |
|-----|--------|
| 'b' | binary mode |
| 't' | text mode (default) |
| '+' | open for updating (reading and writing) |

--

## File Names

- The file name is a string representing the path to the file.
  - There are many complexities with files and paths that we are going to overlook at present.
- As we are using linux files will use the forward slash ```/``` as a path separator.
- If we don't specifiy a path, the file will be created in the current (working) directory.

---

## Opening and Closing Files

- To create a simple text file we can use the following code in the REPL:

```python
f = open("test.txt", "w")
f.write("Hello, World!")
f.close()
```

- everything written to the file will be ASCII text

--

## explanation

- This will create a file called ```test.txt``` in the current directory 
- Write the string ```Hello, World!``` to it. 
- The ```close``` method is used to close the file after we have finished writing to it. 
- If we do not close the file, the changes we have made to it may not be saved.

---

## Reading in a file

- To read a file we can use the ```read``` method on an open file object.

```python
f = open("test.txt", "r")
contents = f.read()
print(contents)
f.close()
```

--

## explanation

- first we open the file in read mode
- then we read the contents of the file into a string 
  - typically we would then process the string in some way
- finally we close the file

---

## [context managers](https://docs.python.org/3/reference/datamodel.html#context-managers)

- You will notice in both examples we have to remember to close the file. 
- This can be a source of bugs in programs if we forget to close the file. 
- To help with this Python has a feature called a context manager. 

--

## Context Managers
  
- Context managers are objects that manage resources, such as files, and automatically clean up after themselves when they are no longer needed. 
- We can use the ```with``` statement to create a context manager for a file. For example:

```python
with open("test.txt", "r") as file:
    contents = file.read()
    print(contents)
```

- This will automatically close the file when the block of code inside the ```with``` statement is finished.

---


## [exceptions](https://docs.python.org/3/tutorial/errors.html)

- python uses exceptions to tell us something has gone wrong there are a number of build in exceptions for example 

```python
10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

- will raise a ```ZeroDivisionError```

--

## [zen of python](https://peps.python.org/pep-0020/)

> Errors should never pass silently.

> Unless explicitly silenced.

- this is a key part of python, it is better to fail fast and know what has gone wrong than to have a silent error that is hard to debug
- this is why we have exceptions

--


## [try / except blocks](https://docs.python.org/3/reference/compound_stmts.html#try)

- when we want to execute some code that may throw an exception we place it in a ```try : ``` block 
- we then use the ```except [type]: ``` block

```python
#!/usr/bin/env python

a=10
b=0
try :
    print('Doing Division {}'.format(a/b))
except ZeroDivisionError:
    print('Cant divide by zero')

print('now do something else')
``` 


--

## built in exceptions

- python  has many build in exceptions a list can be found [here](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
- We can also generate our own exceptions using the ```raise``` keyword
- this is useful when we design our own API's and want to provide useful error messages

---

## File exceptions

- It may not always be possible to open a file, for example if the file does not exist or the user does not have permission to read or write to it. 
- In these cases, Python will raise a ```FileNotFoundError``` or ```PermissionError``` exception. 
- To handle these exceptions, we can use a ```try``` statement to catch the exception and handle it gracefully. 

--

## example

```python
#!/usr/bin/env python

try :
    with open("nothere", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found")
    
# throw a permission denied exception
try:
    with open("/etc/passwd", "w") as file:
        ...
except PermissionError:
    print("Permission denied")

```

---

## OS module

- The module **os** provides functions for interacting with the operating system and allows for
  - Handling the current working directory
  - Creating a directory
  - Listing out files and directories with Python

--

## Getting the Current working directory

- To get the location of the current working directory use *os.getcwd()* 
```python
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 
```

--

## Listing out Files and Directories 

- Another useful function is OS is *os.listdir()*
  - It lists all files and directories in the specified directory 
  - If no directory specified, it lists all files and folders in the current working directory

```python
import os 
path = "/"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list)
```

--

## Is that all for files?

- for now this is all we need.
- Later we will look at more advanced file handling, such as reading and writing binary files, and working with directories.
- Also structured file formats such as JSON or XML, which are used in many DCC tools.


---

## Meshes

- In computer graphics, a mesh is a collection of vertices, edges, and faces that define the shape of a 3D object.
- Meshes are typically stored in files using a simple text format that describes the vertices, edges, and faces of the mesh.
- They typically consist of a collection of lists, with the faces referring to the vertices by index. 
- One of the most common file formats for storing meshes is the Wavefront OBJ format.

--

## [The OBJ file format](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

- The OBJ file format is a simple text format that describes the vertices, normals, UK's and faces of a mesh.
- It can actually many different types of data, but we will only look at the basic format in this lecture.
- We will start by considering a simple  triangle mesh (in 3D)

--

## A Simple Triangle

- A triangle mesh contains a single face with three vertices.
- Each vertex has a position in 3D space, given by three floating-point numbers (x, y, z).

```python
triangle=[
    [2.0, 0.0, 0.0],
    [0.0, 4.0, 0.0],
    [-2.0, 0.0, 0.0]
]
```

--

## Obj components

- The OBJ file format consists of a series of lines, each of which describes a different component of the mesh.
- The most important components are:
  - ```v``` - a vertex position
  - ```vn``` - a vertex normal
  - ```vt``` - a vertex texture coordinate
  - ```f``` - a face

## A Simple Triangle

- The OBJ file format for a simple triangle mesh would look like this:

```
v 2.0 0.0 0.0
v 0.0 4.0 0.0
v -2.0 0.0 0.0
f 1 2 3
```

- We can save this into a text file and open it in maya. 

--- 

## Python Objewriter 

- We can write a simple python program to write out an obj file

```python


```
