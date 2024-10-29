from project.entity.creatures.creature import Creature
from project.simulation.creating_objects import CreatingObjects
from project.entity.static_objects.empty import Empty

class Predator(Creature):
    '''Хищник. На что может потратить ход хищник:

    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника. Если значение HP жертвы опускается до 0, травоядное исчезает'''
    def __init__(self, x, y, speed: int, hp: int, strengh: int, engry: int = 2):
        super().__init__(x,y, speed, hp, engry)
        self.strengh = strengh
        self.name = "Pred"

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int,  int], Creature]) -> None:
        # Определяем, действие: ест травоядного или движется

        # Голодание
        if self.hp <= 0:
            self.remove_pred(map)
            CreatingObjects.remove_creature(self.x, self.y)
            print(f'{self}{self.x, self.y} is dead от голода и холода и старости')
            return None
        else:
            print(f'Ходит {self} со скоростью {self.speed} и здоровьем {self.hp}/{self.full_hp}')
            self.hp -= self.engry

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if len(path_of_animal) == 2:
                self.eat_herb(path_of_animal[1], map)
            else:
                self.move(path_of_animal, map)
        else:
            print(f'{self}{self.x, self.y} больше некуда идти :(')

    def eat_herb(self, position: tuple[int, int], map: dict[tuple[int, int], Creature]) -> None:
        # Хищник ест травоядное, восполняет здоровье до полного и травоядное удаляется с карты и из списка moving_creatures
        x, y = position
        print(f'{self} съел Herb {self.x, self.y} -> {x, y} и восполнил здоровье')
        CreatingObjects.remove_creature(x, y, self.name)
        map[(x, y)] = Empty(x, y)
        self.hp = self.full_hp

    def move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        # Хищник движется к ближайшему травоядному(по поиску в ширину) со своей скоростью
        # Получение новой позиции на основе скорости
        target_index = min(self.speed, len(path_of_animal) - 2)
        target_position = path_of_animal[target_index]

        # Обновление позиции и карты
        old_position = (self.x, self.y)
        self.x, self.y = target_position
        map[target_position] = self
        print(f'{self.name} походил {old_position} -> {self.x, self.y}')

        # Обновление старого положения, если оно не пустое
        map[old_position] = Empty(*old_position)

    def remove_pred(self, map: dict[tuple[int, int], Creature]) -> None:
        map[(self.x, self.y)] = Empty(self.x, self.y)

    def __str__(self):
        return self.name
