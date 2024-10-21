#!/usr/bin/env python3


from PIL import Image, ImageDraw

resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
line_colour = (255, 255, 155)  # white line colour
step = 128

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    canvas.line(((x, 0), (x + step, step)), (255, 255, 0))
    canvas.line(((x, step), (x + step, 0)), (255, 255, 0))

image.show()
