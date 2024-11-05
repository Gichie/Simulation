from project.entity.entity import Entity


class Empty(Entity):
    '''Пустое место на карте, куда может походить существо'''

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.name = ' '

    def __str__(self):
        return self.name
