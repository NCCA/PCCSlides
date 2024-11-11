#!/usr/bin/env python3
from PIL import Image

fg = Image.open("green.jpg")
bg = Image.open("background.jpg")
mask = Image.new("L", fg.size, 0)
# matte extraction
for x in range(0, bg.width):
    for y in range(0, bg.height):
        pixel = fg.getpixel((x, y))
        if pixel[1] < (pixel[0] + pixel[2]) * 0.65:
            mask.putpixel((x, y), (255))
        else:
            mask.putpixel((x, y), (0))


result = Image.new("RGB", bg.size, 0)
for x in range(0, result.width):
    for y in range(0, result.height):
        maskPixel = mask.getpixel((x, y))
        fgPixel = fg.getpixel((x, y))
        bgPixel = bg.getpixel((x, y))
        if maskPixel > 128:
            result.putpixel((x, y), fgPixel)
        else:
            result.putpixel((x, y), bgPixel)
result.show()
