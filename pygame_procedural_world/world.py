from pysurface import Pygame_canvas

class Camera():
    def __init__(self, map, posX, posY):
        self.map = map
        self.posX, self.posY = posX,posY
    
    def move(self, x, y):
        self.posX = self.posX + x
        self.posY = self.posY + y
        self.map.posX = self.posX
        self.map.posY = self.posY
    
class RPG_map(Pygame_canvas):
    def __init__(self, map_size, display_canvas, block_size, block_matriz, objects_dict):
        self.camera = Camera(self, 0, 0)
        self.display_canvas = display_canvas
        self.block_size = block_size
        self.block_matriz = block_matriz
        self._objects_dict = objects_dict

        super().__init__(width = map_size[0],height = map_size[1], master = display_canvas)

    def build(self):
        for row in range(len(self.block_matriz)):
            for col in range(len(self.block_matriz[row])):
                object_name = self.block_matriz[row][col]
                object_surface = self._objects_dict[object_name]
                object_pos = self.block_size[0]*col, self.block_size[1]*row
                self.surface.blit(object_surface, object_pos)

