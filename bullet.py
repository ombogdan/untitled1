import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):#Створює обєкт пулі
    def __init__(self, ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Pozition bullet
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self): #переміщує пулю вверх по екрану
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self): #Виводить пулю на екран
        pygame.draw.rect(self.screen, self.color, self.rect)
