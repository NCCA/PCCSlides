#!/usr/bin/env python3
from PIL import Image, ImageDraw
from random import randint


def draw_hollow_box(canvas, x, y, h, w, colour):
    canvas.line(((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)), colour)

def draw_solid_box(canvas, x, y, h, w, colour):
    canvas.polygon(((x, y), (x + w, y), (x + w, y + h), (x, y + h)), c, colour)

im = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(im)
for x in range(1, 5):
    for y in range(1, 5):
        h = randint(20, 60)
        w = randint(20, 60)
        c = (randint(0, 256), randint(0, 256), randint(0, 256))
        draw_solid_box(canvas, x * 100, y * 100, h, w, c)
im.show()
