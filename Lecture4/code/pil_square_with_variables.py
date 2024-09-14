from PIL import Image, ImageDraw

window_size = (640, 480)
background_colour = (255, 255, 20)
draw_colour = (0, 255, 255)
im = Image.new('RGB', window_size, background_colour)
draw = ImageDraw.Draw(im)
draw.line( ( (0, 0), (100,0)), draw_colour)
draw.line( ( (100, 0), (100,100)), draw_colour)
draw.line( ( (100, 100), (0,100)), draw_colour)
draw.line( ( (0, 100), (0,0)), draw_colour)
im.show()
