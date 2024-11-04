from abc import ABC


class Entity(ABC):
    '''Общий класс для всех существ и объектов'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y})'

    def __str__(self):
        return self.name
