import pygame
from map import Map
from tower import Tower
TOWERS = Tower(55,55,2,1,1)
class Gui():
    def __init__(self):
        self.life = 20
        self.money = 200
    
    def timer(self, time):
        second = round((pygame.time.get_ticks()-time)/1000)
        minute = 0
        hour = 0
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        return str(hour) + ":" + str(minute) + ":" + str(second)
    
    
    def draw_gui(self, screen,time):
        pygame.font.init()   
        font = pygame.font.SysFont("comicsans.ttf", 100)
        lifelife = "Life: " + str(self.life)
        lifelabel = font.render(lifelife, 1, (255,50,50))
        towerlabel = font.render("Tower", 1, (0,0,0))
        moneylabel = font.render("Gold",1,(255,215,0))
        moneylabel2 = font.render(str(self.money), 1, (255,215,0))
        time = font.render(self.timer(time), 1, (255,255,255))
        screen.blit(towerlabel, (700,500))
        screen.blit(lifelabel, (1000, 500))
        screen.blit(moneylabel, (50,500))
        screen.blit(moneylabel2, (70, 580))
        screen.blit(time, (250, 500))
        towerrect = pygame.Rect(750,580,100,100)
        pygame.draw.rect(screen, (0,0,0), towerrect)
        return towerrect
    