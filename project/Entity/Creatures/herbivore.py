from project.Entity.Creatures.Creature import Creature

class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x,y, speed: int, hp: int):
        super().__init__(x,y, speed, hp)
        self.name = 'Herb'

    def make_move(self):
        pass


