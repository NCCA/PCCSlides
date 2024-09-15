from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (0, 255, 255)
points = [(0, 0), (100,0), (100,100), (0, 100)]
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( points[0], points[1]), draw_colour)
draw.line( ( points[1], points[2]), draw_colour)
draw.line( ( points[2], points[3]), draw_colour)
draw.line( ( points[3], points[0]), draw_colour)
im.show()
