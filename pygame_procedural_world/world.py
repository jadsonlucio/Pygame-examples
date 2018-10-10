from pysurface import Pygame_canvas

class Camera():
    def __init__(self, map, posX, posY):
        self.posX, self.posY = posX,posY
    
class RPG_map(Pygame_canvas):
    def __init__(self, map_size, display_canvas, block_size, block_matriz, objects_dict):

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

