#!/usr/bin/env python
#coding:utf-8

'''
直线运动
'''

import pygame
from pygame import *
from sys import exit

pygame.init()


screen = pygame.display.set_mode((640,480), 0, 32)
background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

x = 0.0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(sprite, (x,100))    # 初始位置
    
    x += 0.1    # 沿x方向的移动速率
    
    if x > 640.0:
        x = 0.0
    
    pygame.display.update()