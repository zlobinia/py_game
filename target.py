import random
import pygame
from pygame.sprite import Sprite

class TargetSettings():
    def __init__(self):
        self.energy = 100

class Target(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images/target.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        x_d = random.randint(-2,2)
        y_d = random.randint(-2,2)
        self.x += x_d
        self.y += y_d
        rect = self.screen.get_rect()
        if self.x > rect.right:
            self.x = rect.left
        if self.x < rect.left:
            self.x = rect.right
        if self.y > rect.bottom:
            self.y = rect.top
        if self.y < rect.top:
            self.y = rect.bottom

        self.rect.x = self.x
        self.rect.y = self.y

