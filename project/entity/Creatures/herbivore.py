from project.entity.Creatures.Creature import Creature
from project.simulation.creatingObjects import CreatingObjects
from project.entity.Static_objects.empty import Empty

class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x,y, speed: int, hp: int):
        super().__init__(x,y, speed, hp)
        self.name = 'Herb'

    def make_move(self, path_of_animal: list, map: dict):
        if len(path_of_animal) == 2:
            self.eat_grass(path_of_animal[1], map)
        else:
            self.move(path_of_animal, map)

    def eat_grass(self, position: tuple, map: dict):
        x, y = position
        print(f'{self} съел Grass {self.x, self.y} -> {x, y}')
        CreatingObjects.remove_creature(x, y, self.name)
        map[(x, y)] = Empty(x, y)

    def move(self, path_of_animal: list, map: dict):
        x,y = path_of_animal[0]
        self.x, self.y = path_of_animal[1]
        map[path_of_animal[1]] = self
        print(f'{self.name} походил {x, y} -> {self.x, self.y}')
        # Удаление старого положения, если оно не пустое
        map[(x, y)] = Empty(x, y)
    def __str__(self):
        return self.name
