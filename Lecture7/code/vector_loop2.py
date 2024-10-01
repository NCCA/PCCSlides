#!/usr/bin/env python3
from PIL import Image, ImageDraw
import random
import math


def draw_segment(canvas, start, direction, colour) -> None:
    """
    Draws a line segment on the given canvas.

    Args:
        canvas: The canvas object on which to draw the line segment.
        start (tuple): The start point of the line segment as a two-element tuple.
        direction (tuple): The direction vector of the line segment as a two-element tuple.
        colour (tuple): The color of the segment's outline as an RGB tuple.

    Returns:
        None
    """
    canvas.line(
        ((start[0], start[1]), (start[0] + direction[0], start[1]+direction[1])),
        colour
    )

image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
start_point = (200,200)
for i in range(1, 100):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    x_n = x/math.sqrt(x*x+y*y)
    y_n = y/math.sqrt(x*x+y*y)
    x = x_n*100
    y = y_n*100
    draw_segment(canvas, start_point, (x,y), (255, 255, 0))

image.show()
