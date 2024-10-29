from project.entity.entity import Entity
from project.entity.static_objects.empty import Empty
from random import shuffle


class Grass (Entity):
    '''Ресурс для травоядных(Herbivore)'''
    def __init__(self, x,y):
        super().__init__(x,y)
        self.name = 'Grss'
    def __str__(self):
        return 'Grss'

    @classmethod
    def create_grass(cls, map):
        '''Собирает все пустые координаты и в случайном месте создает траву'''
        empty_coords = []
        for k, v in map.items():
            if isinstance(v, Empty):
                empty_coords.append(k)
        shuffle(empty_coords)
        # Проверка на пустые координаты
        if empty_coords:
            map[(empty_coords[0])] = Grass(*empty_coords[0])
