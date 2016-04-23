#!/usr/bin/env python 
#coding:utf-8
import pygame
from gameobjects.vector2 import Vector2
from pip._vendor.html5lib.treewalkers._base import ENTITY

class GameEntity(object):
    '''
    游戏元素的基类，每个游戏元素有自己的位置，目标，速度，和图形。
    同时还有一个自己享用的状态机（至少要有进入和退出两种状态）；
    以及一个和外界的关联的关系对象。
    '''
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.0
        self.brain = StateMachine()
        self.id = 0
    
    def render(self, surface):
        '游戏对象绘制自身'
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x-w/2, y-h/2))
    
    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            vec_to_desination = self.destination - self.location
            distance_to_destination = vec_to_desination.get_length()
            heading = vec_to_desination.get_normalized()
            travel_distance = min(distance_to_destination, time_passed*self.speed)
            self.location += travel_distance * heading


class World(object):
    'Wordl用描述世界内的游戏元素；所有对象名称和ID，位置，背景图片；'
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255,255,255))
        pygame.draw.cirle(self.background, (200,255,200),NEST_POSITION, int(NEST_SIZE))
    
    def add_entity(self, entity):
        '添加一个游戏实体'
        'add a new game entity'
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1
        
    def remove_entity(self, entity):
        del self.entities[entity.id]
    
    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
    
    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.itervalues():
            entity.process(time_passed_seconds)
    
    def render(self, surface):
        surface.blit(self.background, (0,0))
        for entity in self.entities.values():
            entity.render(surface)
    
    def get_close_entity(self, name, location, wrange=100.0):
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < wrange:
                    return entity
        return None


class Ant(GameEntity):
    def __init__(self, world, image):
        super(Ant, self).__init(world, "ant", image)
        exploring_state = AntStateExploring(self)
        seeking_state = AntStateSeeking(self)
        delivering_state = AntStateDelivering(self)
        hunting_state = AntStateHunting(self)
        self.brain.add_state(exploring_state)
        self.brain.add_state(seeking_state)
        self.brain.add_state(delivering_state)
        self.brain.add_state(hunting_state)
    
    def carry(self, image):
        self.carry_image = image
    
    def drop(self, surface):
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x-w/2,y-h/2))
            self.carry_image = None
    
    def render(self, surface):
        super(Ant, self).render(surface)
        if self.carry_image:
            x, y = self.location
            w, h = self.carry_image.get_size()
            surface.blit(self.carry_image, (x-w/2,y-h/2))


class State(object):
    def __init__(self, name):
        self.name = name
    
    def do_action(self):
        pass
    
    def check_conditions(self):
        pass
    
    def entry_actions(self):
        pass
    
    def exit_actions(self):
        pass   