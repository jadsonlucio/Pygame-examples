import os

import pygame

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        for i in range(1,7):
            self.images.append(self.load_image('img/{0}.png'.format(i)))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def load_image(self, img):
        return pygame.image.load(img)

pygame.init()

screen = pygame.display.set_mode((600,400))

clock = pygame.time.Clock()
fps=1

group = pygame.sprite.Group(CustomSprite())

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill((0,0,0))
    group.update()
    group.draw(screen)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()