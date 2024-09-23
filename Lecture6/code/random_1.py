#!/usr/bin/python3
from PIL import Image, ImageDraw
from random import randint


def drawBox(im, x, y, h, w, c):
    draw.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), c)


im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
for x in range(1, 5):
    for y in range(1, 5):
        h = randint(20, 60)
        w = randint(20, 60)
        drawBox(im, x * 100, y * 100, h, w, (255, 255, 0))
im.show()
