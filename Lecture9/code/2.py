#!/usr/bin/env python3
from PIL import Image

im = Image.open("green.jpg")
im.save("green_new.jpg")
