import pygame
from settings import Settings
from ship import Ship
from game_status import GameStatus

import game_functions as gf
from pygame.sprite import Group
def run_game(): #створення вікна
    pygame.init()
    ai_settings = Settings()
    bullets = Group()
    aliens = Group()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)
    #Екземпляр для зберігання ігрової статистики
    status = GameStatus(ai_settings)
    #Створення корабля ы групи
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
           gf.check_events(ai_settings, screen, ship, bullets)
           ship.update()
           gf.update_bullets(ai_settings, screen,ship, aliens, bullets)
           gf.update_aliens(ai_settings, status, screen, ship, aliens, bullets)
           gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)
run_game()