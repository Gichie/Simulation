from random import randint

class Setting:
    '''Настройка симуляции'''
    def __init__(self):
        self.width = 6
        self.height = 5
        self.count_grass = 2
        self.count_rock = 1
        self.count_tree = 1
        self.count_herbivore = 2
        self.count_predator = 1
        self.speed_range = (1, 3)
        self.hp = 10
        self.pred_strength = 5

    def determines_speed(self):
        return randint(*self.speed_range)


