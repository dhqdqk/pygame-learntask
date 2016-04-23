#!/usr/bin/env pythn
#coding:utf-8

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'    # 背景图片
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0 # 窗口中坐标；（0，0）在左上角
move_x, move_y = 0, 0

my_event = pygame.event.Event(KEYDOWN, {'key': K_SPACE, 'mod': 0, 'unicode': u' '}) # 创建触发事件；按键为空格键
pygame.event.post(my_event) # 传递自定义的事件

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1 # 按下左方向键，坐标x减1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
            elif event.key == K_SPACE:
                print event.mod # 当按下空格键时，输出mod的值
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
    
    x += move_x
    y += move_y
    
    screen.fill((0, 0, 0))
    screen.blit(background, (x, y)) # 绘制背景图片，其左上角是操作坐标
    pygame.display.update()
    
    