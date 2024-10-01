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
vec_b = (-50, 20)
vec_a_plus_b = (vec_a[0]+vec_b[0],vec_a[1]+vec_b[1]) # Implementation of vector addition
start_a = (100,50)
start_b = (start_a[0]+vec_a[0], start_a[1]+vec_a[1]) # Position the vector b for its start point coincide with end point of vector a
draw_segment(canvas, start_a, vec_a, (0, 255, 255))
draw_segment(canvas, start_b, vec_b, (0, 255, 0))
draw_segment(canvas, start_a, vec_a_plus_b, (255, 255, 0))
image.show()
