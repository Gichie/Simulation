from project.entity.Creatures.Creature import Creature
from project.simulation.creatingObjects import CreatingObjects
from project.entity.Static_objects.empty import Empty

class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x,y, speed: int, hp: int):
        super().__init__(x,y, speed, hp)
        self.name = 'Herb'

    def make_move(self, creature, path_of_animal: list, map: dict):
        if len(path_of_animal) == 2:
            x, y = path_of_animal[1]
            map[(x,y)] = Empty(x,y)
            print(f'{self.name} съел Grss {self.x, self.y} -> {x, y}')
            CreatingObjects.remove_creature(x, y, self.name)
        else:
            x,y = path_of_animal[0]
            map[(x,y)] = Empty(x,y)
            creature.x, creature.y = path_of_animal[1]
            map[path_of_animal[1]] = creature
            print(f'{self.name} походил {path_of_animal[0]} -> {creature.x, creature.y}')

    def __str__(self):
        return self.name
