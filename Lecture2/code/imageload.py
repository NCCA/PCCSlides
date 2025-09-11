#!/usr/bin/env -S uv run --script
from PIL import Image

im = Image.open("Squirrel.tiff")
im.show()
im.save("xxx.jpg")
