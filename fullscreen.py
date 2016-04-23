#!/usr/bin/env pythn
#coding:utf-8

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    if event.type == KEYDOWN:
        # 全屏模式的快键键设定为f(无视大小写）
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
            else: 
                screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    
    screen.blit(background, (0, 0))
    pygame.display.update()