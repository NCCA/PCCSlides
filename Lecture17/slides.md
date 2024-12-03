### Lesson 17: Python in  Maya

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Introduction to Python in Autodesk Maya
- **What will you learn today:**
  - How to create objects in Maya using Python
  - Procedural content creation in Maya

---

### Maya as a scripting Engine

- at it's simplest maya is a scripting engine that can run MEL language scripts.
- When maya starts up it executes multiple scripts located in the directory 

``` $MAYA_LOCATION/scripts/startup/ ```

- This makes it possible to fully customize the look and feel of maya.

--

## MEL (Maya Embedded Language)

>As a language, MEL is descended from UNIX shell scripting. This means MEL is strongly based on executing commands to accomplish things (like executing commands in a UNIX shell), rather than manipulating data structures, calling functions, or using object oriented methods as in other languages.

--

# [MEL](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Scripting/files/GUID-60178D44-9990-45B4-8B43-9429D54DF70E-htm.html)

- Maya’s user interface is created primarily using MEL, and MEL provides an easy way to extend the functionality of Maya. 
- Everything you can do using Maya’s graphical interface can be automated and extended using MEL. 
- Familiarity with MEL can deepen your understanding of and expertise with Maya.
- it’s easy to perform a task in the graphical interface, then drag the resulting commands from the Script Editor to the shelf to create a button. 

--

# Do I need MEL?

- Mel is still the low level core of maya, as a power user (TD) it can be useful to know how to write mel scripts.
- However, for most users it is better to use Python as it is a more modern language and is more widely used in the industry.
- maya.cmds is a python module that wraps the mel commands so you can use them in python.
  - because of this the way we interact with maya is very similar in both languages.

---


## The script editor

![](images/mel1.png)

- The script editor can be launched by pressing the icon at the bottom right of the screen.
- simple mel commands can also be executed in the mel dialog to the left.

--

## The script editor

![](images/mel2.png)

--

## The script editor

- The script editor has two tabs at the bottom, these allow us to switch between mel and python.
- We can also load in files to edit and run.
- Feedback is provided in the output window above the script editor.

---

## a simple commands

- **Create a sphere:**

```python
cmds.polySphere()
```

- This will create a simple polysphere at the origin there are some things to note
  - it has a default name of pSphere1
  - it is selected by default
  - The command returns the name of the object created.

```
# Result: ['pSphere1', 'polySphere1']
```


--

### Create, edit, and query modes

- many of the commands have different modes outlined in the documentation.

![](images/mel3.png)

- by default the command is in create mode, but we can also query and edit the object.

--

## Query mode

- Query the radius of the sphere:

```python
radius=cmds.polySphere(q=True, r=True)
print(radius)
```

- What happens if the object is not selected?
- Always best to name the object we want to query.

```
radius=cmds.polySphere('pSphere1', q=True, r=True)
print(radius)
```

--

## Edit mode

- Edit the radius of the sphere:

```python
cmds.polySphere('pSphere1', e=True, r=2)
```

- In this case we are naming the object and editing the radius, however if selected this would affect the selected object.

--

## edit and query mode

- we can only edit / query one attribute at a time
- if we need to change more than one object we need to do them individually.

```python
cmds.polySphere('pSphere1', e=True, r=2)
cmds.polySphere('pSphere1', e=True, sx=10)
cmds.polySphere('pSphere1', e=True, sy=10)
```

---


## Maya Python cookbook

- most of the following examples will show you simple code recipes to do certain tasks in maya.

- This helps to combine things together into bigger scripts. Lets start with a simple example.


```python
cmds.file(new=True, f=True)
```
- this will not ask to save the current scene and can be useful when starting a new script.


--

## Python in Maya

- all of the python structures we have used so far will work in maya.
- All the data types (int, float, string, list, tuple, dictionary) are available.
- We can use loops, conditionals, functions, classes, and modules.

--

## A function to scatter spheres

- Lets write a simple function that will scatter spheres in the scene.

```python
import random

def scatter_spheres(num,x_range=10,y_range=10,z_range=10,radius=0.5):
    for _ in range(num):
        x=random.uniform(-x_range,x_range)
        y=random.uniform(-y_range,y_range)
        z=random.uniform(-z_range,z_range)
        cmds.polySphere(r=radius)
        cmds.move(x,y,z)

scatter_spheres(200,10,0,10,1.0)

```

--

## A note on numbering

- maya will check names when you create things.
- In the previous example if we run the ```scatter_spheres``` command again it will re-number the spheres from where it left off.
- always best to name objects if you want to query them later.


---

## Transforming Objects

- the commands **move**, **rotate** and **scale** transform object by performing one command

```python
import maya.cmds as cmds
cmds.polyCube(name="MyCube", width=2, height=2, depth=2)
cmds.move(5, 0, 0, "MyCube")
cmds.rotate(45, 0, 0, "MyCube")
cmds.scale(2, 2, 2, "MyCube")
position = cmds.getAttr("MyCube.translate")
```

--

## Transforming Objects

- More control can be achieved with **xform**

```python
import maya.cmds as cmds
cubeObject = cmds.polyCube(name="MyCube", width=2, height=2, depth=2)
cmds.xform(cubeObject, t=[5,0,0],r=True, os=True) #translate by (5,0,0), relative transformation in object space
cmds.xform(cubeObject, ro=[45,0,0],r=True, os=True) #rotate by 45 degrees around x, relative transformation in object space
cmds.xform(cubeObject, s=[2, 2, 2], r=True) #uniform scale by 2, relative transformation
```

--

## Setting Attributes

```python
# lets delete all objects
cmds.select(all=True)
cmds.delete()
#lets create a nurb's cube
cmds.nurbsCube(w=3, name='Cube1')
cmds.getAttr('Cube1.tx')
cmds.getAttr('Cube1.ty')
cmds.getAttr('Cube1.tz')

# let's make sure 'Cube1' is selected
cmds.select('Cube1', replace=True)
#let's change its translation attributes
cmds.setAttr('Cube1.tx', 1)
cmds.setAttr('Cube1.ty', 2)
cmds.setAttr('Cube1.tz', 3)
```

---

## Selection and Querying

- We can select all object in the scene using the  select

```python
cmds.select(all=True)
cmds.delete()
```

- If we want more control we need to use the ls command.


--

## Selection and Querying

- ls works a little like the linux command, but we can choose what we want to select.

```python
objects=cmds.ls()
for obj in objects:
    print(obj)
```

- we can also use wildcards to select objects.

```python
objects=cmds.ls('pSphere*')
for obj in objects:
    print(obj)
```

--

## Selection and Querying

- we can also query the selection

```python
selected=cmds.ls(sl=True)
for obj in selected:
    print(obj)
```

--

## Selection and Querying

- we can also query the type of object

```python
# Get all mesh objects in the scene
meshes = cmds.ls(type='mesh')

# Iterate through each mesh and delete its parent transform node
for mesh in meshes:
    parent = cmds.listRelatives(mesh, parent=True)
    if parent:
        cmds.delete(parent)
```

--

## type flag

- the type flag can be used to query objects of a certain type. 
- we can see all the types by running the following command.

```python
cmds.ls(nt=True)
```

- as you can see there are many types of objects in maya.

---


## maya.OpenMaya

- This is a Python wrapper for the Maya C++ API, and referred to as Python API 1.0. 
- It is suitable for developing plug-ins, and other tasks that require functionality not exposed by MEL. 
- To understand the exposed classes, you should refer to the conceptual topics and the "C++ API Reference" in the Maya Developer Help.
- This gives us a lot more low level control over the Maya including the DAG and direct access to nodes.

--

## maya.api.OpenMaya

- This is a Python wrapper for the Maya C++ API, and referred to as Python API 2.0. 
- This wrapper has better performance and is more "Pythonic" than the Python API 1.0. 
- It is also a newer API, and is still under development, so not all classes exposed in 1.0 are available. 
- Try to use this if possible.

--

## MVectors

- The MVector class is a 3D vector class that is used in the Maya API.
- It is used to represent 3D points and vectors in the 3D space.
- It is a very useful class for performing 3D math operations.

```python
from maya.api.OpenMaya import MVector

# Create vectors
vec1 = MVector(1, 2, 3)
vec2 = MVector(4, 5, 6)

# Basic operations
add_result = vec1 + vec2  # Vector addition
sub_result = vec1 - vec2  # Vector subtraction
scale_result = vec1 * 2   # Scaling by a scalar
length = vec1.length()    # Vector magnitude (length)
normalized = vec1.normal()  # Normalized vector (unit vector)

# Dot and cross product
dot_product = vec1 * vec2  # Dot product
cross_product = vec1 ^ vec2  # Cross product

# Display results
print(f"Add: {add_result}")
print(f"Subtract: {sub_result}")
print(f"Scaled: {scale_result}")
print(f"Length: {length}")
print(f"Normalized: {normalized}")
print(f"Dot Product: {dot_product}")
print(f"Cross Product: {cross_product}")
```

--

## MMatrix

- The MMatrix class is a 4x4 matrix class that is used in the Maya API.
- It is used to represent 4x4 matrices in the 3D space.

```python
from maya.api.OpenMaya import MMatrix

# Create matrices
mat1 = MMatrix([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

mat2 = MMatrix([[2, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 2]])

# Basic operations
mult_result = mat1 * mat2  # Matrix multiplication
transpose_result = mat1.transpose()  # Transpose of a matrix
inverse_result = mat1.inverse()  # Inverse of a matrix

# Accessing individual elements
element = mat1.getElement(1,1)  # Access element at row 1, column 1

# Display results
print(f"Matrix Multiplication: {mult_result}")
print(f"Transpose: {transpose_result}")
print(f"Inverse: {inverse_result}")
print(f"Element at (1, 1): {element}")
```

--

## Combining MVector and MMatrix

- You can multiply an MVector by an MMatrix to transform the vector using the matrix.

```python
from maya.api.OpenMaya import MVector, MMatrix

# Create a vector
vec = MVector(1, 2, 3)

# Create a transformation matrix (scaling by 2)
scale_matrix = MMatrix([[2, 0, 0, 0],
                        [0, 2, 0, 0],
                        [0, 0, 2, 0],
                        [0, 0, 0, 1]])

# Transform the vector using the matrix
transformed_vec = vec * scale_matrix

# Display result
print(f"Original Vector: {vec}")
print(f"Transformed Vector: {transformed_vec}")
```

--

## Rotating a Vector Using a Rotation Matrix

```python
from maya.api.OpenMaya import MVector, MMatrix

import math

# Create a vector
vec = MVector(1, 0, 0)

# Define a rotation matrix (90 degrees around the Z-axis)
theta = math.radians(90)
rotation_matrix = MMatrix([[math.cos(theta), -math.sin(theta), 0, 0],
                           [math.sin(theta),  math.cos(theta), 0, 0],
                           [0,                0,              1, 0],
                           [0,                0,              0, 1]])

# Rotate the vector
rotated_vec = vec * rotation_matrix

# Display results
print(f"Original Vector: {vec}")
print(f"Rotated Vector: {rotated_vec}")
```


--

## combining matrices

- we can combine matrices to create a new matrix.

```python
from maya.api.OpenMaya import MVector, MMatrix

# Create a scaling matrix
scale_matrix = MMatrix([[2, 0, 0, 0],
                        [0, 2, 0, 0],
                        [0, 0, 2, 0],
                        [0, 0, 0, 1]])

# Create a translation matrix (translate by 5 units along X, Y, Z)
translation_matrix = MMatrix([[1, 0, 0, 5],
                               [0, 1, 0, 5],
                               [0, 0, 1, 5],
                               [0, 0, 0, 1]])

# Combine transformations
combined_matrix = scale_matrix * translation_matrix

# Transform a vector
vec = MVector(1, 1, 1)
transformed_vec = vec * combined_matrix

# Display results
print(f"Combined Transformation Matrix: {combined_matrix}")
print(f"Transformed Vector: {transformed_vec}")
```

---

## MTransformationMatrix

- The MTransformationMatrix class is a 4x4 transformation matrix class that is used in the Maya API.
- It is is used to handle 3D transformations such as translation, rotation, scaling, and shear. 
- It provides convenient methods to manipulate and query transformations.

--

### Creating a Transformation Matrix

```python
m=MTransformationMatrix()
m.setTranslation(MVector(2,3,4),om.MSpace.kWorld)
m.setRotation(om.MEulerRotation(0,20,0))
m.setScale(MVector(2.5,3.12,4.2),om.MSpace.kWorld)
print(m.asMatrix())

# extract the data

print(m.rotation())
print(m.scale(om.MSpace.kWorld))
print(m.translation(om.MSpace.kWorld))
```

```

---

## Next Time

- We have looked at some of the basics of maya python
- next time we will look at some more functions
- we will write some scripts to create useful tools in maya.