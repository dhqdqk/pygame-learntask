#!/usr/bin/env python
#coding:utf-8

import pygame
import time
from pygame.locals import *
from sys import exit

'''
测试RGB的成像原理；画出三原色的通道，控制混合比例并显示混合色
'''

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE)

def create_scales(height):
    # 创建三个（640，80）的颜色通道
    red_scale_surface = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    
    # 宽度方向将三个颜色上色；注意x/640.是小数除
    for x in xrange(640):
        c = int((x / 640.) * 255)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return  red_scale_surface, green_scale_surface, blue_scale_surface

red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()   # 加快退出速度
            exit()
    
    screen.fill((0, 0 , 0))
    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))
    
    x, y = pygame.mouse.get_pos()
    
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component * 80 and y < (component + 1) * 80:
                color[component] = int((x / 639.) * 255.)
                # 当鼠标点下时的y坐标在某个通道内,获取x坐标所在点的色值
        pygame.display.set_caption("pygame color test -" + str(tuple(color)))
    
    for component in range(3):
        pos = (int((color[component] / 255.) * 639), component * 80 + 40)
        pygame.draw.circle(screen, (255, 255, 255), pos, 15)
        #在每个通道上画一个白色的圆，半径15；初始位置x坐标在中间；
    
    pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))
    # 四边形的四个顶点坐标
    
    pygame.display.update()