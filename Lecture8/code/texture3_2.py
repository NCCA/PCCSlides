#!/usr/bin/env python3


from PIL import Image, ImageDraw
import math


def draw_square_tile(canvas, x, y, size, colour1, colour2) -> None:
    for height in range(y, y + size, 1):
        t = (height - y) / size
        colour_r = math.floor(colour1[0] + t * (colour2[0] - colour1[0]))
        colour_g = math.floor(colour1[1] + t * (colour2[1] - colour1[1]))
        colour_b = math.floor(colour1[2] + t * (colour2[2] - colour1[2]))
        colour = (colour_r, colour_g, colour_b)
        canvas.line(
            ((x + t * size / 2, y + t * size), (x + size - t * size / 2, y + t * size)),
            colour,
        )


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
line_colour_1 = (255, 0, 0)  # red colour
line_colour_2 = (0, 255, 0)  # green colour
step = 128

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

draw_square_tile(canvas, 0, 0, step, line_colour_1, line_colour_2)

image.show()
