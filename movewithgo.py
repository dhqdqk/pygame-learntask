#!/usr/bin/env python
#coding:utf-8

'''
用失量控制物体的移动速度和方向
'''

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(sprite, position)   # 物体的初始位置在(100,100)
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    #　print time_passed, time_passed_seconds
    
    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size()) / 2.0
    # 一下帧物体的目标坐标：（鼠标的坐标位置）- （物体尺寸的一半）
    
    vector_to_mouse = Vector2.from_points(position, destination)
    # 鼠标在上一帧的位置到目标坐标的位移
    
    vector_to_mouse.normalize()
    #　位移单位化
    #print vector_to_mouse
    
    heading = heading + (vector_to_mouse * .6)
    # heading是物体的移动速率
    #print heading
    position += heading * time_passed_seconds
    # 更新物体的坐标；上一次的坐标位置加上单位时间内的位移
    print position
    
    pygame.display.update()