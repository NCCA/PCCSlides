#!/usr/bin/env python

from PIL import Image, ImageDraw


image = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(image)
x = 300
y = 300
w = 100
h = 50
canvas.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), (255, 255, 0))
image.show()
