from project.entity.Entity import Entity

class Empty(Entity):
    '''Пустое место на карте, куда может походить существо'''
    def __init__(self, x,y):
        super().__init__(x,y)
        self.name = f'({self.x},{self.y})'
    def __str__(self):
        return self.name