#!/usr/bin/env python3
import turtle

running = True
while running:
    print("enter triangle, square, or exit:")
    entered = input()
    if entered == "triangle":
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
            continue
    if entered == "square":
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
            continue
    if entered == "exit":
        running = False
        print("exiting...")
    else:
        print("not a command")
