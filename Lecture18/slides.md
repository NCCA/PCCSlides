## Lesson 18: Python in Maya 2

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- We will look at how maya python works
- How to create a simple tool (and design it)


---

## Python Paths

- maya will use the global python path which you can set as usual
- it is also possible to setup some default python behaviors using a file called ```userSetup.py```
- this lives in the default maya user directory as follows
```
# Windows
%HOMEDRIVE%\%HOMEPATH%\Documents\maya\[version]\scripts
# Linux 
~/maya/[version]/scripts
# Mac OSX
~/Library/Preferences/Autodesk/maya/[version]/scripts
```

--

## userSetup.py

- to add to the path in the userSetup.py file we can do the following

```
import sys
from pathlib import Path
sys.path.append(str(Path.home() / "scripts"))
```

--

## A Scripts Folder

- We will make a scripts folder for our maya scripts

```bash
mkdir ~/scripts
cd ~/scripts
touch NCCAFunctions.py
```

--

## NCCAFunctions.py

- We will put useful code in here

```python
def hello() :
  print("hello from NCCA Functions")
```

- we can now load this in maya

```python
from NCCAFunctions import hello
hello()
```

--

## [reload](https://docs.python.org/2/library/functions.html#reload)

- To help the development cycle, we can easily modify the script and call

```python

import NCCAFunctions
NCCAFunctions.hello()
# make changes to source.
from importlib import reload
reload (NCCAFunctions)
NCCAFunctions.hello()
```

- to reload the module from the source file, otherwise this will be the same module for the whole of the session.

---

## A turntable script

- We are going to create a camera turntable script
- This script will create a camera and animate it around the selected objects
- We try to automate as much of this as possible

--

## Program Design

1. check to see we have selected objects
2. calculate the center of the selected objects
3. get the radius of the bounding sphere
4. create a camera
5. animate the camera around the center of the selected objects

--

## Program Design

- We can create a number of re-usable functions to do this
- To start with we will create a function to calculate the center of the selected objects which we will use to aim the camera

```python
import maya.api.OpenMaya as om

def get_center_of_selection():
    # Get the current selection
    selection = om.MGlobal.getActiveSelectionList()
    if selection.length() == 0:
        print("No objects selected.")
        return None

    # Initialize variables for bounding box
    bbox_min = om.MVector(float('inf'), float('inf'), float('inf'))
    bbox_max = om.MVector(float('-inf'), float('-inf'), float('-inf'))

    # Iterate through the selection and calculate the bounding box
    for i in range(selection.length()):
        dag_path = selection.getDagPath(i)
        fn_node = om.MFnDagNode(dag_path)
        bbox = fn_node.boundingBox
        bbox_min = om.MVector(
            min(bbox_min.x, bbox.min.x),
            min(bbox_min.y, bbox.min.y),
            min(bbox_min.z, bbox.min.z)
        )
        bbox_max = om.MVector(
            max(bbox_max.x, bbox.max.x),
            max(bbox_max.y, bbox.max.y),
            max(bbox_max.z, bbox.max.z)
        )

    # Calculate the center of the bounding box
    center = (bbox_min + bbox_max) * 0.5
    return center
```


--

## bounding sphere radius

```python
import maya.cmds as cmds

def get_bounding_sphere_radius():
    """
    Calculate the radius of the bounding sphere of the selected objects in Maya.
    
    Returns:
        float: The radius of the bounding sphere.
        None: If no objects are selected.
    """
    # Get the selected objects
    selection = cmds.ls(selection=True)
    if not selection:
        print("No objects selected.")
        return None

    # Initialize variables for the bounding box
    bbox_min = [float('inf')] * 3
    bbox_max = [float('-inf')] * 3

    # Iterate over the selected objects and calculate the bounding box
    for obj in selection:
        # Get the bounding box of the object
        bbox = cmds.exactWorldBoundingBox(obj)
        # Update the overall bounding box
        bbox_min = [min(bbox_min[i], bbox[i]) for i in range(3)]
        bbox_max = [max(bbox_max[i], bbox[i+3]) for i in range(3)]

    # Calculate the center of the bounding box
    bbox_center = [(bbox_min[i] + bbox_max[i]) / 2.0 for i in range(3)]

    # Calculate the radius of the bounding sphere
    # Radius is the distance from the center to the farthest corner of the bounding box
    radius = ((bbox_max[0] - bbox_center[0]) ** 2 +
              (bbox_max[1] - bbox_center[1]) ** 2 +
              (bbox_max[2] - bbox_center[2]) ** 2) ** 0.5

    return radius

```


--

## turntable_camera 

```python
def turntable_camera(radius=10, center=(0,0,0),start_frame=1, end_frame=360, camera_name="turntable_camera"):
    """
    Creates an animated camera along a circular path.

    Parameters:
        radius (float): Radius of the circular path.
        start_frame (int): Starting frame of the animation.
        end_frame (int): Ending frame of the animation.
        camera_name (str): Name of the camera.
    """
    # Create the camera
    camera = cmds.camera(name=camera_name)
    camera_transform = camera[0]  # The transform node
    # Create the aim target (a locator)
    aim_target = cmds.spaceLocator(name=f"{camera_name}_target")[0]
    cmds.setAttr(f"{aim_target}.translate", *center)

    # Create a NURBS circle as the path
    circle_path = cmds.circle(name="camera_path", radius=radius, normal=(0, 1, 0))[0]

    # Attach the camera to the path using a motion path
    motion_path = cmds.pathAnimation(
        camera_transform, 
        c=circle_path, 
        follow=True, 
        followAxis="x", 
        upAxis="y", 
        worldUpType="vector", 
        worldUpVector=(0, 1, 0),
        startTimeU=0,
        endTimeU=1.0
    )

    # Ensure the motion path spans the full curve length
    cmds.setAttr(f"{motion_path}.fractionMode", True)  # Interpret uValue as normalized (0-1) across the entire curve

    # Keyframe the motion path's uValue for animation
    cmds.setAttr(f"{motion_path}.uValue", 0)  # Start at the beginning of the path
    cmds.setKeyframe(motion_path, attribute="uValue", t=start_frame)

    cmds.setAttr(f"{motion_path}.uValue", 1)  # End at the end of the path
    cmds.setKeyframe(motion_path, attribute="uValue", t=end_frame)

    # Set keyframe interpolation to linear for consistent speed
    cmds.selectKey(motion_path, attribute="uValue", keyframe=True)
    cmds.keyTangent(itt="linear", ott="linear")

    # Create an aim constraint
    cmds.aimConstraint(
        aim_target, camera_transform, 
        aimVector=(0, 0, -1),  # Camera aims down its negative Z-axis
        upVector=(0, 1, 0),    # Y-axis as the up direction
        worldUpType="scene"    # Use world up direction
    )

```

--

## Putting it all together.

[NCCAFunctions.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture18/code/NCCAFunctions.py)

```python
import NCCAFunctions

center=NCCAFunctions.get_center_of_selection()
radius=get_bounding_sphere_radius()
NCCAFunctions.turntable_camera(radius=radius+2,center=center,start_frame=1,end_frame=360,camera_name="turntable_camera")
```

---

# A simple GUI

- We can create a simple GUI using the maya.cmds module
- This can let us automate the process of creating the camera

![](images/gui.png)


--

## Code

[turntable_gui.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture18/code/turntable_gui.py)

```python
import NCCAFunctions
import maya.cmds as cmds


def create_turntable(radius, camera_name, start_frame, end_frame):
    # print(radius, camera_name, start_frame, end_frame)
    # see if we have anything selected
    selection = cmds.ls(selection=True)
    # if we have nothing selected then select just meshes
    if not selection:
        selection = cmds.ls(type="mesh")
        cmds.select(selection)
    center = NCCAFunctions.get_center_of_selection()
    bounds = NCCAFunctions.get_bounding_sphere_radius()
    # create a camera
    NCCAFunctions.turntable_camera(
        radius=radius + bounds,
        camera_name=camera_name,
        center=center,
        start_frame=start_frame,
        end_frame=end_frame,
    )


def turntable_gui():
    """
    Creates a simple Maya UI window with a button to execute a command.
    """
    # Window name
    window_name = "TurntableGUI"

    # Check if the window already exists
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    # Create a new window
    cmds.window(window_name, title="Turntable GUI", widthHeight=(300, 200))

    # Create a layout
    cmds.columnLayout(adjustableColumn=True)
    # Slider for radius offset
    radius_slider = cmds.floatSliderGrp(
        label="Radius", field=True, minValue=0.0, maxValue=50.0, value=2.0
    )
    # create a camera name text field
    camera_name = cmds.textFieldGrp(label="Camera Name", text="turntable_camera")
    # start frame
    start_frame = cmds.intFieldGrp(label="Start Frame", value1=1)
    # end frame
    end_frame = cmds.intFieldGrp(label="End Frame", value1=100)

    # Add a button
    cmds.button(
        label="Run Command",
        command=lambda x: create_turntable(
            cmds.floatSliderGrp(radius_slider, query=True, value=True),
            cmds.textFieldGrp(camera_name, query=True, text=True),
            cmds.intFieldGrp(start_frame, query=True, value1=True),
            cmds.intFieldGrp(end_frame, query=True, value1=True),
        ),  # Query the slider value
    )

    # Show the window
    cmds.showWindow(window_name)


# Run the function to create the window
turntable_gui()


```

---

# Conclusion

- **What have you learned today**
  - How to create UI
  - How to create tools in Maya
- **Homework**
  - The information from this session is enough for one of the coursework ideas, think about it!

--

# Next time

- **What will you learn next time**
  - We do not have any new material, so only revision weeks are coming!
  - Also we will be helping you with your Python assignments

--

# Q&A and discussion
- **Open Floor for Questions**
