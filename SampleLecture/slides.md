### Writing Slides with Markdown

- press the right arrow key to continue


---

### Overview

- This slide set will show examples of how to write slides using markdown
- It will also include some of the more complex elements where you need to embed html or javascript
- This can be used along with the index.html file as a starting point / reference
- **now press the down key!**

--

## Navigation 

- Use the arrow keys to move between slides
- Pressing the ```s``` key will open the speaker notes
- Pressing the ```f``` key will open full screen mode
- Pressing the ```b``` key will open a black screen
- Pressing the ```ESC``` will give full overview of slides

Note:
  The notes keyword is used to add speaker notes to a slide. 
  These notes are not visible to the audience.
  Note the new line and the Tabs

--

### Menu Button

- The home button at the top left returns to the first slide, but can be altered to go to a different url if required
- The menu button at the bottom left opens a menu with many options including themes 

--


### Structure of slides

- I tend to group topics into vertical sections each slide has a ```--``` to separate them in the markdown file
- Horizontal slides are created using the ```---``` separator and I use these for core heading topics 
- Make sure the spaces are correct or the slide will not render correctly you basically need a blank line between each slide

---


### Part One basic reveal.js

- Bullets are easy you just use the ```-``` symbol
- You can also use numbers
  - Indentation is used to create sub bullets
  - You can also use numbers

--

### numbers

1. This is a numbered list
2. This is the second item
  1. This is a sub item
  2. This is another sub item
3. This is the third item

--

## fragments (press down!)

* Fragments are used to animate items on a slide press right to continue <!-- .element: class="fragment" -->
* I tend not to use these <!-- .element: class="fragment" -->
* but you can add them if you wish <!-- .element: class="fragment" -->
* they can be used to reveal items one at a time <!-- .element: class="fragment" -->

Note:
  If using a markdown file you need to add the element tags to get it to render correctly

--

## more complex fragments

* default is fade in <!-- .element: class="fragment" -->
* highlight red <!-- .element: class="fragment highlight-red" -->
* fade in then out <!-- .element: class="fragment fade-in-then-out" -->
* slide up while fading in <!-- .element: class="fragment fade-up" -->
* slide down while fading in <!-- .element: class="fragment fade-down" -->
* slide left while fading in <!-- .element: class="fragment fade-left" -->
* slide right while fading in <!-- .element: class="fragment fade-right" -->



---

## C-Code

```c
#include <stdio.h>
int main()
{
  printf("Hello World\n");
  return 0;
}
```

--

# Python Code

```python
print("Hello World")
```

---

#### Runable Python (using PyScript)

- The following code will run inline python, we need a target div to display the output
- Note we need a unique div name for each code block

```python
<script type="py-editor" target="editor1">
import this
</script>
<div id="editor1" style="font-size: 18px; text-align: left; overflow:scroll; height:250px;"></div>
```

<script type="py-editor" target="editor1">
import this
</script>
<div id="editor1" style="font-size: 18px; text-align: left; overflow:scroll; height:250px;"></div>


--

# Code from file

- Code can be loaded from a file it will be placed in the text edit
- note the size and scroll bars are set in the div

```python
<script type="py-editor" src="code/python.py"  target="editor2"></script>
<div id="editor2" style="font-size: 18px; text-align: left; overflow-y: scroll; height:400px;"></div>
```

--

## Code from file

<script type="py-editor" src="code/python.py"  target="editor2"></script>
<div id="editor2" style="font-size: 18px; text-align: left; overflow-y: scroll; height:400px;"></div>


