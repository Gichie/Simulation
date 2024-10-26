from project.simulation.creatingObjects import CreatingObjects
from collections import defaultdict


class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''
    def __init__(self, width, height):
        self.map = defaultdict(lambda: ' ')
        self.width = width
        self.height = height
        self.create_map()

    def create_map(self):
        for el in CreatingObjects.creating_objects:
            self.map[(el.x, el.y)] = el
        return None
