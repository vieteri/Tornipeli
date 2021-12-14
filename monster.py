import pygame


class Monster():
    def __init__(self, hp, speed, money, size):
    #    self.picture = 0 #import picture
        self.pos = (0,175)
        self.rect =  pygame.Rect(self.pos[0],self.pos[1],size,size)
        self.maxhp = hp
        self.hp = hp #dies
        self.speed = speed#proportional to time. time to be implemented
        self.money = money
        
def monstermove(monsterlist, tiles, gui):
    up = 1
    right = 2
    down = 3
    for monster in monsterlist:
        dir = right
        for i in range(3,7):
            if monster.rect.colliderect(tiles[8][i].rect):
                dir = down
            if monster.rect.colliderect(tiles[8][7]):
                dir = right
        for i in range(2,7):
            if monster.rect.colliderect(tiles[16][i]):
                dir=up
        if monster.rect.colliderect(tiles[16][2]) and not monster.rect.colliderect(tiles[16][3]):
            dir = right
        if dir==right:
            monster.rect.move_ip(2,0)
        elif dir==down:
            monster.rect.move_ip(0,2)
        else:
            monster.rect.move_ip(0,-2)
        if monster.rect.colliderect(tiles[24][2].rect):
            gui.life-=1
            monsterlist.remove(monster)
def die(monsterlist, gui):
    for enemy in monsterlist:
        if enemy.hp<=0:
            gui.money+=enemy.money
            monsterlist.remove(enemy)
            
            
def draw_monsters(monsterlist, screen):
    for mon in monsterlist:
        health_bar_width = 30
        pers = int(max(min(mon.hp / float(mon.maxhp) * health_bar_width, health_bar_width), 0))
        rekt = pygame.Rect(mon.rect.left, mon.rect.top-5,pers,5)
        
        pygame.draw.rect(screen, (0,0,255), rekt)
        pygame.draw.rect(screen, (255,0,0),mon.rect)