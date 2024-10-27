from project.entity.Creatures.Creature import Creature
from project.simulation.creatingObjects import CreatingObjects

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
            map[path_of_animal[1]] = '(..)'
            print(f'{self} съел Herb')
            x, y = path_of_animal[1]
            CreatingObjects.remove_creature(x, y, self.name)
        else:
            map[path_of_animal[0]] = '(..)'
            map[path_of_animal[1]] = self.name
            print(f'{self} походил -> {path_of_animal[1]}')
            self.x, self.y = path_of_animal[1]

    def __str__(self):
        return self.name