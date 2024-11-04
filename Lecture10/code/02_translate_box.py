#!/usr/bin/env python3
import math
from random import randint

from PIL import Image, ImageDraw


def translate_points(points, dx, dy) -> list:
    new_points = list()
    for p in points:
        new_points.append((p[0] + dx, p[1] + dy))
    return new_points


im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
white = (255, 255, 255)
green = (0, 255, 0)
points = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]
draw.line(tuple(points), white)
new_points = translate_points(points, 50, 50)
draw.line(tuple(new_points), green)
im.show()
