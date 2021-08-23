'''
Created on 6.3.2017

@author: viet
'''
import pygame
import math

class Tower():
    def __init__(self, y, x, damage, multiplier, range):
        #self.img = pygame.paska
        self.y = y
        self.x = x
        self.dps = damage
        self.multiplier = multiplier
        self.range = range
        
    def shoot(self, screen, enemylist, tiles):
        for enemy in enemylist:
            dist = math.hypot(tiles[self.y][self.x].rect.center[0]-enemy.rect.center[0], tiles[self.y][self.x].rect.center[1]-enemy.rect.center[1])
            if dist<=self.range:
                enemy.hp -= self.dps
                pygame.draw.line(screen, (0,255,0), tiles[self.y][self.x].rect.center, enemy.rect.center,2)
                return
                    