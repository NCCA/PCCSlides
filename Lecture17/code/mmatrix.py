from maya.api.OpenMaya import MMatrix

# Create matrices
mat1 = MMatrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

mat2 = MMatrix([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]])

# Basic operations
mult_result = mat1 * mat2  # Matrix multiplication
transpose_result = mat1.transpose()  # Transpose of a matrix
inverse_result = mat1.inverse()  # Inverse of a matrix

# Accessing individual elements
element = mat1.getElement(1, 1)  # Access element at row 1, column 1

# Display results
print(f"Matrix Multiplication: {mult_result}")
print(f"Transpose: {transpose_result}")
print(f"Inverse: {inverse_result}")
print(f"Element at (1, 1): {element}")
