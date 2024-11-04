from project.entity.entity import Entity
from project.entity.static_objects.empty import Empty
from project.simulation.creating_objects import CreatingObjects
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
            print(f'Трава выросла {coords}')

    def remove_grass(self, map: dict[tuple[int, int], 'Grass']) -> None:
        map[(self.x, self.y)] = Empty(self.x, self.y)
        CreatingObjects.remove_creature(self.x, self.y, 'Herb')
        self.create_grass(map)

