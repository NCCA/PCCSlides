# Writing Slides with Markdown

Jon Macey

---

# Overview

- This slide set will show examples of how to write slides using markdown
- It will also include some of the more complex elements where you need to embed html or javascript
- This can be used along with the index.html file as a starting point / reference

---

### Part One basic reveal.js

- Bullets are easy you just use the ```-``` symbol
- You can also use numbers
  - Indentation is used to create sub bullets
  - You can also use numbers

--

## numbers


1. This is a numbered list
2. This is the second item
  1. This is a sub item
  2. This is another sub item
3. This is the third item

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
<script type="py-editor" src="docs/SampleLecture/code/python.py"  target="editor2"></script>
<div id="editor2" style="font-size: 18px; text-align: left; overflow-y: scroll; height:400px;"></div>
```

--

## Code from file

<script type="py-editor" src="docs/SampleLecture/code/python.py"  target="editor2"></script>
<div id="editor2" style="font-size: 18px; text-align: left; overflow-y: scroll; height:400px;"></div>


