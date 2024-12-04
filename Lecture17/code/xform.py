import maya.cmds as cmds

cubeObject = cmds.polyCube(name="MyCube", width=2, height=2, depth=2)
cmds.xform(
    cubeObject, t=[5, 0, 0], r=True, os=True
)  # translate by (5,0,0), relative transformation in object space
cmds.xform(
    cubeObject, ro=[45, 0, 0], r=True, os=True
)  # rotate by 45 degrees around x, relative transformation in object space
cmds.xform(
    cubeObject, s=[2, 2, 2], r=True
)  # uniform scale by 2, relative transformation
