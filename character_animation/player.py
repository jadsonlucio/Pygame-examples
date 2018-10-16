import pygame
from pysprite import Sprite

class Sprite_animation():
    def __init__(self, img_url, rows, cols, speed, playing = False):
        self.image = pygame.image.load(img_url)
        self.image_rect = self.image.get_rect()
        self.rows = rows 
        self.cols = cols 
        self.speed = speed
        self.playing = playing
        self.section = 0

        self.sprite_count = 0
        self.sprite_width = self.image_rect.width/self.cols
        self.sprite_height = self.image_rect.height/self.rows


    @property
    def sprite_size(self):
        return self.sprite_width,self.sprite_height

    @property
    def current_surface(self):
        posX = self.sprite_count * self.sprite_width
        posY = self.section * self.sprite_width
        return self.image.subsurface((posX, posY, self.sprite_width, self.sprite_width))
    
    def start(self):
        pass
    
    def stop(self):
        pass

    def play(self):
        self.sprite_count += 1
        self.sprite_count %= self.cols

class Character(Sprite):
    def __init__(self, display, img_url, rows, cols):
        self.sprite_animation = Sprite_animation(img_url, rows, cols, 0.5)
        width, height = self.sprite_animation.sprite_size
        super().__init__(display, width = width, height = height)
        self.surface = self.sprite_animation.current_surface

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.sprite_animation.section = 0
            elif event.key == pygame.K_DOWN:
                self.sprite_animation.section = 2
            elif event.key == pygame.K_LEFT:
                self.sprite_animation.section = 1
            elif event.key == pygame.K_RIGHT:
                self.sprite_animation.section = 3

 

    