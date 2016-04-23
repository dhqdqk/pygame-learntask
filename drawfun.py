#!/usr/bin/env python
#coding:utf-8
'''
测试pygame.draw的图形功能
'''

import pygame
from pygame.locals import *
from sys import exit
from random import randint
from math import pi

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
#screen.fill((0, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
    
    # 矩形
    x, y = 0, 48
    for i in range(2, 5):
        rect = (x, x, y, y)
        a = pygame.draw.rect(screen, (0, 255, 0), rect, i)
        x = 64 * i
        y *= i
    rand_col = (randint(0, 249), randint(0, 249), randint(0, 249))
    # 多边形
    polygon = [(5, 5), (80, 5), (160, 125), (125, 195), (45, 225)]
    pygame.draw.polygon(screen, rand_col, polygon, 2)
    
    # 圆
    circle = (319, 239)
    pygame.draw.circle(screen, rand_col, circle, 35, 2)
    
    # 椭圆
    ellipse = (55, 55, 155, 255) # 椭圆外接矩形的坐标（长宽为椭圆的两个轴长）
    pygame.draw.rect(screen, (255, 255, 255), ellipse, 1)
    pygame.draw.ellipse(screen, (255, 255, 0), ellipse, 3)
    
    # 椭圆弧
    arc = (65, 65, 135, 235)
    pygame.draw.rect(screen, (255, 255, 255), arc, 1)
    pygame.draw.arc(screen, (0, 255, 255), arc, pi/2.0, pi, 2)
    
    # 线段
    s_pos = (25, 45),
    stop_pos = (150, 150)
    pygame.draw.line(screen, (0, 15, 155), s_pos, stop_pos, 2)
    pygame.display.update()
    