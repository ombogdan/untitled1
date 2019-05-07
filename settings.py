class Settings():
    #Клас для зберігання налаштувань в грі
    def __init__(self):
        self.screen_width = 1030
        self.screen_height = 700
        self.bg_color = (255,255,255)
        self.ship_speed_factor = 4.5
        self.bullet_speed_factor = 1
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullets_allowed = 10
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 20
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.ship_limit = 2