#!/usr/bin/env python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 255)
draw_colour = (0, 0, 255)
origin_x = 0
origin_y = 0
points = [
    (origin_x, origin_y),
    (origin_x + 100, origin_y),
    (origin_x + 100, origin_y + 100),
    (origin_x, origin_y + 100),
]
image = Image.new("RGB", window_size, background_colour)
canvas = ImageDraw.Draw(image)
canvas.line((points[0], points[1]), draw_colour)
canvas.line((points[1], points[2]), draw_colour)
canvas.line((points[2], points[3]), draw_colour)
canvas.line((points[3], points[0]), draw_colour)
image.show()
