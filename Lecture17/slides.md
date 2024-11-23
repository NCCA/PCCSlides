## Lesson 17: Python in Autodesk Maya

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

## Recap: Procedural content

- A procedure is the instruction or set of instructions to be executed
- Content can be anything we are presenting to the user

--

## Recap: libararies


---

## Why Python in Maya?

- Automate repetitive tasks
- Create custom tools for artists
- Implement procedural content generation:
  - Speeds up asset creation
  - Allows for flexibility and scalability
  - Enables iterative design

--

### Maya's Scripting Capabilities

- Python Integration in Maya:
  - A Python API for scripting
  - Compatible with MEL (Maya Embedded Language)
- Access Python in Maya
  - Script Editor: Write and execute Python commands
  - Python Plug-ins: Extend Maya’s functionality

---

### Setting up Python in Maya

- Script Editor allows write, execute, and save Python scripts
- Access via Windows > General Editors > Script Editor
- Import Maya Modules:
```python
import maya.cmds as cmds
```

--

## Core Python Modules in Maya

- **maya.cmds**:
  - Main module for interacting with Maya's commands.
  - Examples: Creating objects, setting attributes, querying data.
- **maya.OpenMaya**:
  - Advanced API for lower-level interactions.
  - Old API
- **maya.api.OpenMaya**
  - Advanced API, version 2.0

--

## maya.cmds

- Every action in Maya is a command
- You can run this command using the script
```python
import maya.cmds as cmds
cmds.ls()
cmds.sphere( radius=4 )
```

--

## maya.cmds: an explanation

- **import maya.cmds as cmds** imports **cmds** module from **maya** library
  - it will be referred to as just **cmds*
- command **ls** returns the names of objects in the scene
  - we are using it as a cheap way to deselect objects
- what the command **cmds.sphere( radius=4 )** do?

---

## Creating objects

```python
import maya.cmds as cmds
cmds.polyCube(name="MyCube", width=2, height=2, depth=2)
```

--

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

---

## Procedural content in Maya

- Procedural Content created algorithmically instead of manually.
- Applications in Maya:
  - Automatic creation of assets (e.g., buildings, trees).
  - Randomised or rule-based placement.
  - Pattern and structure generation.
  
--

## Creating procedural geometry

```python
import maya.cmds as cmds
for i in range(10):
    cmds.torus(name=f"Donut_{i}")
    cmds.move(i * 2, 0, 0, f"Donut_{i}")
```

--

## Using Randomness for Variation

- Use Python’s **random** module to introduce variation.

```python
import maya.cmds as cmds
import random
for i in range(10):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    cmds.polySphere(name=f"Sphere_{i}")
    cmds.move(x, y, 0, f"Sphere_{i}")
```

--

## Generating Patterns and Grids

- Procedural Grid Example:

```python
import maya.cmds as cmds
import random
for x in range(5):
    for y in range(5):
        cmds.polyCube(name=f"Cube_{x}_{y}")
        cmds.move(x * 2, y * 2, 0)
```

- Use case: creating city layouts, modular patterns, or grids of objects.

--

## Rule-Based Procedural Systems

- Defining Rules control how objects are placed or transformed.

```python
import maya.cmds as cmds
for i in range(10):
    cmds.polyCube(name=f"Step_{i}")
    cmds.move(i, i, 0, f"Step_{i}")
```

---

### Example: creating a Solar System
```python
import maya.cmds as cmds

def createSatelite(star, numOfMoons, distance, scaleFactor):
	incr = 360.0/numOfMoons
	newStars = []
	for i in range(numOfMoons):
		satellite = cmds.duplicate(star)
		newStars.append(satellite)
		cmds.xform(satellite, ro=[0,i*incr,0],r=True, os=True)
		cmds.xform(satellite, s=[scaleFactor, scaleFactor, scaleFactor], r=True)
		cmds.xform(satellite, t=[distance,0,0],r=True, os=True)
	for i in range(numOfMoons):
		cmds.parent(newStars[i],star)

cmds.select(all=True)
cmds.delete()
Sun = cmds.sphere(name='sun')
createSatelite(Sun[0], 12, 20, 0.2)
```

---

## Procedural Textures and Shading

```python
import maya.cmds as cmds
for i in range(10):
    material = cmds.shadingNode("lambert", asShader=True, name=f"Shader_{i}")
    cmds.setAttr(f"{material}.color", random.random(), random.random(), random.random(), type="double3")
    cmds.polySphere(name=f"Sphere_{i}")
    cmds.select(f"Sphere_{i}")
    cmds.hyperShade(assign=material)
```

---

## Procedural terrain generation

- Create a grid and adjust heights based on noise.
- Adjust the colour based on the height

--

### Procedural terrain generation: the Python code
```python
import maya.cmds as cmds
import random
import math
 # the idea is described here: https://www.redblobgames.com/maps/terrain-from-noise/

def noiseMap(width, height, scale):
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            noise[i][j] = scale * random.random() # (0,1]
    return noise

def Elevation(terrain, width, height, sharpness):
	noiseMap3 = noiseMap(width/4, height/4, 1.4)
	noiseMap2 = noiseMap(width/2, height/2, 1.2)
	noiseMap1 = noiseMap(width, height, 1.0)
	for y in range(height):
		for x in range(width):
			pointy = noiseMap3[x/4][y/4] + 0.4* noiseMap2[x/2][y/2] + 0.2* noiseMap1[x][y]
			pointy = math.pow(pointy, sharpness)
			cmds.xform(terrain + ".vtx["+ str(y*width+x) +"]", r=True, t=[0, pointy, 0])
    
cmds.select(all=True)
cmds.delete()
height=32
width=32
smoothness = 2
sharpness = 6.0
terrain=cmds.polyPlane(n="plane1",h=100, w=100, sx=(width-1), sy=(height-1))
Elevation(terrain[0], width, height, sharpness)    
cmds.polyAverageVertex(iterations = smoothness)
cmds.select(terrain)
cmds.polySmooth()
```

---

# Conclusion

- **What have you learned today**
  - How to create objects in Maya using Python
- **Homework**
  - Can you extend the code to add colours to the terrain? 

--

# Next time

- **What will you learn next time**
  - How to animate objects in Maya
  - How to add UI using Maya scripts

--

# Q&A and discussion
- **Open Floor for Questions**

