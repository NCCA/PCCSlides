#!/usr/bin/env python3

from PIL import Image, ImageDraw

resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
line_colour = (255, 255, 155)  # white line colour

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

canvas.line(((0, 0), (100, 100)), (255, 255, 0))
canvas.line(((0, 100), (100, 0)), (255, 255, 0))

image.show()
