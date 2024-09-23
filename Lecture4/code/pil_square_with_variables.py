#!/usr/bin/env python
from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 255)
draw_colour = (0, 0, 255)
image = Image.new("RGB", window_size, background_colour)
canvas = ImageDraw.Draw(image)
canvas.line(((0, 0), (100, 0)), draw_colour)
canvas.line(((100, 0), (100, 100)), draw_colour)
canvas.line(((100, 100), (0, 100)), draw_colour)
canvas.line(((0, 100), (0, 0)), draw_colour)
image.show()
