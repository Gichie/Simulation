from project.Entity.Entity import Entity

class Grass (Entity):
    '''Ресурс для травоядных(Herbivore)'''
    def __init__(self, x,y):
        super().__init__(x,y)
        self.name = 'Grss'
    def __str__(self):
        return 'Grss'


