from project.entity.entity import Entity
from project.simulation.map import Map


class Grass (Entity):
    '''Ресурс для травоядных(Herbivore)'''
    def __init__(self, x,y):
        super().__init__(x,y)
        self.name = 'Grss'
    def __str__(self):
        return 'Grss'

    @classmethod
    def create_grass(cls, map):
        '''Собирает все пустые координаты и в случайном месте создает траву'''
        coords = Map.collects_free_coordinates(map)
        if coords:
            map[coords] = Grass(*coords)
