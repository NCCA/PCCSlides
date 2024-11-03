#!/usr/bin/python3
from PIL import Image, ImageDraw

def draw_polyline(canvas, pointList, colour) -> None:
    #the function takes the list of points as an input, we need to convert to tuple
    pointTuple = tuple(pointList)
    #the line() function takes a tuple of points as a first argument
    canvas.line(pointTuple, colour)
    
def translatePoint(point, dx, dy) -> (float, float): #The function moves just one point given the offset
    return (point[0] + dx, point[1] + dy)

def translatePoints(points, dx, dy) -> list: #This function moves multiple points with the same offset
    newPoints = list()
    for p in points:
        newPoints.append(translatePoint(p, dx, dy))
    return newPoints


im = Image.new("RGB", (640, 480), (100, 0, 20))
canvas = ImageDraw.Draw(im)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)
rainbow = (red, yellow, green, cyan, blue, purple)
points = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]
tx = 40 #shift for x
ty = 40 #shift for y
for count in range(0, 6):
    draw_polyline(canvas, points, rainbow[count])
    points = translatePoints(points, 40, 40)
im.show()
