from pygame import Surface

class Pygame_canvas():
    TOP_LEVEL_DISPLAY = None

    def __init__(self, master = None, surface = None, **surf_kwargs):     
        self.children = []

        if not surface:
            self._build_surface(**surf_kwargs)
        else:
            self.surface = surface

        if not master:
            self.master = self.TOP_LEVEL_DISPLAY
        else:
            self.master = master


    def _build_surface(self, width, height):
        self.surface = Surface((width,height))

    def add_child(self, pygame_surface):
        if isinstance(pygame_surface,Pygame_canvas):
            self.children.append(pygame_surface)
        else:
            raise TypeError("pygame_surface:{} is not of type Pygame_surface".
                            format(type(Pygame_canvas.__class__.__name__)))

    def pack(self, posX, posY):
        self.posX, self.posY = posX, posY
        if self.master:
            self.master.add_child(self)

    def update(self):
        if self.has_change():
            self.draw()
        
        for child in self.children:
            child.update()

    def draw(self):
        if self.master:
            self.master.surface.blit(self.surface, (self.posX,self.posY))

    def has_change(self):
        return True
