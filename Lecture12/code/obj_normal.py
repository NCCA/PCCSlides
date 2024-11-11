#!/usr/bin/env python3
import math

def calc_normal(v1, v2) :
    
    n=[v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]]
    # normalize the normal
    length = math.sqrt((n[0]**2 + n[1]**2 + n[2]**2))
    if length == 0:
        return n
    n[0] /= length
    n[1] /= length
    n[2] /= length
    return n

triangle = [[2.0, 0.0, 0.0], [0.0, 4.0, 0.0], [-2.0, 0.0, 0.0]]

faces = [[0, 1, 2]]

normals=[]
normals.append(calc_normal(triangle[0], triangle[1]))
normals.append(calc_normal(triangle[1], triangle[2]))
normals.append(calc_normal(triangle[2], triangle[0]))

with open("triangle2.obj", "w") as file:
    for vertex in triangle:
        file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
    for normal in normals:
        file.write(f"vn {normal[0]} {normal[1]} {normal[2]}\n")
    # write the faces Note these are 1-based indices
    for face in faces:
        file.write(f"f {face[0]+1}//{face[0]+1} {face[1]+1}//{face[1]+1} {face[2]+1}//{face[2]+1}\n")
        