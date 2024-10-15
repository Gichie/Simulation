from project.Entity.Creatures.Creature import Creature

class Predator(Creature):
    '''Хищник. На что может потратить ход хищник:

    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника. Если значение HP жертвы опускается до 0, травоядное исчезает'''
    def __init__(self, x, y, speed: int, hp: int, strengh: int):
        super().__init__(x,y, speed, hp)
        self.strengh = strengh
        self.name = "Pred"

    def make_move(self):
        pass