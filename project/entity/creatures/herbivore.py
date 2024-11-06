from project.entity.creatures.creature import Creature


class Herbivore(Creature):
    '''Травоядное. Стремится найти ресурс (траву), может потратить свой ход на движение в сторону травы, либо на её поглощение.'''

    def __init__(self, x: int, y: int, speed: int, hp: int, engry: int = 1, **strength):
        super().__init__(x, y, speed, hp, engry)
        self._name = 'Herb'

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        # Определяем, действие: ест траву или движется
        print(f'Ходит {self}{self.x, self.y} со скоростью {self._speed} и здоровьем {self._hp}/{self._full_hp}')
        if self._hp <= 0:
            self.remove_creature(map)
            return

        self._hp -= self._engry

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if len(path_of_animal) == 2:
                self.eat_target(map[path_of_animal[1]], map)
            elif len(path_of_animal) > 2:
                self.move(path_of_animal, map)
        else:
            print(f'{self}{self.x, self.y} больше некуда идти :(')
