from random import randint

class Setting:
    '''Настройка симуляции'''
    def __init__(self):
        self.width = 11
        self.height = 5
        self.count_grass = 3
        self.count_rock = 4
        self.count_tree = 4
        self.count_herbivore = 10
        self.count_predator = 4
        self.speed_range = (1, 3)
        self.herb_health = (1, 70)
        self.pred_health = (3, 20)
        self.pred_strength = self.herb_health

    def determines_speed(self):
        return randint(*self.speed_range)

    def determines_herb_health(self):
        return randint(*self.herb_health)

    def determines_pred_health(self):
        return randint(*self.pred_health)

    determines_strength = determines_herb_health

