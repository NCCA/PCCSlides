import math

from maya.api.OpenMaya import MMatrix, MVector

# Create a vector
vec = MVector(1, 0, 0)

# Define a rotation matrix (90 degrees around the Z-axis)
theta = math.radians(90)
rotation_matrix = MMatrix(
    [
        [math.cos(theta), -math.sin(theta), 0, 0],
        [math.sin(theta), math.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
)

# Rotate the vector
rotated_vec = vec * rotation_matrix

# Display results
print(f"Original Vector: {vec}")
print(f"Rotated Vector: {rotated_vec}")
