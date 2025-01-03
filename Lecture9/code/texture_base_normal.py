#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math


def draw_circle(canvas, cx, cy, radius, colour, thickness) -> None:
    dr = 5
    drRad = dr / 360.0 * 2 * math.pi
    for theta in range(0, 360, dr):
        thetaRad = (theta / 360.0) * (2 * math.pi)
        x1 = cx + radius * math.cos(thetaRad)
        y1 = cy + radius * math.sin(thetaRad)
        x2 = cx + radius * math.cos(thetaRad + drRad)
        y2 = cy + radius * math.sin(thetaRad + drRad)
        canvas.line(((x1, y1), (x2, y2)), colour, thickness)


def normal_map(canvas, cx, cy, size) -> None:
    for point_x in range(size):  # x is in-between 0 and size
        for point_y in range(size):  # y is in-between 0 and size
            u = float(point_x * 2) / size - 1  # u is now [-1,1]
            v = float(point_y * 2) / size - 1  # v is also [-1,1]
            nx = u  # normal, x coordinate
            ny = v  # normal, y coordinate
            distance_squared = u * u + v * v  # distance in UV coordinates
            if distance_squared >= 1.0:
                distance_squared = 0.0
                nx = 0
                ny = 0
                nz = 1
            else:
                nz = math.sqrt(1.0 - distance_squared)  # normal, z coordinate
            # the normal (nx, ny, nz) should be unit (why?)
            colour_x = math.floor((nx + 1) * 128)
            colour_y = math.floor((ny + 1) * 128)
            colour_z = math.floor((nz + 1) * 128)
            canvas.point((point_x + cx, point_y + cy), (colour_x, colour_y, colour_z))


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
circle_colour = (255, 0, 0)  # red colour
step = 128
lineThickness = 10

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_circle(
            canvas, x + step / 2, y + step / 2, step / 2, circle_colour, lineThickness
        )

image.save("baseColor.png")

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        normal_map(canvas, x, y, step)

image.save("normal_map.png")
