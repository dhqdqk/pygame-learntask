#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame import *
from sys import exit

my_name = "panhaoqing"

pygame.init()

my_font = pygame.font.SysFont("arial", 64)
print my_font
name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
print name_surface
pygame.image.save(name_surface, "name.png")

import os
if os.path.exists("name.png"):
    print os.path.abspath("name.png")