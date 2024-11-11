#!/usr/bin/env python3
from PIL import Image


def gammaCorrection(colour, gamma) -> tuple:
    unitColour = (colour[0] / 255, colour[1] / 255, colour[2] / 255)
    gammaColour = (
        pow(unitColour[0], 1 / gamma),
        pow(unitColour[1], 1 / gamma),
        pow(unitColour[2], 1 / gamma),
    )
    return (
        int(gammaColour[0] * 255),
        int(gammaColour[1] * 255),
        int(gammaColour[2] * 255),
    )


im = Image.open("green.jpg")
gamma = 2
for x in range(0, im.width):
    for y in range(0, im.height):
        pixel = im.getpixel((x, y))
        newPixel = gammaCorrection(pixel, gamma)
        im.putpixel((x, y), newPixel)
im.show()
