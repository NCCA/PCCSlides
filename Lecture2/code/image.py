#!/usr/bin/env python3
from PIL import Image

# by convention we use uppercase for constants
WIDTH = 400
HEIGHT = 300

img = Image.new(mode="RGB", size=(WIDTH, HEIGHT), color=(209, 123, 193))
img.show()
