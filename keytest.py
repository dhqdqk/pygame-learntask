#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

backgound_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        print 'space'
    
    pygame.display.update()