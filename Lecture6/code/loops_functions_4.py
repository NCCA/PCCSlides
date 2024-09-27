#!/usr/bin/env python3
from PIL import Image, ImageDraw


def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)


im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
w = 50
h = 50
y = 200
for x in range(1, 5):
    for y in range(1, 5):
        drawBox(im, x * 100, y * 100, h, w, (255, 255, 0))
im.show()
