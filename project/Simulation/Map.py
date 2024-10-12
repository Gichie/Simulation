from project.Simulation.CreatingObjects import CreatingObjects
class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''
    def __init__(self, width, height):
        self.map = {}
        self.width = width
        self.height = height
        for i in range(height):
            for j in range(width):
                self.map[(i, j)] = '(...)'
        for obj in CreatingObjects.creating_objects:
            self.map[(obj.x, obj.y)] = obj.name