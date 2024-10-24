from project.Entity.Creatures.Creature import Creature

class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x,y, speed: int, hp: int):
        super().__init__(x,y, speed, hp)
        self.name = 'Herb'

    def make_move(self, path_of_animal: list, map: dict):
        if len(path_of_animal) == 2:
            map[path_of_animal[1]] = '(..)'
            print(f'{self.name} съел Grss {self.x, self.y} -> {path_of_animal[1]}')
        else:
            map[path_of_animal[0]] = '(..)'
            map[path_of_animal[1]] = self.name
            self.x, self.y = path_of_animal[1]
            print(f'{self.name} походил {path_of_animal[0]} -> {self.x, self.y}')


