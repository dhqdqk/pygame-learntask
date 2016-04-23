#!/usr/bin/env pythn
#coding:utf-8
'''
捕捉鼠标移动和点击事件，并输出每次的事件的文本信息
'''
import pygame
from pygame.locals import *
from sys import exit

pygame.init()   # 初始化硬件
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
print font_height

event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-SCREEN_SIZE[1] / font_height:]
    # 此切片操作保证event_text中只保留一个屏幕的文字
    
    if event.type == QUIT:
        exit()
    screen.fill((255, 255, 255))
    
    y = SCREEN_SIZE[1] - font_height    # 合适的起笔位置
    print event_text
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 255, 0)), (0, y))
        y -= font_height    # 把笔提一行
    pygame.display.update()