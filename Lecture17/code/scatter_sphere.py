import random


def scatter_spheres(num, x_range=10, y_range=10, z_range=10, radius=0.5):
    for _ in range(num):
        x = random.uniform(-x_range, x_range)
        y = random.uniform(-y_range, y_range)
        z = random.uniform(-z_range, z_range)
        cmds.polySphere(r=radius)
        cmds.move(x, y, z)


scatter_spheres(200, 10, 0, 10, 1.0)
