import pygame
from pysprite import Sprite

class Sprite_animation():
    def __init__(self, img_url, rows, cols, speed, playing = False):
        self.image = pygame.image.load(img_url).convert_alpha()
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
        posY = self.section * self.sprite_height
        return self.image.subsurface((posX, posY, self.sprite_width, self.sprite_height))
    
    def start(self):
        self.playing = True
    
    def stop(self):
        self.playing = False

    def play(self):
        self.sprite_count += 1
        self.sprite_count %= self.cols

class Character(Sprite):
    def __init__(self, display, img_url, rows, cols):
        self.sprite_animation = Sprite_animation(img_url, rows, cols, 0.5)
        width, height = self.sprite_animation.sprite_size
        super().__init__(display, width = width, height = height, flags=pygame.SRCALPHA, depth=32)
        self.velocity = 10
        self.set_colorkey((0,0,0))
        self.blit(self.sprite_animation.current_surface, (0,0))

    def key_press(self, event):
        self.sprite_animation.start()
        self.add_after_event(self.sprite_animation.speed, self.reload)
    
    def key_pressed(self, event):
        x, y = 0, 0

        if event.key == pygame.K_UP:
            self.sprite_animation.section = 0
            y = -self.velocity
        elif event.key == pygame.K_DOWN:
            self.sprite_animation.section = 2
            y = self.velocity
        elif event.key == pygame.K_LEFT:
            self.sprite_animation.section = 1
            x = -self.velocity
        elif event.key == pygame.K_RIGHT:
            self.sprite_animation.section = 3
            x = self.velocity

        
        self.move(x,y)

    def key_release(self, event):
        self.after_events = []
        self.sprite_animation.sprite_count = 0
        self.reload(None)
        self.sprite_animation.start()

    def reload(self, event):
        self.fill((0,0,0))
        self.blit(self.sprite_animation.current_surface, (0,0))
        self.sprite_animation.play()

    def update(self):
        self.master.blit(self, (368,268))