#!/usr/bin/env -S uv run --script

with open("test.txt", "w") as file:
    file.write("Hello, world!")
    file.writelines(["\n", "This is a test file."])

with open("test.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line)
