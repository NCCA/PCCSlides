#!/usr/bin/python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        newPixel = (int(pixel[0]*0.25), int(pixel[1]*1.25), int(pixel[2]))
        im.putpixel((x, y), newPixel)
im.show()
