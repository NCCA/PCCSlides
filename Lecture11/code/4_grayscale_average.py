#!/usr/bin/env python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        grey = int((pixel[0] + pixel[1] + pixel[2]) / 3)
        newPixel = (grey, grey, grey)
        im.putpixel((x, y), newPixel)
im.show()
