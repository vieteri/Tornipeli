import pygame

GREY = (192,192,192)
class Map():
    def __init__(self, width, height): #Create map
        self.screen = pygame.display.set_mode([width, height])
        self.screen.fill(GREY)

        

    def menu(self, left, top, size): #To be implemented?
        pass
    
    def draw_tiles(self, tiles, column, row): #draws every tile to the window
        for j in range(0,column):
            for i in range(0,row):
                pygame.draw.rect(self.screen, tiles[i][j].color, tiles[i][j])