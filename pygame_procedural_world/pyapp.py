from random import choice
import pygame
import numpy as np
from pygame.locals import *

from world import RPG_map
from map_generation import generate_map
from pysurface import Pygame_canvas

is_valid = lambda new_pos, matrix_size :True if new_pos >= 0 and new_pos < matrix_size else False
is_valid_pos = lambda posX,posY,matrix_shape : True if is_valid(posX, matrix_shape[0]) and is_valid(posY, matrix_shape[1]) else False



def build_environment_matrix(shape, objects_graph):
    matrix_objects = np.empty(shape, dtype = object)
    matrix = generate_map(shape, 600, 20)

    for cont in range(len(matrix)):
        for cont2 in range(len(matrix[cont])):
            if matrix[cont][cont2] == 0:
                matrix[cont][cont2] = "ground"
            elif matrix[cont][cont2] == 1:
                matrix[cont][cont2] = "grass"

    return matrix

def build_rpg_map(display_surface):
    grass_object = pygame.image.load("grass.jpg")
    ground_object = pygame.image.load("ground.jpg")
    water_object = pygame.image.load("water.png")
    objects_dict = {
        "grass": grass_object,
        "ground": ground_object,
        "water": water_object,
    }

    environment_matrix = build_environment_matrix((100,100), None) 
    return RPG_map((100*100,100*100), display_surface, (100,100), environment_matrix, objects_dict)

class App():
    def __init__(self, name, width, height, debug = False):
        self._running = False
        self._on_init(width, height)

        self.map = build_rpg_map(self._display)
        self.map.pack(-100,-100)
        self.map.build()


    def run(self):
        self._running = True

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self._display.surface.fill((255,255,0))
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def _on_init(self, width, height, **app_config):
        pygame.init()
        surface = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display = Pygame_canvas(surface = surface)
        Pygame_canvas.TOP_LEVEL_DISPLAY = self._display

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.map.camera.move(-100,0)
            elif event.key == pygame.K_DOWN:
                self.map.camera.move(100,0)
            elif event.key == pygame.K_LEFT:
                self.map.camera.move(0, 100)
            elif event.key == pygame.K_RIGHT:
                self.map.camera.move(0, -100)

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