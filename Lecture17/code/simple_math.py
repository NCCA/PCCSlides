from maya.api.OpenMaya import MMatrix, MVector

# Create a vector
vec = MVector(1, 2, 3)

# Create a transformation matrix (scaling by 2)
scale_matrix = MMatrix([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 1]])

# Transform the vector using the matrix
transformed_vec = vec * scale_matrix

# Display result
print(f"Original Vector: {vec}")
print(f"Transformed Vector: {transformed_vec}")
