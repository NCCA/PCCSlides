#!/usr/bin/env python3
from PIL import Image, ImageDraw



def scale_point(point, sx, sy) -> (float, float):  
    # The function does non-uniform scaling for a point
    return (point[0] * sx, point[1] * sy)


def scale_points(points, sx, sy) -> list:  
    # The function does non-uniform scaling for a point set
    new_points = list()
    for p in points:
        new_points.append(scale_point(p, sx, sy))
    return new_points


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
    canvas.line( points, rainbow[count])
    points = scale_points(points, 1.1, 1.1)
im.show()
