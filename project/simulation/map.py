from project.simulation.creating_objects import CreatingObjects
from project.entity.static_objects.empty import Empty
from random import shuffle

class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = self.create_map()

    def create_map(self):
        game_map = {(i, j): Empty(i,j) for i in range(self.width) for j in range(self.height)}
        for el in CreatingObjects.creating_objects:
            game_map[(el.x, el.y)] = el
        return game_map

    @classmethod
    def collects_free_coordinates(cls, map: dict[tuple[int,  int]]) -> tuple([int, int]):
        '''Собирает все пустые координаты и перемешивает их'''
        empty_coords = [k for k, v in map.items() if isinstance(v, Empty)]
        if empty_coords:
            shuffle(empty_coords)
            return empty_coords[0]
