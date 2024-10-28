from project.simulation.creating_objects import CreatingObjects
from project.entity.static_objects.empty import Empty

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

