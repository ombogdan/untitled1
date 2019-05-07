class GameStatus(): #Клас для відсліжування статистики
    def __init__(self, ai_settings): #ініціалізує статистику
        self.ai_settings = ai_settings
        self.reset_status()
    def reset_status(self): #ініціалізує статистику яка змінюється в ході гри
        self.ship_left = self.ai_settings.ship_limit

