from project.entity.creatures.creature import Creature
from project.simulation.creating_objects import CreatingObjects
from project.entity.static_objects.empty import Empty

class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x: int, y: int, speed: int, hp: int):
        super().__init__(x, y, speed, hp)
        self.name = 'Herb'

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int,  int], Creature]) -> None:
        # Определяем, действие: ест траву или движется
        if len(path_of_animal) == 2:
            self.eat_grass(path_of_animal[1], map)
        else:
            self.move(path_of_animal, map)

    def eat_grass(self, position: tuple[int, int], map: dict[tuple[int, int], Creature]) -> None:
        x, y = position
        print(f'{self} съел Grass {self.x, self.y} -> {x, y}')
        CreatingObjects.remove_creature(x, y, self.name)
        map[(x, y)] = Empty(x, y)

    def move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
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
    def __str__(self):
        return self.name
