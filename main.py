#import pygame
import pygame
from tile import *
from map import Map
from gui import Gui
from tower import *
#from tower import Tower
from monster import *
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 380
GREY = (192,192,192)
BROWN = (131,92,59)

def read_conf(file): #read conffile and parse line by line
    conffile = open(file, 'r')

    for line in conffile:
        currentline = line.split(";")
        if currentline[0] == "Tiles": #create tiles according to conf file
            tiles = create_tiles(int(currentline[1]),int(currentline[2]),int(currentline[3]),int(currentline[4]))
            for i in range(0,7):
                tiles[i][3].color = BROWN
                tiles[i][3].type = 3 #the road monsters go
            for i in range(3,6):
                tiles[7][i].color = BROWN
                tiles[7][i].type = 3
            for i in range(7,15):
                tiles[i][6].color = BROWN
                tiles[i][6].type = 3
            for i in range(2,7):
                tiles[15][i].color = BROWN
                tiles[15][i].type = 3
            for i in range(15,24):
                tiles[i][2].color = BROWN
                tiles[i][2].type = 3
            tiles[24][2].color = (66,66,66) #The goal monsters like to reach
            tiles[24][2].type = 4
        elif currentline[0] == "Dimensions":
            map = Map(int(currentline[1]),int(currentline[2]))
    yield map
    yield tiles

def main():
    mon = Monster(100,1,20,30)
    second = round((pygame.time.get_ticks())/1000)
    gui = Gui() #initialize gui
    time = 0
    clock = pygame.time.Clock()
    enemylist = []
    towerlist = []
    map = Map(SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.set_caption("Tower defense")
    tiles = 0
    pygame.font.init()   
    font = pygame.font.SysFont("comicsans.ttf", 30)
    label = font.render("Vietin eeppinen tornipuolustuspeli",1,(0,0,0))
    

    running = 1
    status=0
    start = pygame.image.load("menu.png")
    image = pygame.image.load("start.png")
    image_rect = image.get_rect()
    
    map.screen.blit(start, (0,0))
    map.screen.blit(image, (230,300))
    map.screen.blit(label, (130,50))
    buy = 0
    while running: 
       
        
        if gui.life<=0:
             return 0
        #running = map.handler(map, pygame.event.poll())
        event = pygame.event.poll()
        sec2 = round((pygame.time.get_ticks()-time)/1000)
        if event.type==pygame.QUIT:
            return 0
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            if status==0 and mousex>=230 and mousey>=300 and mousex < 230+192 and mousey<=350:              
                (map, tiles) = read_conf("tiles.conf")
                #Tehdään alue, missä hrviöt voivat liikkua
                #Muutetaan tiiliskivien tyyppi
                time = pygame.time.get_ticks()
                status=1
            elif status == 1 and buy.collidepoint(mousex,mousey): #Checks if monster collides to it's goal
                status = 2
            elif status == 2:
                for i in range(0,len(tiles)):
                    for j in range(0,len(tiles[0])):
                        if tiles[i][j].rect.collidepoint(mousex,mousey) and tiles[i][j].type==1 and gui.money>0:
                            tiles[i][j].type=2
                            tiles[i][j].color = (0,0,0)
                            towerlist.append(Tower(i,j,1,1,100))
                            gui.money-=20
                            status = 1
        if sec2-second==3 and status>0:
            enemylist.append(Monster(100*(1+(0.01*sec2)),1,20,30))
            second=sec2

            #if status==1:
        #            print("Collides")
            #    print(tiles[24][2].Rect)
            
        if status>0:
            monstermove(enemylist, tiles, gui) #moves every monster
            map.screen.fill(GREY)
            map.draw_tiles(tiles, len(tiles[0]),len(tiles))
            pygame.draw.line(map.screen, (0,0,0), (0,465), (1280,465), 3)
            buy = gui.draw_gui(map.screen,time) #draw gui
            draw_monsters(enemylist, map.screen) #draws the monsters
            for tower in towerlist: #Every tower shoots
                tower.shoot(map.screen, enemylist, tiles)
            die(enemylist, gui) #checks if any monster dies
        #    pygame.draw.rect(map.screen, (255,0,0),mon.rect)
        clock.tick(60) #frame rate
        pygame.display.flip()
        
    
main()
  