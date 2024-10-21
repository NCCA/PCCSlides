#!/usr/bin/env python3

from PIL import Image, ImageDraw


def draw_square_tile(canvas, x, y, size, colour) -> None:
    canvas.line(((x, y), (x + size, y + size)), colour)
    canvas.line(((x, y + size), (x + size, y)), colour)


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
line_colour = (255, 255, 155)  # white line colour
step = 128

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_square_tile(canvas, x, y, step, line_colour)

image.show()
