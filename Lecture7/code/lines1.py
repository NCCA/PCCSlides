#!/usr/bin/env python3
from PIL import Image, ImageDraw


def draw_line(canvas, start, direction, colour) -> None:
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
x = 300
y = 100
w = 100
h = 50
for x in (300, 320, 340, 360):
    y += 50
    h += 12
    w += 18
    draw_line(canvas, (x, y), (h, w), (255, 255, 0))
image.show()
