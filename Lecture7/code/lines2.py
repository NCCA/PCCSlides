#!/usr/bin/env python3
from PIL import Image, ImageDraw

def draw_segment(canvas, start, direction, colour) -> None:
    canvas.line(((start[0], start[1]), (start[0] + direction[0], start[1]+direction[1])), colour)

image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
draw_segment(canvas, (100, 100), (-100, 50), (255, 255, 0))
draw_segment(canvas, (280, 270), (-100, 50), (255, 255, 0))
draw_segment(canvas, (400, 30), (-100, 50), (255, 255, 0))
image.show()
