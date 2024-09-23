#!/usr/bin/python3
from PIL import Image, ImageDraw


def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)


im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
x = 300
y = 300
w = 100
h = 50
for x in (300, 320, 340, 360):
    drawBox(im, x, y, h, w, (255, 255, 0))
im.show()
