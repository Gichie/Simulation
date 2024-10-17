from project.simulation.creatingObjects import CreatingObjects
from project.simulation.actions import Actions
from project.setting import Setting

class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''
    def __init__(self, width=3, height=3):
        self.map = {}
        self.width = width
        self.height = height

    def create_map(self):
        for i in range(self.height):
            for j in range(self.width):
                self.map[(i, j)] = '(..)'
        for el in CreatingObjects.creating_objects:
            self.map[(el.y, el.x)] = el.name
        return self.map
