import pygame
from pygame import Surface,surfarray
from pyevent import Events

class Canvas(Surface,Events):
    def __init__(self, master = None, surface = None, **surf_kwargs):     
        self.children = []

        if not surface:
            self._build_surface(**surf_kwargs)
        else:
            surf_rect = surface.get_rect()
            Surface.__init__(surf_rect.size, masks = pygame.mask.from_surface(surface))
            array = surfarray.array2d(surface)
            surfarray.blit_array(self, array)

        if not master:
            self.master = pygame.display.get_surface()
        else:
            self.master = master

        Events.__init__(self)

    def _build_surface(self, width, height):
        Surface.__init__(self,(width,height))

    def add_child(self, pygame_surface):
        if isinstance(pygame_surface,Canvas):
            self.children.append(pygame_surface)
        else:
            raise TypeError("pygame_surface:{} is not of type Pygame_surface".
                            format(type(Pygame_canvas.__class__.__name__)))

    def pack(self, posX, posY):
        self.posX, self.posY = posX, posY
        if isinstance(self.master, Canvas):
            self.master.add_child(self)

    def update(self, events):
        if self.has_change():
            self.draw()
        
        self.process_events(events)
        self.update_children()

    def update_children():
        for child in self.children:
            child.update(self.events)

    def draw(self):
        self.master.blit(self, (self.posX,self.posY))

    def has_change(self):
        return True

        

