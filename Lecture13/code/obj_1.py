#!/usr/bin/env python3


triangle = [[2.0, 0.0, 0.0], [0.0, 4.0, 0.0], [-2.0, 0.0, 0.0]]

faces = [[0, 1, 2]]


with open("triangle1.obj", "w") as file:
    for vertex in triangle:
        file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
    # write the faces Note thes are 1-based indices
    for face in faces:
        file.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")
