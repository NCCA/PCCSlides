#!/usr/bin/env python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        newPixel = (pixel[0] + 40, pixel[1] + 40, pixel[2] + 40)
        im.putpixel((x, y), newPixel)
im.show()
