#!/usr/bin/python3
from PIL import Image, ImageDraw
from random import randint
import math


im = Image.new("RGB", (640, 480), (100, 0, 20))
draw = ImageDraw.Draw(im)
white = (255, 255, 255)
points = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]
draw.line(tuple(points), white)
im.show()
