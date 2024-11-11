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

## Python ObjWriter 

- We can write a simple python program to write out an obj file

```python
#!/usr/bin/env python3


triangle = [[2.0, 0.0, 0.0], [0.0, 4.0, 0.0], [-2.0, 0.0, 0.0]]

faces = [[0, 1, 2]]


with open("triangle1.obj", "w") as file:
    for vertex in triangle:
        file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
    # write the faces Note these are 1-based indices
    for face in faces:
        file.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")

```

--

## Python ObjWriter

- This will write out a simple triangle mesh to a file called ```triangle1.obj```
- We can then open this file in a 3D application such as Maya to view the mesh.
- You will notice there are no normals or texture coordinates in this file 
- we will add normals next

---

## Adding Normals

- Normals are vectors that are perpendicular to the surface of the mesh at each vertex.
- They are used to calculate the shading of the mesh.
- We can add normals to our OBJ file by adding lines like this:

```
vn 0.0 0.0 1.0
```

- This line defines a normal vector pointing straight  in the z-direction.


--

## Calculating Normals

- To calculate the normals for a triangle mesh, we can use the cross product of the edges of the triangle.
- The cross product of two vectors gives a vector that is perpendicular to both of them.
- We can calculate the normal for a triangle by taking the cross product of two of its edges.
- For example, the normal of a triangle with vertices A, B, and C is given by the cross product of the vectors AB and AC.

==

## Calculating Normals

- The cross product of two vectors A and B is given by the formula:

```
A x B = (AyBz - AzBy, AzBx - AxBz, AxBy - AyBx)
```

- We can use this formula to calculate the normal of a triangle mesh.

--

## Python ObjWriter

- We can add normals to our OBJ file by calculating the normals for each face and writing them to the file.

```python
#!/usr/bin/env python3

def calc_normal(v1, v2) :
    
    n=[v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]]
    # normalize the normal
    length = math.sqrt((n[0]**2 + n[1]**2 + n[2]**2))
    if length == 0:
        return n
    n[0] /= length
    n[1] /= length
    n[2] /= length
    return n

```

--

## Python ObjWriter

- We can then calculate the normals for each face and write them to the file.

```python
triangle = [[2.0, 0.0, 0.0], [0.0, 4.0, 0.0], [-2.0, 0.0, 0.0]]

faces = [[0, 1, 2]]

normals=[]
normals.append(calc_normal(triangle[0], triangle[1]))
normals.append(calc_normal(triangle[1], triangle[2]))
normals.append(calc_normal(triangle[2], triangle[0]))

with open("triangle2.obj", "w") as file:
    for vertex in triangle:
        file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
    for normal in normals:
        file.write(f"vn {normal[0]} {normal[1]} {normal[2]}\n")
    # write the faces Note these are 1-based indices
    for face in faces:
        file.write(f"f {face[0]+1}//{face[0]+1} {face[1]+1}//{face[1]+1} {face[2]+1}//{face[2]+1}\n")
        
```

--

## Python ObjWriter

- This will write out a simple triangle mesh with normals to a file called ```triangle2.obj```
- We can then open this file in a 3D application such as Maya to view the mesh.
- You will notice there are no texture coordinates in this file so the face format is ```v//n```
- we will add texture coordinates next

---

## Adding Texture Coordinates

- Texture coordinates are used to map a 2D image onto a 3D mesh.
- They are typically given as two floating-point numbers (u, v) that specify the position of the texture on the mesh.
- We can add texture coordinates to our OBJ file by adding lines like this:

```
vt 0.0 0.0
vt 1.0 0.0
vt 0.0 1.0
```

--

## Python ObjWriter

- the uv index is inbetween the vertex and normal index

```python
f v/vt/n v/vt/n v/vt/n
```

- again it is an index into the list of texture coordinates

---

## A Cube

- A cube mesh contains six faces, each with four vertices We can define it as follows

```
#!/usr/bin/env python3
import math
# unit cube around the origin centered at 0,0,0 with sides of length 0.5
cube_verts=[
    [-0.5, -0.5, -0.5], # back bottom left
    [0.5, -0.5, -0.5], # back bottom right
    [0.5, 0.5, -0.5], # back top right
    [-0.5, 0.5, -0.5], # back top left
    [-0.5, -0.5, 0.5], # front bottom left
    [0.5, -0.5, 0.5], # front bottom right
    [0.5, 0.5, 0.5], # front top right
    [-0.5, 0.5, 0.5] # front top left
]

# normals for each face
cube_normals=[
    [0, 0, -1], # pointing out of the back
    [0, 0, 1], # pointing out of the front
    [0, -1, 0], # pointing out of the bottom
    [0, 1, 0], # pointing out of the top
    [-1, 0, 0], # pointing out of the left
    [1, 0, 0] # pointing out of the right
]

# texture coordinates

cube_uv=[
    [0, 0], # bottom left
    [1, 0], # bottom right
    [1, 1], # top right
    [0, 1] # top left
]

## todo write out the face data note we can share normals and uv's
## the back face is done for you.
faces=[
    [1, 1, 1], [2, 2, 1], [3, 3, 1],[4, 4, 1], # back face 
]

with open("cube.obj", "w") as file:
    for vertex in cube_verts:
        file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
    for normal in cube_normals:
        file.write(f"vn {normal[0]} {normal[1]} {normal[2]}\n")
    for st in cube_uv :
        file.write(f"vt {st[0]} {st[1]}\n")
    # write the faces Note these are 1-based indices
    for i in range(0, len(faces), 4):
        # for ease we can build a string and write it in one go
        file.write(f"f {faces[i][0]}/{faces[i][1]}/{faces[i][2]}")
        file.write(f"  {faces[i+1][0]}/{faces[i+1][1]}/{faces[i+1][2]}") 
        file.write(f"  {faces[i+2][0]}/{faces[i+2][1]}/{faces[i+2][2]}")
        file.write(f"  {faces[i+3][0]}/{faces[i+3][1]}/{faces[i+3][2]}\n")
```

--

## exercise

- using the code above write the remaining faces of the cube
- open the file in maya and check it is correct
- a solution is provided in the code directory
  - Think how you could do this as a triangle mesh


