#!/usr/bin/env python
#coding:utf-8
'''
通过方向键控制物体移动；并可以转向移动；左右键控制转向，上下键控制上下移动
'''
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

background_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)
background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2(200, 150)
sprite_speed = 300.0
sprite_rotation = 0.0   # 初始角度
sprite_rotation_speed = 360.0  # 角速度

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
    
    pressed_keys = pygame.key.get_pressed()
    #print len(pressed_keys)
    
    rotation_direction = 0.0
    movement_direction = 0.0
    
    screen.blit(background, (0,0))
    
    # 角度转向，顺时针或逆时针
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.0
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.0
    
    # 前进后退
    if pressed_keys[K_UP]:
        movement_direction = +1.0
    if pressed_keys[K_DOWN]:
        movement_direction = -1.0
    
    # 将图像转向
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    # 获取转向后的图像的尺寸（和原图像不一样）
    w, h = rotated_sprite.get_size()
    # 转向后图像的坐标重新计算
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y  - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos)
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    # 单位时间后图像的角度；等号右边是需要转动的角度；
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    #　计算图像当前角度的向量（用三角函数计算，是单位化的）
    heading_x = sin(sprite_rotation*pi/180.0)
    heading_y = cos(sprite_rotation*pi/180.0)
    #　计算在当前角度方向的位移
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction
    
    sprite_pos += heading * sprite_speed * time_passed_seconds
    
    pygame.display.update()