#!/usr/bin/env pythn
#coding:utf-8

import pygame
from pygame.locals import *
from sys import exit


background_image_filename = 'sushiplate.jpg'
SCREEN_SIZE = (640, 480)
fontfile = 'simsun'

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()
my_font = pygame.font.SysFont(fontfile, 16) # 创建字体对象
text_surface = my_font.render(u"浩博", True, (0, 0 , 255))

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Widow size:" + str(event.size))
    
    screen_width, screen_height = SCREEN_SIZE
    # 重新绘制背景图；以背景图的长宽为步长,重复背景图
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    
    pygame.display.update()