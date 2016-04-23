#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame.locals import *
from sys import exit
from random import randint
from math import pi

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()
        if event.type == KEYDOWN:
            points = []
            screen.fill((255, 255, 255))
        if event.type == MOUSEBUTTONDOWN:
            # 鼠标点一下随机画一个矩形（随机颜色）
            rc = (randint(0, 255), randint(0, 255), randint(0,255))
            rp = (randint(0,639), randint(0,479))
            rs = (639-randint(rp[0], 639), 479-randint(rp[1],479))            
            pygame.draw.rect(screen, rc, Rect(rp, rs))
            
            # 鼠标点一下随机画一个圆
            rc = (randint(0,255), randint(0,255), randint(0,255))
            rp = (randint(0,639), randint(0,479))
            rr = randint(1, 200)
            pygame.draw.circle(screen, rc, rp, rr)
            
            # 每次鼠标点下的坐标储存
            x, y = pygame.mouse.get_pos()
            points.append((x, y))
            
            # 根据鼠标点的位置画一段圆弧（其位置是同一个椭圆上）
            angle = (x/639.) * pi * 2.0
            pygame.draw.arc(screen, (0,0,0), (0,0,639,479), 0, angle, 3)
            
            # 以原点和鼠标点下的位置画一个椭圆
            pygame.draw.ellipse(screen, (0,255,0), (0,0,x,y))
            
            # 鼠标点下的位置，与原点及右下角连接两条线段
            pygame.draw.line(screen, (0,0,255), (0,0), (x,y))
            pygame.draw.line(screen, (255,255,0), (x,y), (640, 480))
            
            # 将每次鼠标点下的位置连接成线；每点一次全部重画，所以在图像的顶层
            if len(points) > 1:
                pygame.draw.lines(screen, (155, 155, 0), False, points, 2)
            
            # 给每次鼠标点下的位置用圆点标记；图像是置顶的
            for p in points:
                pygame.draw.circle(screen, (155,155,155), p, 10)
            
            
    pygame.display.update()