#!/usr/bin/python3
from PIL import Image

def key(img, min) -> Image:
    mask = Image.new("L", img.size, 0)
    for x in range(0, img.width):
        for y in range(0, img.height):
            pixel = img.getpixel((x, y))
            if pixel[1] < (pixel[0] + pixel[2]) * 0.65:
                mask.putpixel((x, y), (255))
            else:
                mask.putpixel((x, y), (0))
    return mask


def over(fg, bg, mask) -> Image:
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
    return result


fg = Image.open("green.jpg")
bg = Image.open("background.jpg")
mask = key(fg, 0.65)
mask.show()
result = over(fg, bg, mask)
result.show()
