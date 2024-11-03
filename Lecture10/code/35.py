#!/usr/bin/python3
from PIL import Image, ImageDraw
import math

def draw_polyline(canvas, pointList, colour) -> None:
    pointTuple = tuple(pointList)
    canvas.line(pointTuple, colour)


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


im = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(im)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)
rainbow = (red, yellow, green, cyan, blue, purple)

points = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]
for count in range(0, 6):
    draw_polyline(canvas, points, rainbow[count])
    points = rotatePoints(points, 0.1)
im.show()
