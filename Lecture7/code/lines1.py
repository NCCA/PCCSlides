#!/usr/bin/env -S uv run --script
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
        ((start[0], start[1]), (start[0] + direction[0], start[1] + direction[1])),
        colour,
    )


image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
draw_segment(canvas, (100, 50), (-100, 50), (255, 255, 0))
image.show()
