from maya.api.OpenMaya import MVector

# Create vectors
vec1 = MVector(1, 2, 3)
vec2 = MVector(4, 5, 6)

# Basic operations
add_result = vec1 + vec2  # Vector addition
sub_result = vec1 - vec2  # Vector subtraction
scale_result = vec1 * 2  # Scaling by a scalar
length = vec1.length()  # Vector magnitude (length)
normalized = vec1.normal()  # Normalized vector (unit vector)

# Dot and cross product
dot_product = vec1 * vec2  # Dot product
cross_product = vec1 ^ vec2  # Cross product

# Display results
print(f"Add: {add_result}")
print(f"Subtract: {sub_result}")
print(f"Scaled: {scale_result}")
print(f"Length: {length}")
print(f"Normalized: {normalized}")
print(f"Dot Product: {dot_product}")
print(f"Cross Product: {cross_product}")
