#!/usr/bin/env python3
from PIL import Image

fg = Image.open("green.jpg")
mask = Image.new("L", fg.size, 0)
for x in range(0, fg.width):
    for y in range(0, fg.height):
        pixel = fg.getpixel((x, y))
        if pixel[1] < (pixel[0] + pixel[2]) * 0.65:
            mask.putpixel((x, y), (255))
        else:
            mask.putpixel((x, y), (0))
mask.show()
