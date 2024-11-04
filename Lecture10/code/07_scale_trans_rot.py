#!/usr/bin/env python3
import math

from PIL import Image, ImageDraw




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


def roate_point(point, theta) -> (float, float):
    return (
        point[0] * math.cos(theta) + point[1] * math.sin(theta),
        -point[0] * math.sin(theta) + point[1] * math.cos(theta),
    )


def roate_points(points, theta) -> list:
    new_points = list()
    for p in points:
        new_points.append(roate_point(p, theta))
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

points = [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]

for count in range(0, 6):
    new_points = scale_points(points, count * 60, count * 60)
    new_points = roate_points(new_points, (count * 5) / 360.0 * 2 * math.pi)
    new_points = translate_points(new_points, 320, 240)
    canvas.line( new_points, rainbow[count])
im.show()
