#!/usr/bin/env python3
from PIL import Image, ImageDraw


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
vec_a = (20, 30)
start_a = (100,100)
start_b = (150,100)
start_c = (200,100)
draw_segment(canvas, start_a, vec_a, (0, 255, 255))
draw_segment(canvas, start_b, (vec_a[0]*2, vec_a[1]*2), (0, 255, 0))
draw_segment(canvas, start_c, (vec_a[0]*(-0.5), vec_a[1]*(-0.5)), (255, 255, 0))
image.show()
