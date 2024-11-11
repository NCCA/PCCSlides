#!/usr/bin/env python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        if pixel[1] > (pixel[0] + pixel[2]) * 0.6:
            newPixel = (0, 0, 0)
            im.putpixel((x, y), newPixel)
im.show()
