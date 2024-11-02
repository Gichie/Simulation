from random import randint

class Setting:
    '''Настройка симуляции'''
    def __init__(self):
        self.width = 15
        self.height = 15
        self.count_grass = 3
        self.count_rock = 7
        self.count_tree = self.count_rock
        self.count_predator = 1
        self.count_herbivore = self.count_predator * 19
        self.speed_range = (1, 2)
        self.herb_health = (7, 65)
        self.pred_health = (1, 9)
        self.pred_strength = (2, 69)

    def determines_speed(self):
        return randint(*self.speed_range)

    def determines_herb_health(self):
        return randint(*self.herb_health)

    def determines_pred_health(self):
        return randint(*self.pred_health)

    def determines_strength(self):
        return randint(*self.pred_strength)

