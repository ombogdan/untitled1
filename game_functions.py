import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets): #Всі функції програми
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def update_screen(ai_settings, screen, status, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not status.game_active:
        play_button.draw_button()
        pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets): # всі пулі удаляються коли доходять до верху екрана
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
        collision = pygame.sprite.groupcollide(bullets,aliens, True, True)
        if  len(aliens) == 0:
            bullets.empty()
            create_fleet(ai_settings, screen,ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets): # не більше 10 пуль на екрані
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return  number_rows

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return  number_aliens_x
def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #Створення правого ряду прибульцыв
    for row_number in range(number_rows):
       for alien_number in range(number_aliens_x):
           create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):#Реагує на досягнення бокових країв екрану
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):#коли флот диходить до правої частини він опускається до низу і міняє напрямок руху
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, status, screen, ship, aliens, bullets):
    #Оброблює зіткнення корабля і прибульців
    #Зменшує кількість кораблів на 1
    if status.ship_left > 0:
      status.ship_left -= 1

    #Очищає весь екран від пуль і прибульців
      aliens.empty()
      bullets.empty()

    #Створюється новий флот і корабель стає в центр екрану
      create_fleet(ai_settings,screen, ship, aliens)
      ship.center_ship()

    #Пауза
      sleep(1)
    else: status.game_active = False

def check_aliens_bottom(ai_settings, status, screen, ship, aliens, bullets):
    #Перевіряє чи добралися прибульці до  краю екрасна
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, status, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, status, screen, ship, aliens, bullets):#перевіряє чи достиг флот краю екрана
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, status, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, status, screen, ship, aliens, bullets)