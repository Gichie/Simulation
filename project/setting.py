from random import randint

class Setting:
    '''Настройка симуляции'''
    def __init__(self):
        self.width = 22
        self.height = 19
        self.count_grass = 3
        self.count_rock = 7
        self.count_tree = self.count_rock
        self.count_predator = 2
        self.count_herbivore = self.count_predator * 22
        self.speed_range = (1, 2)
        self.herb_health = (6, 65)
        self.pred_health = (5, 11)
        self.pred_strength = (5, 68)

    def determines_speed(self):
        return randint(*self.speed_range)

    def determines_herb_health(self):
        return randint(*self.herb_health)

    def determines_pred_health(self):
        return randint(*self.pred_health)

    def determines_strength(self):
        return randint(*self.pred_strength)

