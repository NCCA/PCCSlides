#!/usr/bin/env python3
from PIL import Image, ImageDraw

im = Image.new("RGB", (640, 480), (255, 255, 20))
draw = ImageDraw.Draw(im)
draw.line(((0, 0), (100, 0)), (0, 255, 255))
draw.line(((100, 0), (100, 100)), (0, 255, 255))
draw.line(((100, 100), (0, 100)), (0, 255, 255))
draw.line(((0, 100), (0, 0)), (0, 255, 255))
im.show()
