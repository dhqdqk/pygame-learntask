#!/usr/bin/env python
#coding:utf-8

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

all_colors = pygame.Surface((4096, 4096), depth=24)

# 15的二进制为1111；r & 15（按位与）的结果是0到15内的整数, 相当于r%16，按位运算更快
# r>>4指将r的二进制右移去掉4个位；
for r in xrange(256):
    print r + 1, "out of 256"
    x = (r & 15) * 256
    y = (r >> 4) * 256
    for g in xrange(256):
        for b in xrange(256):
            all_colors.set_at((x+g, y+b), (r, g, b))

pygame.image.save(all_colors, "allcolors.bmp")