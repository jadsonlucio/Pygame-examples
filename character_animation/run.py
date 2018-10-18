import numpy as np
import pygame
from pygame.locals import *
from random import choice

from world import MazeMap,Camera
from map_generation import generate_map

from player import Character
from pysurface import Canvas



def set_key_pressed_events():
    keys = pygame.key.get_pressed()
    for cont in range(len(keys)):
        if keys[cont]:
            pygame.event.post(pygame.event.Event(31, key=cont))

def build_environment_matrix(shape, objects_graph):
    matrix_objects = np.empty(shape, dtype = object)
    matrix = generate_map(shape, 400, 20)

    for cont in range(len(matrix)):
        for cont2 in range(len(matrix[cont])):
            if matrix[cont][cont2] == 0:
                matrix[cont][cont2] = "ground"
            elif matrix[cont][cont2] == 1:
                matrix[cont][cont2] = "grass"

    print(matrix)
    return matrix

def build_maze_map(display_surface):
    grass_object = pygame.image.load("images/grass.jpg")
    ground_object = pygame.image.load("images/ground.jpg")
    water_object = pygame.image.load("images/water.png")
    objects_dict = {
        "grass": grass_object,
        "ground": ground_object,
        "water": water_object,
    }

    environment_matrix = build_environment_matrix((100,100), None) 
    return MazeMap((100*100,100*100), display_surface, (100,100), environment_matrix, objects_dict)

class App():
    def __init__(self, name, fps, width, height, debug = False):
        self._running = False
        self.screen_width = width
        self.screen_height = height

        self._display = None
        self.player = None
        self.map = None

        self.time_event = pygame.event.Event(30, time = 0, fps = fps, count_fps = 0)

    def add_events_queue(self):
        pygame.event.post(self.time_event)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            set_key_pressed_events()
            self.add_events_queue()
            for event in pygame.event.get():
                self.on_event(event)
            self._display.fill((0,145,0))
            self.on_loop()
            self.on_render()
            self.tick()

        self.on_cleanup()

    def on_init(self):
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)

        self._display = Canvas(width = self.screen_width, height = self.screen_height)
        self._display.pack(0, 0)

        self.world = build_maze_map(self._display)
        self.world.build()
        self.world.pack(0,0)
        
        self.player = Character(self._display,"player.png",4, 9)
        self.player.pack(8*64,7*64)
        
        self.camera = Camera(self.player)
        self.world.camera = self.camera

        self.screen = pygame.display.get_surface()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        else:
            self._display.event_call(event)

    def on_loop(self):
        self.world.update_map_position(self.camera)
        

    def on_render(self):
        self._display.update()
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()

    
    def tick(self):
        time_event = self.time_event
        time_event.count_fps += 1
        if time_event.count_fps % time_event.fps == 0:
            time_event.time += 1
            time_event.count_fps = 0
        
        pygame.time.Clock().tick(time_event.fps)

    
    
if __name__ == "__main__":
    app = App("teste", 30,832, 704)
    app.on_execute()