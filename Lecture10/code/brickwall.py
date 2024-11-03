#!/usr/bin/python3
from PIL import Image, ImageDraw
import random
import math

def draw_polyline(canvas, pointList, colour) -> None:
    pointTuple = tuple(pointList)
    canvas.line(pointTuple, colour)

def draw_polygon(canvas, pointList, colour) -> None:
    pointTuple = tuple(pointList)
    canvas.polygon(pointTuple, colour, colour)

def translatePoint(point, dx, dy) -> (float, float):
    return (point[0] + dx, point[1] + dy)

def translatePoints(points, dx, dy) -> list:
    newPoints = list()
    for p in points:
        newPoints.append(translatePoint(p, dx, dy))
    return newPoints

def scalePoint(point, sx, sy) -> (float, float):
    return (point[0] * sx, point[1] * sy)

def scalePoints(points, sx, sy) -> list:
    newPoints = list()
    for p in points:
        newPoints.append(scalePoint(p, sx, sy))
    return newPoints

def rotatePoint(point, theta) -> (float, float):
    return (
        point[0] * math.cos(theta) + point[1] * math.sin(theta),
        -point[0] * math.sin(theta) + point[1] * math.cos(theta),
    )

def rotatePoints(points, theta) -> list:
    newPoints = list()
    for p in points:
        newPoints.append(rotatePoint(p, theta))
    return newPoints

cement = (200, 200, 200)
brick = (178, 34, 34)
resolution = 1024
step = 128
im = Image.new("RGB", (resolution, resolution), cement)
canvas = ImageDraw.Draw(im)

points = [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]
lineShift = True
for x in range(0, resolution+1, step):
    for y in range(0, resolution, math.floor(step/2)):
        newPoints = scalePoints(points, 115, 55)
        newPoints = rotatePoints(newPoints, random.uniform(-0.05,0.05))
        if lineShift :
            newPoints = translatePoints(newPoints, x, y)
            lineShift = False
        else :
            newPoints = translatePoints(newPoints, x+step/2, y)
            lineShift = True
        draw_polygon(canvas, newPoints, brick)
im.show()
