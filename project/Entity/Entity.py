from abc import ABC
class Entity(ABC):
    '''Общий класс для всех существ и объектов'''
    def __init__(self, x, y):
        self.x = x
        self.y = y