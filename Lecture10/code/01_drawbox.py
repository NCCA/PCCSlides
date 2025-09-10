#!/usr/bin/env -S uv run --script

from PIL import Image, ImageDraw

im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
white = (255, 255, 255)
points = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]
draw.line(points, white)
im.show()
