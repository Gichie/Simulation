from random import shuffle

from project.entity.entity import Entity
from project.setting import Setting
from project.simulation.creating_objects import CreatingObjects


class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''

    setting = Setting()
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map = self.create_map()
        setting = Setting()

    def create_map(self) -> dict[tuple[int, int], Entity]:
        game_map = {(el.x, el.y): el for el in CreatingObjects.creating_objects}
        return game_map

    @classmethod
    def collects_free_coordinates(cls, map: dict[tuple[int, int]]) -> tuple([int, int]):
        '''Собирает все пустые координаты и перемешивает их'''
        empty_coords = [(x, y) for x in range(cls.setting.width) for y in range(cls.setting.height) if map.get((x, y), None) is None]
        if empty_coords:
            shuffle(empty_coords)
            return empty_coords[0]
