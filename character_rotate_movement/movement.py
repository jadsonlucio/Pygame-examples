import math

import pygame


class Character:
    def __init__(self, master, pos_x, pos_y, width=32, height=32):

        self.image = pygame.Surface((width, height))
        self.original_image = self.image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.master = master
        self.angle = self.set_angle()
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        self.velocidade = 10

    def update(self):
        self.set_angle()
        # self.rotate()
        self.draw()

    def draw(self):
        self.master.blit(self.font.render(str(round(self.angle, 2)), False, (0, 0, 0)), (0, 0))
        self.master.blit(self.image, (self.pos_x, self.pos_y))
        pygame.draw.line(self.master, (255, 255, 255), self.get_center_pos(), self.mouse_pos)

    def get_pos(self):
        return (self.pos_x, self.pos_y)

    def get_center_pos(self):
        return (self.pos_x + (self.width / 2), self.pos_y + (self.height / 2))

    def set_angle(self):
        self.mouse_pos = pygame.mouse.get_pos()
        pos = self.get_center_pos()
        dx = self.mouse_pos[0] - pos[0]
        dy = self.mouse_pos[1] - pos[1]
        d = math.atan2(-dy, dx)
        d %= 2 * math.pi

        self.angle = math.degrees(d)

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.pos_x += math.cos(self.angle * math.pi / 180) * self.velocidade
                self.pos_y -= math.sin(self.angle * math.pi / 180) * self.velocidade
            if event.key == pygame.K_s:
                self.pos_x -= math.cos(self.angle * math.pi / 180) * self.velocidade
                self.pos_y += math.sin(self.angle * math.pi / 180) * self.velocidade


pygame.init()
pygame.font.init()

size = (640, 480)

screen = pygame.display.set_mode(size)
screen.fill((0, 145, 0))

clock = pygame.time.Clock()
FPS = 30

player = Character(screen, 100, 100)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.move(event)

    screen.fill((0, 145, 0))
    player.update()
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
