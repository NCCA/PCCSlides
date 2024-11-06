#!/usr/bin/python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        grey = int((pixel[0] * 0.299 + pixel[1] * 0.5870 + pixel[2] * 0.1140))
        newPixel = (grey, grey, grey)
        im.putpixel((x, y), newPixel)
im.show()
