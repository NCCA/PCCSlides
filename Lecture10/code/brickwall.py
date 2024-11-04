#!/usr/bin/env python3
import math
import random

from PIL import Image, ImageDraw




def draw_polygon(canvas, pointList, colour) -> None:
    pointTuple = tuple(pointList)
    canvas.polygon(pointTuple, colour, colour)


def translate_point(point, dx, dy) -> (float, float):
    return (point[0] + dx, point[1] + dy)


def translate_points(points, dx, dy) -> list:
    new_points = list()
    for p in points:
        new_points.append(translate_point(p, dx, dy))
    return new_points


def scale_point(point, sx, sy) -> (float, float):
    return (point[0] * sx, point[1] * sy)


def scale_points(points, sx, sy) -> list:
    new_points = list()
    for p in points:
        new_points.append(scale_point(p, sx, sy))
    return new_points


def rotate_point(point, theta) -> (float, float):
    return (
        point[0] * math.cos(theta) + point[1] * math.sin(theta),
        -point[0] * math.sin(theta) + point[1] * math.cos(theta),
    )


def rotate_points(points, theta) -> list:
    new_points = list()
    for p in points:
        new_points.append(rotate_point(p, theta))
    return new_points


cement = (200, 200, 200)
brick = (178, 34, 34)
resolution = 1024
step = 128
im = Image.new("RGB", (resolution, resolution), cement)
canvas = ImageDraw.Draw(im)

points = [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]
lineShift = True
for x in range(0, resolution + 1, step):
    for y in range(0, resolution, math.floor(step / 2)):
        new_points = scale_points(points, 115, 55)
        new_points = rotate_points(new_points, random.uniform(-0.05, 0.05))
        if lineShift:
            new_points = translate_points(new_points, x, y)
            lineShift = False
        else:
            new_points = translate_points(new_points, x + step / 2, y)
            lineShift = True
        canvas.polygon( new_points, brick)
im.show()
