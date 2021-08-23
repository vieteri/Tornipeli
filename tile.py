import pygame
from enum import Enum

    
    
class Tile:
    def __init__(self, left, top, width, height, type=1): #type=1 by default
        self.rect = pygame.Rect(left, top, width, height)
        self.left = left
        self.top = top
        self.type = type # 1=free 2=tower 3=road 4=goal
        self.width = width
        self.height = height
        self.color = (255,255,255)
        
def create_tiles(y,x, width, height): #Create 2-D array
    tiles = []
    lst = []
    for row in range(0,y):
        for column in range(0,x):
            tmp = Tile(52*row+1,52*column+1, 50, 50, 1)
            lst.append(tmp)
        tiles.append(lst)
        lst=[]
    return tiles


