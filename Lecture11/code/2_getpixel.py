#!/usr/bin/env -S uv run --script
from PIL import Image

im = Image.open("green.jpg")
pixel = im.getpixel((100, 100))
print(pixel)
im.show()
