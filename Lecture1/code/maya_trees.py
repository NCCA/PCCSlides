import maya.cmds as cmds
import random
import math

def simple_tree(x: float, z: float, height: float) -> None:
    """
    Generates a simple tree using Maya primitives.

    Args:
        x (float): The x-coordinate of the tree's base.
        z (float): The z-coordinate of the tree's base.
        height (float): The height of the tree.

    Returns:
        None
    """
    # Create the trunk
    trunk_height = height * 0.5
    trunk_radius = height * 0.1
    trunk = cmds.polyCylinder(h=trunk_height, r=trunk_radius, sx=20, sy=1, sz=1, name='tree_trunk')[0]
    cmds.move(x,  trunk_height / 2, z, trunk)

    # Create the foliage
    foliage_height = height * 0.5
    foliage_radius = height * 0.3
    foliage = cmds.polySphere(r=foliage_radius, sx=20, sy=20, name='tree_foliage')[0]
    cmds.move(x,  trunk_height + foliage_height / 2, z, foliage)



def scatter_trees(num_objects: int, area_size: float, min_distance: float) -> None:
    """
    Scatters trees randomly within a specified area ensuring no two objects occupy the same space.

    Args:
        num_objects (int): The number of objects to scatter.
        area_size (float): The size of the area within which to scatter the objects.
        min_distance (float): The minimum distance between any two objects.

    Returns:
        None
    """
    def is_valid_position(new_pos: tuple[float, float], existing_positions: list[tuple[float, float]]) -> bool:
        """
        Checks if the new position is valid (i.e., not too close to existing positions).

        Args:
            new_pos (tuple[float, float]): The new position to check.
            existing_positions (list[tuple[float, float]]): The list of existing positions.

        Returns:
            bool: True if the new position is valid, False otherwise.
        """
        for pos in existing_positions:
            if math.dist(new_pos, pos) < min_distance:
                return False
        return True

    positions = []
    for _ in range(num_objects):
        while True:
            x = random.uniform(-area_size / 2, area_size / 2)
            y = random.uniform(-area_size / 2, area_size / 2)
            if is_valid_position((x, y), positions):
                positions.append((x, y))
                break

    for pos in positions:
        simple_tree(pos[0], pos[1], 10)

# Example usage
scatter_trees(140, 150, 5)