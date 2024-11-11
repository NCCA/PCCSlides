#!/usr/bin/env python3
from PIL import Image, ImageDraw

fg = Image.open("green.jpg")
bg = Image.open("background.jpg")
for x in range(0, bg.width):
    for y in range(0, bg.height):
        pixel = fg.getpixel((x, y))
        if pixel[1] < (pixel[0] + pixel[2]) * 0.65:
            bg.putpixel((x, y), pixel)
bg.show()
