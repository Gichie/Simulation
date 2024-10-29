from project.entity.creatures.creature import Creature
from project.simulation.creating_objects import CreatingObjects
from project.entity.static_objects.empty import Empty
from project.entity.static_objects.grass import Grass

class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x: int, y: int, speed: int, hp: int, engry: int = 1):
        super().__init__(x, y, speed, hp, engry)
        self.name = 'Herb'

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int,  int], Creature]) -> None:
        # Определяем, действие: ест траву или движется
        print(f'Ходит {self} со скоростью {self.speed} и здоровьем {self.hp}/{self.full_hp}')

        # Голодание
        if self.hp <= 0:
            self.remove_herb(map)
            CreatingObjects.remove_creature(self.x, self.y)
            print(f'{self}{self.x, self.y} is dead')
            return None
        else:
            self.hp -= self.engry

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if len(path_of_animal) == 2:
                self.eat_grass(path_of_animal[1], map)
            else:
                self.move(path_of_animal, map)
        else:
            print(f'{self}{self.x, self.y} больше некуда идти :(')

    def eat_grass(self, position: tuple[int, int], map: dict[tuple[int, int], Creature]) -> None:
        # Травяожное ест траву, восполняет здоровье до полного и трава удаляется с карты и из списка grasses
        x, y = position
        print(f'{self} съел Grass {self.x, self.y} -> {x, y} и восполнил здоровье')
        CreatingObjects.remove_creature(x, y, self.name)
        map[(x, y)] = Empty(x, y)
        # метод, генерирующий 1 траву в случайном свободном месте
        Grass.create_grass(map)
        self.hp = self.full_hp

    def move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        # Травяодное движется к ближайшей траве(по поиску в ширину) со своей скоростью
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

    def remove_herb(self, map: dict[tuple[int, int], Creature]) -> None:
        map[(self.x, self.y)] = Empty(self.x, self.y)

    def __str__(self):
        return self.name
