import pygame


class UnitGenome():

    def __init__(self):
        self.speed_factor = 0.5


class Unit():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/unit.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.sm_up = False
        self.sm_down = False
        self.sm_left = False
        self.sm_right = False

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.genome = UnitGenome()

    def update(self):
        if self.sm_up:
            self.centery -= self.genome.speed_factor
        if self.sm_down:
            self.centery += self.genome.speed_factor
        if self.sm_left:
            self.centerx -= self.genome.speed_factor
        if self.sm_right:
            self.centerx += self.genome.speed_factor
        if self.centerx > self.screen_rect.right:
            self.centerx = self.screen_rect.left
        if self.centerx < self.screen_rect.left:
            self.centerx = self.screen_rect.right
        if self.centery > self.screen_rect.bottom:
            self.centery = self.screen_rect.top
        if self.centery < self.screen_rect.top:
            self.centery = self.screen_rect.bottom

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
