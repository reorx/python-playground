#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

img = Image.new('RGB', (500, 500), "black")
pixels = img.load()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

for i in range(img.size[0]):
    for j in range(img.size[1]):
        j_flag = (j + i) % 2

        color = (255, 255, 0)
        if j_flag:
            color = RED
        else:
            color = GREEN

        pixels[i, j] = color

img.show()
