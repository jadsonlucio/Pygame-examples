from random import choice
import pygame
import numpy as np
from pygame.locals import *

from world import RPG_map
from pysurface import Pygame_canvas

is_valid = lambda new_pos, matrix_size :True if new_pos >= 0 and new_pos < matrix_size else False
is_valid_pos = lambda posX,posY,matrix_shape : True if is_valid(posX, matrix_shape[0]) and is_valid(posY, matrix_shape[1]) else False

def set_block_type(posX, posY, matrix):
    dict_count = {
        "grass"  : 1,
        "water"  : 1
    }

    jump_array = [-1,1,0]
    for jump_x in jump_array:
        for jump_y in jump_array:
            new_posX = posX + jump_x
            new_posY = posY + jump_y
            if is_valid_pos(new_posX, new_posY, matrix.shape):
                block_type = matrix[new_posX][new_posY]
                if block_type:
                    dict_count[block_type] = dict_count[block_type] + 1
    
    sum_houses = sum(dict_count.values())
    p = [cont/sum_houses for cont in dict_count.values()]
    matrix[posX][posY] = np.random.choice(["grass","water"], p = p)


def set_matrix(posX, posY, matrix):
    jump_array = [-1,1,0]
    for jump_x in jump_array:
        for jump_y in jump_array:
            new_posX = posX + jump_x
            new_posY = posY + jump_y
            matrix_shape = matrix.shape
            if is_valid_pos(new_posX, new_posY, matrix_shape):
                if not matrix[new_posX][new_posY]:
                    set_block_type(new_posX, new_posY, matrix)
                    set_matrix(new_posX, new_posY, matrix)

def build_environment_matrix(shape, objects_graph):
    matrix_objects = np.empty(shape, dtype = object)
    set_matrix(0, 0, matrix_objects)
    print(matrix_objects)

    return matrix_objects

def build_rpg_map(display_surface):
    grass_object = pygame.image.load("grass.jpg")
    ground_object = pygame.image.load("ground.jpg")
    water_object = pygame.image.load("water.png")
    objects_dict = {
        "grass": grass_object,
        "ground": ground_object,
        "water": water_object,
    }

    environment_matrix = build_environment_matrix((6,8), None) 
    return RPG_map((800,600), display_surface, (100,100), environment_matrix, objects_dict)

class App():
    def __init__(self, name, width, height, debug = False):
        self._running = False
        self._on_init(width, height)

        self.map = build_rpg_map(self._display)
        self.map.pack(0,0)
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