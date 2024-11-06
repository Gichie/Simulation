from project.entity.creatures.creature import Creature
from project.entity.creatures.herbivore import Herbivore
from project.setting import Setting


class Predator(Creature):
    '''Хищник. На что может потратить ход хищник:
    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника. Если значение HP жертвы опускается до 0, травоядное исчезает'''

    def __init__(self, x: int, y: int, speed: int, hp: int, strength: int, engry: int = 1):
        super().__init__(x, y, speed, hp, engry)
        self.strength = strength
        self._name = "Pred"
        self.amount_eaten = 0
        self._setting: Setting
        self.amount_eaten_for_offspring = self._setting.amount_eaten_for_offspring

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        # Определяем, действие: ест травоядного или движется
        print(
            f'Ходит {self}{self.x, self.y}, Скорость: {self._speed}, Здоровье: {self._hp}/{self._full_hp}, Сила: {self.strength}, Кол-во съеденных: {self.amount_eaten}')
        # Голодание
        if self._hp <= 0:
            self.remove_creature(map)
            return
        else:
            self._hp -= self._engry

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if len(path_of_animal) == 2:
                self.eat_target(map[path_of_animal[1]], map)
            else:
                self.move(path_of_animal, map)
        else:
            print(f"{self}{self.x, self.y} больше некуда идти :(")

    def attacks_target(self, target: Herbivore):
        if self.strength >= target._hp:
            return True
        else:
            target._hp -= self.strength
            return False
