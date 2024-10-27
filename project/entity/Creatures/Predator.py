from project.entity.Creatures.Creature import Creature
from project.simulation.creatingObjects import CreatingObjects
from project.entity.Static_objects.empty import Empty

class Predator(Creature):
    '''Хищник. На что может потратить ход хищник:

    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника. Если значение HP жертвы опускается до 0, травоядное исчезает'''
    def __init__(self, x, y, speed: int, hp: int, strengh: int):
        super().__init__(x,y, speed, hp)
        self.strengh = strengh
        self.name = "Pred"

    def make_move(self, path_of_animal: list, map: dict):
        if len(path_of_animal) == 2:
            self.eat_herb(path_of_animal[1], map)
        else:
            self.move(path_of_animal, map)

    def eat_herb(self, position: tuple, map: dict):
        x, y = position
        print(f'{self} съел Herb {self.x, self.y} -> {x, y}')
        CreatingObjects.remove_creature(x, y, self.name)
        map[(x, y)] = Empty(x, y)

    def move(self, path_of_animal: list, map: dict):
        x, y = path_of_animal[0]
        self.x, self.y = path_of_animal[1]
        map[path_of_animal[1]] = self
        print(f'{self.name} походил {x, y} -> {self.x, self.y}')
        map[(x, y)] = Empty(x, y)

    def __str__(self):
        return self.name