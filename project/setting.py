from random import randint


class Setting:
    '''Настройка симуляции'''

    def __init__(self):
        self.width = 3
        self.height = 3
        self.count_grass = 4
        self.count_rock = 0
        self.count_tree = self.count_rock
        self.count_predator = 1
        self.count_herbivore = self.count_predator * 2
        self.speed_range = (1, 2)
        self.herb_health = (14, 65)
        self.pred_health = (3, 26)
        self.pred_strength = (3, 57)
        self.amount_eaten_for_offspring = 9

    def determines_speed(self) -> int:
        return randint(*self.speed_range)

    def determines_health(self, name_creature: str) -> int:
        if name_creature == 'Herb':
            return randint(*self.herb_health)
        elif name_creature == 'Pred':
            return randint(*self.pred_health)
        raise TypeError(f"Неверный тип входных данных {name_creature}")

    def determines_strength(self, name_creature: str) -> int:
        if name_creature == 'Pred':
            return randint(*self.pred_strength)
        return None

    def count_creatures(self, name_creature: str) -> int:
        if name_creature == 'Herb':
            return self.count_herbivore
        elif name_creature == 'Pred':
            return self.count_predator
