#!/usr/bin/env python
#coding:utf-8
'''
通过方向键控制物体移动；只有8个方向：坐标轴向，及斜45°
'''

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)

background_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2(200, 150)
sprite_speed = 300.0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
    
    pressed_keys = pygame.key.get_pressed()
    
    key_direction = Vector2(0, 0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    #　判断x方向是否按下左右方向键；右为正方向
    
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1
    # 判断y方向是否按下上下方向键；下为正方向
    
    key_direction.normalise()
    
    screen.blit(background, (0,0))
    screen.blit(sprite, sprite_pos)
    
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    
    sprite_pos += key_direction * sprite_speed * time_passed_seconds
    # 计算式右边为单位时间内的位移
    
    pygame.display.update()