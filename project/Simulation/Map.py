from project.Simulation.CreatingObjects import CreatingObjects

class Map:
    '''Карта, содержит в себе коллекцию в виде хеш-таблицы(словаря) для хранения существ(значение) и их расположения(ключ).'''
    def __init__(self, width, height):
        self.map = {}
        self.width = width
        self.height = height

    def create_map(self):
        for i in range(self.height):
            for j in range(self.width):
                self.map[(i, j)] = '(...)'


    def display_map(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.map[(i, j)], end='')
            print()




if __name__ == '__main__':
    map = Map(5, 5)
    map.create_map()
    map.display_map()
