#!/usr/bin/env python
#coding:utf-8

''''
在（640，480）大小的框架内，以其四边为碰撞线，将图形以固定速率在随机地点出发还行；
碰到边时则反弹
'''
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
background_image_filename = 'sushiplate.jpg'
#　运动体
sprite_image_filename = 'fugu.png'

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

FPS = 50

x, y = randint(0, 640), randint(0,480)
# 游戏运行时运动体随机坐标处出现
speed_x, speed_y = 255.0, 255.0
# x和y方向的运行速率

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(sprite, (x,y))
    
    if FPS > 0:
        time_passed = clock.tick(FPS) # 指定FPS的值
    else:
        time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    #　print time_passed
    
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds
    # x,y在单位时间内移动的像素量
    
    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0.0
    # 如果运动体碰到左右边则将x方向速率反向
    
    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0.0
    # 如果运动体碰到上下边则将y方向速率反向
    
    pygame.display.update()