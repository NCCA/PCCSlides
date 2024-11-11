#!/usr/bin/env python3
from PIL import Image


def key(img, min, max) -> Image:
    result = Image.new("RGBA", img.size, 0)
    delta = max - min
    oodelta = 1.0 / delta
    for x in range(0, img.width):
        for y in range(0, img.height):
            pixel = img.getpixel((x, y))
            alpha = (pixel[1] - (pixel[0] + pixel[2]) * 0.5) / 255.0
            alpha = (alpha - min) * oodelta
            alpha = 1 - alpha
            if alpha < 0:
                alpha = 0
            if alpha > 1:
                alpha = 1
            newPixel = (
                int(pixel[0] * alpha),
                int(pixel[1] * alpha),
                int(pixel[2] * alpha),
                int(255 * alpha),
            )
            result.putpixel((x, y), newPixel)
    return result


def blendRGBA(fg, bg) -> tuple:
    a = fg[3] / 255.0
    return (
        int(fg[0] + bg[0] * (1 - a)),
        int(fg[1] + bg[1] * (1 - a)),
        int(fg[2] + bg[2] * (1 - a)),
        1,
    )


def over(fg, bg) -> Image:
    result = Image.new("RGB", bg.size, 0)
    for x in range(0, result.width):
        for y in range(0, result.height):
            fgPixel = fg.getpixel((x, y))
            bgPixel = bg.getpixel((x, y))
            opPixel = blendRGBA(fgPixel, bgPixel)
            result.putpixel((x, y), opPixel)
    return result


fg = Image.open("green.jpg")
bg = Image.open("background.jpg")
newFg = key(fg, 0.05, 0.1)
result = over(newFg, bg)
result.show()
