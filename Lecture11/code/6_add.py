#!/usr/bin/env python3
from PIL import Image

im1 = Image.open("background.jpg")
im2 = Image.open("green.jpg")

for x in range(0, im1.width):
    for y in range(0, im1.height):
        pixel1 = im1.getpixel((x, y))
        pixel2 = im2.getpixel((x, y))
        newPixel = (pixel1[0] + pixel2[0], pixel1[1] + pixel2[1], pixel1[2] + pixel2[2])
        im1.putpixel((x, y), newPixel)
im1.show()
