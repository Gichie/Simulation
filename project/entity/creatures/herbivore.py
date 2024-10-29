from project.entity.creatures.creature import Creature
from project.simulation.creating_objects import CreatingObjects
from project.entity.static_objects.empty import Empty
from project.entity.static_objects.grass import Grass
from project.simulation.breadth_first_search import Bfs


class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''
    def __init__(self, x: int, y: int, speed: int, hp: int, engry: int = 1):
        super().__init__(x, y, speed, hp, engry)
        self.name = 'Herb'


    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int,  int], Creature]) -> None:
        # Определяем, действие: ест траву или движется

        # Голодание
        if self.hp <= 0:
            self.remove_herb(map)
            CreatingObjects.remove_creature(self.x, self.y)
            print(f'{self}{self.x, self.y} is dead')
            return None
        else:
            print(f'Ходит {self} со скоростью {self.speed} и здоровьем {self.hp}/{self.full_hp}')
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
        print(f'{self} съел Grass {self.x, self.y} -> {x, y}, восполнил здоровье и размножился')
        CreatingObjects.remove_creature(x, y, self.name)
        map[(x, y)] = Empty(x, y)
        Grass.create_grass(map)
        self.hp = self.full_hp

        # Создание нового травоядного (размножение)
        self.create_herbivore(map)

    def create_herbivore(self, map: dict[tuple[int, int], Creature]) -> None:
        '''Создание нового травоядного(механика размножения) после того, как оно съело траву'''
        coordinates_for_spawn: tuple[int, int] = Bfs((self.x, self.y), map).bfs(' ')[-1]
        new_herbivore = Herbivore(*coordinates_for_spawn, self.setting.determines_speed(), self.setting.determines_herb_health())
        map[(coordinates_for_spawn)] = new_herbivore
        CreatingObjects.moving_creatures.append(new_herbivore)

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
