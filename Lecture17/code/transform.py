import maya.cmds as cmds

cmds.polyCube(name="MyCube", width=2, height=2, depth=2)
cmds.move(5, 0, 0, "MyCube")
cmds.rotate(45, 0, 0, "MyCube")
cmds.scale(2, 2, 2, "MyCube")
position = cmds.getAttr("MyCube.translate")
