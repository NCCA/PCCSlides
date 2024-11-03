#!/usr/bin/python3
from PIL import Image, ImageDraw

def draw_polyline(canvas, pointList, colour) -> None:
    pointTuple = tuple(pointList)
    canvas.line(pointTuple, colour)

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

points = [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]

for count in range(0, 6):
    #note if you swap next two lines, you will get a different result
    newPoints = scalePoints(points, count * 80, count * 80)
    newPoints = translatePoints(newPoints, 320, 240)
    draw_polyline(canvas, newPoints, rainbow[count])
im.show()
