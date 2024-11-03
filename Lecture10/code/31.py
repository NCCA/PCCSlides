#!/usr/bin/python3
from PIL import Image, ImageDraw
from random import randint
import math


def translatePoints(points, dx, dy) -> list:
    newPoints = list()
    for p in points:
        newPoints.append((p[0] + dx, p[1] + dy))
    return newPoints


im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
white = (255, 255, 255)
green = (0, 255, 0)
points = list()
points.append((100, 100))
points.append((200, 100))
points.append((200, 200))
points.append((100, 200))
points.append((100, 100))
draw.line(tuple(points), white)
newPoints = translatePoints(points, 50, 50)
draw.line(tuple(newPoints), green)
im.show()
