import pygame
from pygame.locals import *

class Obj():
    def __init__(self, posX = 0, posY = 0, width = 100, height = 100):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
    
    def move(self, x, y):
        self.posX = self.posX + x
        self.posY = self.posY + y

    @property
    def pos(self):
        return (self.posX,self.posY)
    
    @property
    def rect(self):
        return (self.posX, self.posY, self.width, self.height)
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill((0,0,0))

        self.light = 
        self.grid = pygame.Surface((640,400))
        self.mask = pygame.Surface((640, 400)).convert_alpha()

        self.obj = Obj()

        for cont in range(0,640,40):
            for cont2 in range(0,400,40):
                pygame.draw.rect(self.grid,(0,255,0),(cont,cont2, 40, 40), 1)

        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.obj.move(0, -5)
            elif event.key == pygame.K_DOWN:
                self.obj.move(0, 5)
            elif event.key == pygame.K_LEFT:
                self.obj.move(-5, 0)
            elif event.key == pygame.K_RIGHT:
                self.obj.move(5, 0)

    def on_loop(self):
        pass

    def on_render(self):
        self.mask.fill((0,0,0,255))
        pygame.draw.rect(self.mask,(0,0,0,128), self.obj.rect)

        self._display_surf.blit(self.grid,(0,0))
        self._display_surf.blit(self.mask,(0,0))

        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()