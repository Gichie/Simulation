from abc import abstractmethod

from project.entity.entity import Entity
from project.setting import Setting
from project.simulation.breadth_first_search import Bfs
from project.simulation.creating_objects import CreatingObjects
from project.simulation.map import Map


class Creature(Entity):
    def __init__(self, x: int, y: int, speed: int, hp: int, engry: int):
        super().__init__(x, y)
        self.speed = speed
        self.full_hp = hp
        self.hp = hp
        self.engry = engry
        self.setting = Setting()
        self.name = None

    @abstractmethod
    def make_move(self):
        pass

    def move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], 'Creature']) -> None:
        # Существо движется к ближайшей цели(по поиску в ширину) со своей скоростью
        target_index = min(self.speed, len(path_of_animal) - 2)
        target_position = path_of_animal[target_index]

        # Обновление позиции и карты
        old_position = (self.x, self.y)
        self.x, self.y = target_position
        map[target_position] = self
        print(f'{self.name} походил {old_position} -> {self.x, self.y}')

        # Обновление старого положения, если оно не пустое
        del map[old_position]

    def remove_creature(self, map: dict[tuple[int, int], 'Creature']) -> None:
        del map[(self.x, self.y)]
        CreatingObjects.remove_creature(self.x, self.y)
        print(f'{self}{self.x, self.y} is dead')
        if self.is_creature_over():
            self.spawn_new_creature(map, self.__class__,
                                    strength={'strength': self.setting.determines_strength(self.name)})

    def spawn_new_creature(self, map: dict[tuple[int, int], 'Creature'], type_of_creature,
                           strength: dict = None) -> None:
        '''Создание новых существ, если все существа одного вида умерли'''
        strength = strength or {}
        for _ in range(self.setting.count_creatures(self.name)):
            coordinates = Map.collects_free_coordinates(map)
            if coordinates:
                new_creature = type_of_creature(
                    *coordinates,
                    self.setting.determines_speed(),
                    self.setting.determines_health(self.name),
                    **strength
                )
                map[coordinates] = new_creature
                CreatingObjects.moving_creatures.append(new_creature)
                print(f'Появился новый {self.name} в {coordinates}')

    def is_creature_over(self) -> bool:
        '''Проверяет осталось ли хоть одно существо переданного типа '''
        return not any(isinstance(creature, type(self)) for creature in CreatingObjects.moving_creatures)

    def eat_target(self, target, map: dict[tuple[int, int], 'Creature']) -> None:
        '''Универсальный метод поглощения цели (Травы или Травоядного)'''
        if self.name == 'Herb':
            print(f'{self}{self.x, self.y} съел Grass и восполнил здоровье')
            target.remove_grass(map)
            self.hp = self.full_hp
            # Создание нового травоядного (размножение)
            self.create_offspring(map, type(self))

        elif self.name == 'Pred':
            if self.attacks_target(target):
                print(f'{self}{self.x, self.y} съел {target} и набрался здоровья')
                target.remove_creature(map)
                self.hp = self.full_hp
                self.amount_eaten += 1
                if self.amount_eaten >= self.amount_eaten_for_offspring:
                    self.create_offspring(map, type(self), can_spawn=True)
                    self.amount_eaten = 0
            else:
                print(f'{self}{self.x, self.y} атакует {target}, осталось {target.hp} здоровья')

    def create_offspring(self, map: dict[tuple[int, int], 'Creature'], creature_class, can_spawn: bool = True) -> None:
        '''Создание нового существа(механика размножения)'''
        if not can_spawn:  # Если размножение не разрешено, прерываем метод
            return
        coordinates_for_spawn = Bfs((self.x, self.y), map, self.setting).bfs(type(None))
        if coordinates_for_spawn:
            coordinates_for_spawn = coordinates_for_spawn[-1]
            offspring = creature_class(
                *coordinates_for_spawn,
                self.setting.determines_speed(),
                self.setting.determines_health(self.name),
                strength=self.setting.determines_strength(self.name) if self.name == "Pred" else 0
            )
            map[coordinates_for_spawn] = offspring
            CreatingObjects.moving_creatures.append(offspring)
            print(f'{self.name} размножился {coordinates_for_spawn}')
        else:
            print('Размножиться не удалось')

    def __str__(self) -> str:
        return self.name
