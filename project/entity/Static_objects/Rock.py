from project.entity.Entity import Entity

class Rock(Entity):
    '''Статичный объект, занимающий клетку'''
    pass
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = 'Rock'