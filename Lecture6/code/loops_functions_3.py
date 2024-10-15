#!/usr/bin/env python3
from PIL import Image, ImageDraw


def draw_box(canvas, x, y, h, w, colour):
    canvas.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), colour)


im = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(im)
w = 50
h = 50
y = 200
for x in range(1, 5):
    draw_box(canvas, x * 100, y, h, w, (255, 255, 0))
im.show()
