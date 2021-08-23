import pygame
from map import Map
def main():
    clock = pygame.time.Clock()
    clock.tick(20)
    map = Map(1280, 720)
    map.screen.fill((255,50,50))
    rekt = pygame.Rect(20,20,30,30)
    x=1
    y=1
    while True:
        event = pygame.event.poll()
        map.screen.fill((255,50,50))
        if event.type==pygame.QUIT:
            return 0
        rekt.move_ip(x,y)
        pygame.draw.rect(map.screen, (0,0,0),rekt)
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            if rekt.collidepoint(mousex, mousey):
                print(type(rekt))
        pygame.display.update()
        """
        Implementoi liikkuvat hirviöt
        Luo hirviö
        Health bar
        Tornit
        Liikkumisreitti
        fps?
        """
main()

