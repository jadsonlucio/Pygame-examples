from pysurface import Pygame_canvas

class Pygame_widget(Pygame_canvas):
    def __init__(master, name, *args, **kwargs):

        self.name = name
        super().__init__(master = master, *args, **kwargs)

    def build(self):
        pass