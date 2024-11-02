from project.entity.creatures.creature import Creature
from project.entity.static_objects.empty import Empty
from project.setting import Setting
from project.simulation.breadth_first_search import Bfs
from project.simulation.creating_objects import CreatingObjects
from project.simulation.map import Map


class Predator(Creature):
    '''Хищник. На что может потратить ход хищник:
    Переместиться (чтобы приблизиться к жертве - травоядному)
    Атаковать травоядное. При этом количество HP травоядного уменьшается на силу атаки хищника. Если значение HP жертвы опускается до 0, травоядное исчезает'''

    def __init__(self, x, y, speed: int, hp: int, strengh: int, engry: int = 1):
        super().__init__(x, y, speed, hp, engry)
        self.strengh = strengh
        self.name = "Pred"
        self.amount_eaten = 0
        self.setting: Setting

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        # Определяем, действие: ест травоядного или движется

        # Голодание
        if self.hp <= 0:
            print(f'Ходит {self}')
            self.remove_pred(map)
            return None
        else:
            print(
                f'Ходит {self}, Скорость: {self.speed}, Здоровье: {self.hp}/{self.full_hp}, Сила: {self.strengh}, Кол-во съеденных: {self.amount_eaten}')
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

        # Позиция цели(травоядного)
        x, y = position
        target = map[(x, y)]

        # Проверка, убьет хищник цель или ранит
        if self.attacks_target(target):
            self.amount_eaten += 1
            print(f'{self} съел Herb {self.x, self.y} -> {x, y} и набрался здоровья')
            # Удаление Травоядного
            target.remove_herb(map)
            self.hp = self.full_hp

            # Создание нового хищника(размножение)
            self.create_predator(map)
        else:
            print(f'{self} атакует Herb {self.x, self.y} -> {x, y}, у Herb осталось {target.hp} здоровья')

    def create_predator(self, map: dict[tuple[int, int], Creature]) -> None:
        '''Создание нового хищника(механика размножения) после того, как он съел травоядное'''
        if self.amount_eaten > 1:
            coordinates_for_spawn: tuple[int, int] = Bfs((self.x, self.y), map).bfs(' ')
            if coordinates_for_spawn:
                coordinates_for_spawn = coordinates_for_spawn[-1]
                new_predator = Predator(
                    *coordinates_for_spawn,
                    self.setting.determines_speed(),
                    self.setting.determines_pred_health(),
                    self.setting.determines_strength()
                )
                map[(coordinates_for_spawn)] = new_predator
                CreatingObjects.moving_creatures.append(new_predator)
                print(f'{self} Размножился')
            else:
                print('Размножиться Хищнику не удалось')

    def attacks_target(self, target):
        if self.strengh >= target.hp:
            return True
        else:
            target.hp -= self.strengh
            return False

    def remove_pred(self, map: dict[tuple[int, int], Creature]) -> None:
        map[(self.x, self.y)] = Empty(self.x, self.y)
        CreatingObjects.remove_creature(self.x, self.y)
        print(f'{self}{self.x, self.y} is dead')

        # Проверка, остались ли еще Хищники, если нет, создание их
        if self.is_predator_over():
            self.spawn_new_predators(map)

    def spawn_new_predators(self, map: dict[tuple[int, int], Creature]) -> None:
        '''Создание нового хищника, если все хищники умерли'''
        for _ in range(self.setting.count_predator):
            coordinates = Map.collects_free_coordinates(map)
            if coordinates:
                new_predator = Predator(
                    *coordinates,
                    self.setting.determines_speed(),
                    self.setting.determines_pred_health(),
                    self.setting.determines_strength()
                )
                map[coordinates] = new_predator
                CreatingObjects.moving_creatures.append(new_predator)
                print(f'Появился новый Pred в {coordinates}')

    def is_predator_over(self) -> bool:
        return not any(isinstance(creature, Predator) for creature in CreatingObjects.moving_creatures)
