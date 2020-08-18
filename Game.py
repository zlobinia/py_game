import sys

import pygame
from pygame.sprite import Group

from Bullet import Bullet, BulletSettings
from settings import GameSettings
from unit import Unit


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    settings = GameSettings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.game_name)
    # Start the main loop for the game.
    unit = Unit(screen)
    bullets = Group()
    while True:
        # Watch for keyboard and mouse events.
        checkEvents(unit, screen, bullets)
        unit.update()
        update_bullets(bullets)
        # Make the most recently drawn screen visible.\
        updateScreen(screen, settings, unit, bullets)


def update_bullets(bullets):
    for bullet in bullets.copy():
        if (bullet.rect.bottom <= 0):
            bullets.remove(bullet)
        elif bullet.range <= 0:
            bullets.remove(bullet)

    bullets.update()


def checkEvents(unit, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, unit, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, unit)


def check_keyup_events(event, unit):
    if event.key == pygame.K_w:
        unit.sm_up = False
    elif event.key == pygame.K_s:
        unit.sm_down = False
    elif event.key == pygame.K_a:
        unit.sm_left = False
    elif event.key == pygame.K_d:
        unit.sm_right = False


def check_keydown_events(event, unit, screen, bullets):
    if event.key == pygame.K_w:
        unit.sm_up = True
    elif event.key == pygame.K_s:
        unit.sm_down = True
    elif event.key == pygame.K_a:
        unit.sm_left = True
    elif event.key == pygame.K_d:
        unit.sm_right = True
    elif event.key == pygame.K_SPACE:
        bullets.add(Bullet(BulletSettings(), screen, unit))


def updateScreen(screen, settings, unit, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    unit.blitme()
    pygame.display.flip()


run_game()
