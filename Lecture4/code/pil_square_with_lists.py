#!/usr/bin/env python3
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 255)
draw_colour = (0, 0, 255)
points = [(0, 0), (100, 0), (100, 100), (0, 100)]
image = Image.new("RGB", window_size, background_colour)
canvas = ImageDraw.Draw(image)
canvas.line((points[0], points[1]), draw_colour)
canvas.line((points[1], points[2]), draw_colour)
canvas.line((points[2], points[3]), draw_colour)
canvas.line((points[3], points[0]), draw_colour)
image.show()
