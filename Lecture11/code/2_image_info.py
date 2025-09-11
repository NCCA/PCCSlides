#!/usr/bin/env -S uv run --script
from PIL import Image

im = Image.open("green.jpg")
print(im.size)
print(f"Width is: {im.width}, heights is: {im.height}")
im.show()
