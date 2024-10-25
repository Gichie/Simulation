from project.simulation.creatingObjects import CreatingObjects


class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''
    def __init__(self, width, height):
        self.map = {}
        self.width = width
        self.height = height

    def create_map(self, creating_objects):
        for i in range(self.width):
            for j in range(self.height):
                self.map[(i, j)] = '    '
        for el in CreatingObjects.creating_objects:
            self.map[(el.x, el.y)] = el
        return self.map
