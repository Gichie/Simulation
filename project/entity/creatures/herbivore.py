from project.entity.creatures.creature import Creature
from project.entity.static_objects.empty import Empty
from project.entity.static_objects.grass import Grass
from project.simulation.breadth_first_search import Bfs
from project.simulation.creating_objects import CreatingObjects


class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''

    def __init__(self, x: int, y: int, speed: int, hp: int, engry: int = 1, **strength):
        super().__init__(x, y, speed, hp, engry)
        self.name = 'Herb'

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        # Определяем, действие: ест траву или движется
        print(f'Ходит {self}{self.x, self.y} со скоростью {self.speed} и здоровьем {self.hp}/{self.full_hp}')
        if self.hp <= 0:
            self.remove_creature(map)
            return

        self.hp -= self.engry

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if len(path_of_animal) == 2:
                self.eat_target(map[path_of_animal[1]], map)
            elif len(path_of_animal) > 2:
                self.move(path_of_animal, map)
        else:
            print(f'{self}{self.x, self.y} больше некуда идти :(')

    def create_herbivore(self, map: dict[tuple[int, int], Creature]) -> None:
        '''Создание нового травоядного(механика размножения) после того, как оно съело траву'''
        coordinates_for_spawn = Bfs((self.x, self.y), map).bfs(' ')
        if coordinates_for_spawn:
            coordinates_for_spawn = coordinates_for_spawn[-1]
            new_herbivore = Herbivore(
                *coordinates_for_spawn,
                self.setting.determines_speed(),
                self.setting.determines_health(self.name)
            )
            map[(coordinates_for_spawn)] = new_herbivore
            CreatingObjects.moving_creatures.append(new_herbivore)
        else:
            print('Размножиться травоядному не удалось')
