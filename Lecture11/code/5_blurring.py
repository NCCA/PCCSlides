#!/usr/bin/python3
from PIL import Image

im = Image.open("green.jpg")
for x in range(1, im.width-1):
    for y in range(1, im.height-1):
        averageR = 0
        averageG = 0
        averageB = 0
        pixels = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        for coordinate in pixels:
            pixel = im.getpixel(coordinate)
            averageR = averageR + pixel[0]
            averageG = averageG + pixel[1]
            averageB = averageB + pixel[2]
        averageR = int(averageR / 9)
        averageG = int(averageG / 9)
        averageB = int(averageB / 9)
        newPixel = (averageR, averageG, averageB)
        im.putpixel((x, y), newPixel)
im.show()
