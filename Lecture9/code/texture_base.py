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


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
circle_colour = (255, 0, 0)  # red colour
step = 128
line_thickness = 10

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_circle(
            canvas, x + step / 2, y + step / 2, step / 2, circle_colour, line_thickness
        )

image.save("baseColor.png")
