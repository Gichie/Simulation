from project.entity.entity import Entity
from project.entity.static_objects.empty import Empty


class Grass (Entity):
    '''Ресурс для травоядных(Herbivore)'''
    def __init__(self, x,y):
        super().__init__(x,y)
        self.name = 'Grss'
    def __str__(self):
        return 'Grss'

    @classmethod
    def create_grass(cls, map):
        empty_coords = []
        for k, v in map.items():
            if isinstance(v, Empty):
                empty_coords.append(k)

        #map[(x,y)] = Grass(x, y)



