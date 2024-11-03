#!/usr/bin/python3
from PIL import Image, ImageDraw

def draw_polyline(canvas, pointList, colour) -> None:
    pointTuple = tuple(pointList)
    canvas.line(pointTuple, colour)


def scalePoint(point, sx, sy) -> (float, float): #The function does non-uniform scaling for a point
    return (point[0] * sx, point[1] * sy)


def scalePoints(points, sx, sy) -> list: #The function does non-uniform scaling for a point set
    newPoints = list()
    for p in points:
        newPoints.append(scalePoint(p, sx, sy))
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
    points = scalePoints(points, 1.1, 1.1)
im.show()
