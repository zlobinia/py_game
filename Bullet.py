import pygame
from pygame.sprite import Sprite


class BulletSettings():

    def __init__(self):
        self.speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 0


class Bullet(Sprite):

    def __init__(self, b_settings, screen, unit):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, b_settings.bullet_width, b_settings.bullet_height)
        self.rect.centerx = unit.rect.centerx
        self.rect.top = unit.rect.top

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = b_settings.bullet_color
        self.speed = b_settings.speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
