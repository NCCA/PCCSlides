from PIL import Image, ImageDraw
import math

def draw_square_tile(canvas, x, y, size, colour1, colour2) -> None:
    for height in range(y, y+size, 1):
        t = (height-y)/size
        colour_r = math.floor(colour1[0]+t*(colour2[0]-colour1[0]))
        colour_g = math.floor(colour1[1]+t*(colour2[1]-colour1[1]))
        colour_b = math.floor(colour1[2]+t*(colour2[2]-colour1[2]))
        colour = (colour_r, colour_g, colour_b)
        canvas.line(((x + t*size/2, y+t*size), (x+size-t*size/2, y+t*size)), colour)

def draw_circle(canvas, cx, cy, r, col) -> None:
    dr = 5
    drRad = dr / 360.0 * 2 * math.pi
    for theta in range(0, 360, dr):
        thetaRad = (theta / 360.0) * (2 * math.pi)
        x1 = cx + r * math.cos(thetaRad)
        y1 = cy + r * math.sin(thetaRad)
        x2 = cx + r * math.cos(thetaRad + drRad)
        y2 = cy + r * math.sin(thetaRad + drRad)
        canvas.line(((x1, y1), (x2, y2)), col)

resolution = 1024 #1k image, i.e. 1024x1024 
background_colour = (0,0,0) #black background
line_colour_1 = (255, 0, 0) #red colour
line_colour_2 = (0, 255, 0) #green colour
circle_colour = (255, 255, 255) #blue colour
step = 128

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_square_tile(canvas, x, y, step, line_colour_1, line_colour_2)
        draw_circle(canvas, x+step/2, y+step/2, step/2, circle_colour)

image.show()
