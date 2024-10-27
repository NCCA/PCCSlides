#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math

def drawCircle(canvas, cx, cy, radius, colour, thickness) -> None:
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
backgroundColour = (0, 0, 0)  # black background
circleColour = (255, 0, 0)  # red colour
step = 128
lineThickness = 10

image = Image.new("RGB", (resolution, resolution), backgroundColour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        drawCircle(canvas, x + step / 2, y + step / 2, step / 2, circleColour, lineThickness)

image.save("baseColor.png")
