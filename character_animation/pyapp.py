from random import choice
import pygame
from pygame.locals import *

from player import Character
from pysurface import Canvas


class App():
    def __init__(self, name, width, height, debug = False):
        self._running = False
        self.on_init(width, height)

        self.player = Character(self._display,"C3ZwL.png",4, 9)
        self.player.pack()

    def run(self):
        self._running = True

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self._display.fill((255,255,0))
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def on_init(self, width, height):
        pygame.init()
        pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF)

        self._display = Canvas(width = width, height = height)
        self._display.pack(0, 0)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display.update()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
    
if __name__ == "__main__":
    app = App("teste", 800, 600)
    app.run()