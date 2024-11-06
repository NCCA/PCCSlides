#!/usr/bin/python3
from PIL import Image

im1 = Image.open("background.jpg") 
im2 = Image.open("green.jpg")

mixValue = 0.2
oneMinusMV = 1 - mixValue

for x in range(0, im1.width):
    for y in range(0, im1.height):
        pixel1 = im1.getpixel((x, y))
        pixel2 = im2.getpixel((x, y))
        newR = int(pixel1[0]*mixValue + pixel2[0]*oneMinusMV)
        newG = int(pixel1[1]*mixValue + pixel2[1]*oneMinusMV)
        newB = int(pixel1[2]*mixValue + pixel2[2]*oneMinusMV)
        newPixel = (newR, newG, newB)
        im1.putpixel((x, y), newPixel)
im1.show()
