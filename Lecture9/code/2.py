#!/usr/bin/env -S uv run --script
from PIL import Image

im = Image.open("green.jpg")
im.save("green_new.jpg")
