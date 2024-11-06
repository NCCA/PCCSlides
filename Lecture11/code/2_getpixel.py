#!/usr/bin/python3
from PIL import Image, ImageDraw

im = Image.open("green.jpg")
pixel = im.getpixel((100, 100))
print(pixel)
im.show()
