from PIL import Image, ImageDraw

def draw_square_tile(canvas, x, y, size, colour) -> None:
	for height in range(y, y+size, 1):
		t = (height-y)/size;
		canvas.line(((x + t*size/2, y+t*size), (x+size-t*size/2, y+t*size)), colour)

resolution = 1024 #1k image, i.e. 1024x1024 
background_colour = (0,0,0) #black background
line_colour = (255, 255, 155) #white line colour
step = 128

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

draw_square_tile(canvas, 0, 0, step, line_colour)

image.show()
