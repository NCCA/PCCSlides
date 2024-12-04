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
