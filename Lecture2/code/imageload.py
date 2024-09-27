#!/usr/bin/env python3
from PIL import Image

im = Image.open("Squirrel.tiff")
im.show()
im.save("xxx.jpg")
