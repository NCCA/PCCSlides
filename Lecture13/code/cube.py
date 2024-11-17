#!/usr/bin/env python3
import math
# unit cube around the origin centered at 0,0,0 with sides of length 0.5
cube_verts=[
    [-0.5, -0.5, -0.5], # back bottom left
    [0.5, -0.5, -0.5], # back bottom right
    [0.5, 0.5, -0.5], # back top right
    [-0.5, 0.5, -0.5], # back top left
    [-0.5, -0.5, 0.5], # front bottom left
    [0.5, -0.5, 0.5], # front bottom right
    [0.5, 0.5, 0.5], # front top right
    [-0.5, 0.5, 0.5] # front top left
]

# normals for each face
cube_normals=[
    [0, 0, -1], # pointing out of the back
    [0, 0, 1], # pointing out of the front
    [0, -1, 0], # pointing out of the bottom
    [0, 1, 0], # pointing out of the top
    [-1, 0, 0], # pointing out of the left
    [1, 0, 0] # pointing out of the right
]

# texture coordinates

cube_uv=[
    [0, 0], # bottom left
    [1, 0], # bottom right
    [1, 1], # top right
    [0, 1] # top left
]

## todo write out the face data note we can share normals and uv's
## the back face is done for you.
faces=[
    [1, 1, 1], [2, 2, 1], [3, 3, 1],[4, 4, 1], # back face 
]

with open("cube.obj", "w") as file:
    for vertex in cube_verts:
        file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
    for normal in cube_normals:
        file.write(f"vn {normal[0]} {normal[1]} {normal[2]}\n")
    for st in cube_uv :
        file.write(f"vt {st[0]} {st[1]}\n")
    # write the faces Note these are 1-based indices
    for i in range(0, len(faces), 4):
        # for ease we can build a string and write it in one go
        file.write(f"f {faces[i][0]}/{faces[i][1]}/{faces[i][2]}")
        file.write(f"  {faces[i+1][0]}/{faces[i+1][1]}/{faces[i+1][2]}") 
        file.write(f"  {faces[i+2][0]}/{faces[i+2][1]}/{faces[i+2][2]}")
        file.write(f"  {faces[i+3][0]}/{faces[i+3][1]}/{faces[i+3][2]}\n")