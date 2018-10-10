import pygame
from pygame.locals import *
from world import RPG_map

def build_environment_matriz(size, objects_graph):
    return [["grass","ground"]]

def build_rpg_map(display_surface):
    grass_object = pygame.image.load("grass.jpg")
    ground_object = pygame.image.load("ground.jpg")
    objects_dict = {
        "grass": grass_object,
        "ground": ground_object,
    }

    environment_matriz = build_environment_matriz((8,6), None) 
    return RPG_map((800,600), display_surface, (100,100), environment_matriz, objects_dict)
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self.rpg_world = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.map = build_rpg_map(self._display_surf)
        self.map.pack(0,0)
        self.map.build()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.flip()

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