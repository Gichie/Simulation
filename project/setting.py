from random import randint

class Setting:
    '''Настройка симуляции'''
    def __init__(self):
        self.width = 8
        self.height = 5
        self.count_grass = 1
        self.count_rock = 1
        self.count_tree = 2
        self.count_herbivore = 2
        self.count_predator = 1
        self.speed_range = (1, 3)
        self.herb_health = (1, 70)
        self.pred_health = (2, 20)
        self.pred_strength = 5

    def determines_speed(self):
        return randint(*self.speed_range)

    def determines_herb_health(self):
        return randint(*self.herb_health)

    def determines_pred_health(self):
        return randint(*self.pred_health)


