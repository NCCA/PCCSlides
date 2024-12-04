import maya.cmds as cmds



def hello() :
    print("Hello from NCCA functions")


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

