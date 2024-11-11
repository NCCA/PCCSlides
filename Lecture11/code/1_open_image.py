#!/usr/bin/env python3
from PIL import Image

im = Image.open("green.jpg")
print(im.size)
im.show()
