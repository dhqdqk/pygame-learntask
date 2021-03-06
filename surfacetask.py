#!/usr/bin/evn python
#coding:utf-8

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
SCREEN_SIZE = (640, 480)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
#screen.set_clip(0, 400, 200, 600)
#screen.set_clip(0, 0, 800, 60)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.lock()
    for i in xrange(100):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos, rand_col)
    screen.unlock()
    pygame.display.update()
    