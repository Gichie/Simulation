from project.entity.entity import Entity

class Rock(Entity):
    '''Статичный объект, занимающий клетку'''
    pass
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self._name: str = 'Rock'