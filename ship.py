import pygame
class Ship():#Клас для корабля
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings= ai_settings
        self.image = pygame.image.load('images/ship1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx  = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
    def update(self):#не дозволяє картінці рухатись зе межі вікна
        if self.moving_right and self.rect.right < self.screen_rect.right+1:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
    def blitme(self):#виводить корабель на екран
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx

