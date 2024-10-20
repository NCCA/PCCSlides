from PIL import Image, ImageDraw

def draw_coordinate_axes(resolution, colour) -> None:
	canvas.line(((resolution/2, 0), (resolution/2, resolution)), colour)
	canvas.line(((0, resolution/2), (resolution, resolution/2)), colour)

resolution = 1024 #1k image, i.e. 1024x1024 
background_colour = (0,0,0) #black background
line_colour = (255, 255, 155) #white line colour
step = 128

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)
draw_coordinate_axes(resolution, line_colour)

image.show()
