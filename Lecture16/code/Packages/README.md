# Packages

This example shows how to create a package using uv then run it as a package or using it in another local project.

The code was initially created as follows

```
uv init --package BouncingBall
cd BouncingBall
uv add nccapy
```

The bouncingball class used in the lectures was copied to the BouncingBall/src/bouncingball directory and __init__.py was modified to include

```python
from .bouncingball import BouncingBall
```

A ```__main__.py``` was also added and the following test program introduced

```python
from .bouncingball import BouncingBall

if __name__ == "__main__":
    ball = BouncingBall(1.0, (0, 10), (0, -2.0))
    for i in range(10):
        ball.update(0.01)
        print(ball.position)
```

We can now run

```zsh
uv run python -m bouncingball
pygame 2.6.1 (SDL 2.28.4, Python 3.13.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
(0.0, 9.98)
(0.0, 9.97)
(0.0, 9.97)
(0.0, 9.98)
(0.0, 10.0)
(0.0, 10.03)
(0.0, 10.069999999999999)
(0.0, 10.12)
(0.0, 10.18)
(0.0, 10.25)
```

## Building a Packages

You can run ```uv build``` in the BouncingBall folder to generate a wheel

```zsh
uv build
Building source distribution (uv build backend)...
Building wheel from source distribution (uv build backend)...
Successfully built dist/bouncingball-0.1.0.tar.gz
Successfully built dist/bouncingball-0.1.0-py3-none-any.whl
```

## Using the package

In root folder I generated an empty project using

```zsh
uv init TestBall
cd TestBall
uv add nccapy
```

To add the local bouncingball package we need to edit the pyproject.toml and add the following

```toml
dependencies = [
    "nccapy>=0.1.7",
    "bouncingball",
]

[tool.uv.sources]
bouncingball = { path = "../BouncingBall/" }
```

In particular the ```[tool.uv.sources]``` tells uv where to look for the package, once saved we can run ```uv sync``` to add this to our project.
