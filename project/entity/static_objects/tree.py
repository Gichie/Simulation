from project.entity.entity import Entity

class Tree(Entity):
    '''Статичный объект, занимающий клетку'''
    pass
    def __init__(self, x, y):
        super().__init__(x, y)
        self. name = 'Tree'