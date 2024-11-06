#!/usr/bin/python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        grey = int((max(list(pixel))+min(list(pixel)))/2)
        newPixel = (grey, grey, grey)
        im.putpixel((x, y), newPixel)
im.show()
