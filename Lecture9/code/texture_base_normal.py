#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math

def drawCircle(canvas, cx, cy, radius, colour, thickness) -> None:
    dr = 5
    drRad = dr / 360.0 * 2 * math.pi
    for theta in range(0, 360, dr):
        thetaRad = (theta / 360.0) * (2 * math.pi)
        x1 = cx + radius * math.cos(thetaRad)
        y1 = cy + radius * math.sin(thetaRad)
        x2 = cx + radius * math.cos(thetaRad + drRad)
        y2 = cy + radius * math.sin(thetaRad + drRad)
        canvas.line(((x1, y1), (x2, y2)), colour, thickness)
        
def normalMap(canvas, cx, cy, size) -> None:
    for pointX in range(size): #x is in-between 0 and size
        for pointY in range(size): #y is in-between 0 and size
            u = float(pointX*2)/size-1 #u is now [-1,1]
            v = float(pointY*2)/size-1 #v is also [-1,1]
            nx = u #normal, x coordinate
            ny = v #normal, y coordinate
            distanceSquared = u*u+v*v #distance in UV coordinates
            if distanceSquared >= 1.0:
                distanceSquared = 0.0
                nx = 0
                ny = 0
                nz = 1
            else:
                nz = math.sqrt(1.0 - distanceSquared) #normal, z coordinate
            #the normal (nx, ny, nz) should be unit (why?)
            colourX = math.floor((nx+1)*128)
            colourY = math.floor((ny+1)*128)
            colourZ = math.floor((nz+1)*128)
            canvas.point((pointX+cx,pointY+cy),(colourX, colourY, colourZ))

resolution = 1024  # 1k image, i.e. 1024x1024
backgroundColour = (0, 0, 0)  # black background
circleColour = (255, 0, 0)  # red colour
step = 128
lineThickness = 10

image = Image.new("RGB", (resolution, resolution), backgroundColour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        drawCircle(canvas, x + step / 2, y + step / 2, step / 2, circleColour, lineThickness)

image.save("baseColor.png")

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        normalMap(canvas, x, y, step)

image.save("NormalMap.png")
