#!/usr/bin/env python3
from PIL import Image

im = Image.open("green.jpg")
print(im.size)
print(f"Width is: {im.width}, heights is: {im.height}")
im.show()
