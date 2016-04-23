#!/usr/bin/env python
#coding:utf-8

'''
用鼠标控制图像转向，方向键控制移动
'''
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

pygame.init()

background_image = 'sushiplate.jpg'
sprite_image = 'fugu.png'

screen = pygame.display.set_mode((640,480), 0, 32)

background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image).convert_alpha()

clock = pygame.time.Clock()
# pygame控制鼠标
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

sprite_pos = Vector2(200, 150)
sprite_speed = 300.0
sprite_rotation = 0.0
sprite_rotation_speed = 360.0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.display.quit()
                exit()
    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    
    rotation_direction = 0.0
    movement_direction = 0.0
    
    rotation_direction = pygame.mouse.get_rel()[0] / 5.0
    
    if pressed_keys[K_LEFT]:
        rotation_direction = +1.0
    
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.0
    if pressed_keys[K_UP] or pressed_mouse[0]:
        movement_direction = +1.0
    if pressed_keys[K_DOWN] or pressed_mouse[2]:
        movement_direction = -1.0
    
    screen.blit(background, (0,0))
    
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x-w/2, sprite_pos.y-h/2)
    screen.blit(rotated_sprite, sprite_draw_pos)
    
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
    
    heading_x = sin(sprite_rotation*pi/180.0)
    heading_y = cos(sprite_rotation*pi/180.0)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction
    
    sprite_pos += heading * sprite_speed * time_passed_seconds
    
    pygame.display.update()