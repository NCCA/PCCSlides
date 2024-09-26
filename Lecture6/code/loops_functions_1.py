#!/usr/bin/env python
from PIL import Image, ImageDraw


def draw_box(canvas, x, y, height, width, colour) -> None:
    """
    Draws a box on the given canvas.

    Args:
        canvas: The canvas object on which to draw the box.
        x (int): The x-coordinate of the top-left corner of the box.
        y (int): The y-coordinate of the top-left corner of the box.
        height (int): The height of the box.
        width (int): The width of the box.
        colour (tuple): The color of the box's outline as an RGB tuple.

    Returns:
        None
    """
    canvas.line(
        ((x, y), (x + width, y), (x + width, y + height), (x, y + height), (x, y)),
        colour,
    )


image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
x = 300
y = 300
w = 100
h = 50
for x in (300, 320, 340, 360):
    draw_box(canvas, x, y, h, w, (255, 255, 0))
image.show()
