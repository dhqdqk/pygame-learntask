#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
font = pygame.font.SysFont("simsun", 40)
text_surface = font.render(u"haobo", True, (0, 0, 225))

x = 0
y = (480 - text_surface.get_height()) / 2

background = pygame.image.load("sushiplate.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print "now quit pygame"
            exit()
    
    screen.blit(background, (0, 0))
    
    x -= 0.2  # 文字滚动的速率
    # 初始位置在(0,0)；字向左移
    if x < -text_surface.get_width():
        print text_surface.get_width()
        x = 640 - text_surface.get_width()
    
    print x
    screen.blit(text_surface, (x, y))
    pygame.display.update()
    