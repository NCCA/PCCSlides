## Lesson 9: Texture maps, colour spaces

#### Jon Macey, Ian Stephenson, Oleg Fryazinov 

- **Course:** BA Computer Animation and Visual Effects
- **Level:** 4 
- **Unit:** Procedural Content Creation

---

# Session outline

- **Title:** Texture maps, colour spaces
- **What will you learn today:**
  - What is a texture map 
  - How to generate normal map using the code
  - More details about colour spaces
  - How to load and save files in Python

---

## Recap: Vectors

- A **vector** is a quantity that has length and direction
- A geometric vector is defined by a directed line segment

<img style="border: 0;" src="images/Desc1.png" width="15%">
<img style="border: 0;" src="images/Picture1.png" width="15%">
<img style="border: 0;" src="images/Desc2.png" width="15%">
<img style="border: 0;" src="images/Picture2.png" width="15%">
<img style="border: 0;" src="images/Desc3.png" width="15%">
<img style="border: 0;" src="images/Picture3.png" width="15%">

--

## Recap: Normalisation

- A vector whose length is equal to 1 is called **unit vector**
- If we multiply any vector by inverse of its length, we get a unit vector with the same direction
- Example: $ \vec{a} = (3,4)$, $ ||\vec{a}|| $ = $\sqrt{3^2+4^2}=5 $, $\vec{a_n} = (\frac{3}{5},\frac{4}{5})$

--

## Recap: Python libraries

- We use **import** keyword for importing the library
- We let Python know we are using the code from the library
- Import turtle graphics: 
```python
import turtle 
```

---

## goScripts 

- Most of you are used to just doing a double click to run software
- Under Linux things are a little different hence the need for extra scripts
  - **goMaya** runs Maya
  - goBlender runs Blender
  - goNuke, goHoudini, goToonz...
- The **&** makes the command run in the background: **goMaya&**

---


## Open image in PIL

- To open an image in PIL use *.open()* method

```python
from PIL import Image

im = Image.open("green.jpg")
im.show()
```

--

## Save image in PIL

- After you worked on an image, do some image processing or image manipulation you will likely want to save this new version of your image.
- Saving an image can be achieved by using *.save()* method with PIL library’s Image module in Python.

```python
from PIL import Image

im = Image.open("green.jpg")
im.save("green_new.jpg")
```

---

## Texture maps
- A texture map is a way of applying properties to a 3D model so as to alter its appearance using 2D images.
  - This can include its colour, fine detail, how shiny or metallic it looks, whether its transparent or if it glows.
- Texture maps are applied to a 2D representation of a 3D model also known as a **UV**.

--

## Physically-based Rendering pipeline
- PBR (Physically Based Rendering) is a texture workflow that aims to simulate how light reacts with a model to attempt to simulate real life materials.
- The PBR pipeline standardises ways of texturing
- Two different types of methodologies used which require different maps
  - *Metallic Roughness*: Base colour, Metallic, Roughness
  - *Specular Glossiness*: Diffuse, Specular, Glossiness

--

## Groups of texture maps
- **Geometry Altering Maps**: maps that have the ability to alter fine details of a model’s geometry
  - Bump map, normal map, displacement map
- **PBR rendering maps**: maps that simulate real-life materials
  - Base colour map, metallic map, roughness map
- Additional maps
  - Opacity map, emissive colour

---

## Create the base colour map

[texture1.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture9/code/texture1.py)

```python
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


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
circle_colour = (255, 0, 0)  # red colour
step = 128
line_thickness = 10

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        drawCircle(
            canvas, x + step / 2, y + step / 2, step / 2, circle_colour, line_thickness
        )

image.show()
```

--

## Save the base colour map

[texture2.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture9/code/texture_base.py)

```python
#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math


def draw_circle(canvas, cx, cy, radius, colour, thickness) -> None:
    dr = 5
    drRad = dr / 360.0 * 2 * math.pi
    for theta in range(0, 360, dr):
        thetaRad = (theta / 360.0) * (2 * math.pi)
        x1 = cx + radius * math.cos(thetaRad)
        y1 = cy + radius * math.sin(thetaRad)
        x2 = cx + radius * math.cos(thetaRad + drRad)
        y2 = cy + radius * math.sin(thetaRad + drRad)
        canvas.line(((x1, y1), (x2, y2)), colour, thickness)


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
circle_colour = (255, 0, 0)  # red colour
step = 128
line_thickness = 10

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_circle(
            canvas, x + step / 2, y + step / 2, step / 2, circle_colour, line_thickness
        )

image.save("baseColor.png")

```

---

## Colour models

- A colour model is a method for representing colours in a way that can be easily understood and manipulated by computers and humans.
- Common Color Models:
  - RGB (Red, Green, Blue): Used in digital displays.
  - HSV (Hue, Saturation, Value): Useful for colour manipulation.
  - CMYK (Cyan, Magenta, Yellow, Black): Primarily used in printing.

--

## RGB colour model

- An additive colour model that combines red, green, and blue light to create colours.
  - Additive Mixing: Colours are created by adding light.
  - Full intensity of each component (255, 255, 255) produces white, and absence (0, 0, 0) results in black.

--

## RGB Examples and Code
- **Red**: (255, 0, 0), **Green**: (0, 255, 0), **Blue**: (0, 0, 255), **White**: (255, 255, 255), **Black**: (0, 0, 0), **Yellow**: (255, 255, 0)

```python
from PIL import Image
img = Image.new("RGB", (128, 128), (255, 255, 0))  # Yellow
img.show()
```

--

## RGBA colour model

- A three-channel RGB color model supplemented with a fourth alpha channel.
- Alpha indicates how opaque each pixel
  - 0 is fully transparent, 255 is fully opaque

```python
from PIL import Image
img = Image.new("RGBA", (128, 128), (255, 255, 0, 255))  # Yellow
img.show()
```

--

## HSV Colour Model – Overview
- HSV Stands for Hue, Saturation, Value.
  - Hue: Represents the color type (0-360°, e.g., 0 = red, 120 = green).
  - Saturation: Intensity or purity of the color (0% to 100%).
  - Value: Brightness or lightness of the color (0% to 100%).
- Applications: Often used in image editing and computer vision as it closely aligns with human perception of color.

--

## CMYK Colour Model – Overview
- CMYK is a subtractive colour model used for printing.
  - Cyan (C), Magenta (M), Yellow (Y), Black (K) are the primary colours.
  - Unlike RGB, CMYK works by subtracting light reflected off a white background.
- How It Works:
  - In printing, colours are layered, with black (K) added for depth and detail.

---

## The opacity map
- The Opacity Map dictates how transparent a model is. This is useful for making material such as glass.
- The Opacity Map is a grey scale map. 
  - Black means the surface is completely transparent 
- Similar to alpha in RGBA model

--

## Create the opacity map

[texture3.py](https://github.com/NCCA/PCCSlides/blob/main/Lecture9/code/texture_base_opacity.py)

```python
#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math


def draw_circle(canvas, cx, cy, radius, colour, thickness) -> None:
    dr = 5
    drRad = dr / 360.0 * 2 * math.pi
    for theta in range(0, 360, dr):
        thetaRad = (theta / 360.0) * (2 * math.pi)
        x1 = cx + radius * math.cos(thetaRad)
        y1 = cy + radius * math.sin(thetaRad)
        x2 = cx + radius * math.cos(thetaRad + drRad)
        y2 = cy + radius * math.sin(thetaRad + drRad)
        canvas.line(((x1, y1), (x2, y2)), colour, thickness)


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
circle_colour = (255, 0, 0)  # red colour
step = 128
line_thickness = 10

image_base = Image.new("RGB", (resolution, resolution), background_colour)
canvas_base = ImageDraw.Draw(image_base)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_circle(
            canvas_base,
            x + step / 2,
            y + step / 2,
            step / 2,
            circle_colour,
            line_thickness,
        )

image_base.save("baseColorMap.png")

image_alpha = Image.new("RGB", (resolution, resolution), background_colour)
canvas_alpha = ImageDraw.Draw(image_alpha)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_circle(
            canvas_alpha,
            x + step / 2,
            y + step / 2,
            step / 2,
            (255, 255, 255),
            line_thickness,
        )

image_alpha.save("opacityMap.png")


```

---

## The normal map

- Normal mapping is technique that uses a texture map to define the normal vectors inside the texture
- When a lighting model is applied it gives the appearance of a non-flat surface.
- A normal map is a texture where the RGB colour values of each textel is used for the x, y and z values of a normal vector

[More information about normal mapping](https://jonshiach.github.io/graphics-book/_pages/09_Normal_mapping.html)

--

## Creating normal maps procedurally

- Step 1: for every pixel in the texture we define the unit normal vector
- Step 2: x of the unit normal is set to R component, y is for the G component and z is for the B component
  - The mapping is the following:
    - X: -1 to +1 : Red: 0 to 255
    - Y: -1 to +1 : Green: 0 to 255
    - Z:  0 to -1 : Blue: 128 to 255
- Step 3: write the mapped normal as the RGB colour

---

### Advanced example: creating normal map in Python

```python
#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math


def draw_circle(canvas, cx, cy, radius, colour, thickness) -> None:
    dr = 5
    drRad = dr / 360.0 * 2 * math.pi
    for theta in range(0, 360, dr):
        thetaRad = (theta / 360.0) * (2 * math.pi)
        x1 = cx + radius * math.cos(thetaRad)
        y1 = cy + radius * math.sin(thetaRad)
        x2 = cx + radius * math.cos(thetaRad + drRad)
        y2 = cy + radius * math.sin(thetaRad + drRad)
        canvas.line(((x1, y1), (x2, y2)), colour, thickness)


def normal_map(canvas, cx, cy, size) -> None:
    for point_x in range(size):  # x is in-between 0 and size
        for point_y in range(size):  # y is in-between 0 and size
            u = float(point_x * 2) / size - 1  # u is now [-1,1]
            v = float(point_y * 2) / size - 1  # v is also [-1,1]
            nx = u  # normal, x coordinate
            ny = v  # normal, y coordinate
            distance_squared = u * u + v * v  # distance in UV coordinates
            if distance_squared >= 1.0:
                distance_squared = 0.0
                nx = 0
                ny = 0
                nz = 1
            else:
                nz = math.sqrt(1.0 - distance_squared)  # normal, z coordinate
            # the normal (nx, ny, nz) should be unit (why?)
            colour_x = math.floor((nx + 1) * 128)
            colour_y = math.floor((ny + 1) * 128)
            colour_z = math.floor((nz + 1) * 128)
            canvas.point((point_x + cx, point_y + cy), (colour_x, colour_y, colour_z))


resolution = 1024  # 1k image, i.e. 1024x1024
background_colour = (0, 0, 0)  # black background
circle_colour = (255, 0, 0)  # red colour
step = 128
lineThickness = 10

image = Image.new("RGB", (resolution, resolution), background_colour)
canvas = ImageDraw.Draw(image)

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        draw_circle(
            canvas, x + step / 2, y + step / 2, step / 2, circle_colour, lineThickness
        )

image.save("baseColor.png")

for x in range(0, resolution, step):
    for y in range(0, resolution, step):
        normal_map(canvas, x, y, step)

image.save("normal_map.png")

```

---

# Conclusion

- **What have you learned today**
  - How to work with files in Python and PIL
  - Colour models
  - Texture maps
- **Homework**
  - Get your head around the advanced example might be enough

--

# Next time

- **What will you learn next time**
  - Transformations: translate, rotate, scale
  - How to position objects in space using code

--

# Q&A and discussion
- **Open Floor for Questions**

