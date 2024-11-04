from random import randint

class Setting:
    '''Настройка симуляции'''
    def __init__(self):
        self.width = 11
        self.height = 11
        self.count_grass = 7
        self.count_rock = 7
        self.count_tree = self.count_rock
        self.count_predator = 1
        self.count_herbivore = self.count_predator * 20
        self.speed_range = (1, 2)
        self.herb_health = (12, 65)
        self.pred_health = (1, 4)
        self.pred_strength = (1, 64)
        self.amount_eaten_for_offspring = 5

    def determines_speed(self):
        return randint(*self.speed_range)

    def determines_health(self, name_creature):
        if name_creature == 'Herb':
            return randint(*self.herb_health)
        elif name_creature == 'Pred':
            return randint(*self.pred_strength)
        raise TypeError(f"Неверный тип входных данных {name_creature}")

    def determines_strength(self, name_creature):
        if name_creature == 'Pred':
            return randint(*self.pred_strength)
        return None

    def count_creatures(self, name_creature):
        if name_creature == 'Herb':
            return self.count_herbivore
        elif name_creature == 'Pred':
            return self.count_predator


