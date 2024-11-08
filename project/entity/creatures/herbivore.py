from project.entity.creatures.creature import Creature


class Herbivore(Creature):
    """
    Herbivore is a creature that seeks out a resource (grass) and may spend its turn either moving toward it or consuming it.
    """

    def __init__(self, x: int, y: int, speed: int, hp: int, hungry: int = 1, **strength):
        """Initializes a Herbivore with specified coordinates, speed, health, hunger level, and optional strength."""
        super().__init__(x, y, speed, hp, hungry)
        self._name = 'Herb'

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        """
        Executes the herbivore's move. If grass is adjacent, it consumes it; otherwise, it moves toward the nearest grass.
        """
        print(f'Ходит {self}{self.x, self.y} со скоростью {self._speed} и здоровьем {self._hp}/{self._full_hp}')

        if self._is_starving():
            self._remove_creature(map)
            return

        self._reduces_health()

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if len(path_of_animal) == 2:
                self.eat_target(map[path_of_animal[1]], map)
            elif len(path_of_animal) > 2:
                self.move(path_of_animal, map)
        else:
            print(f'{self}{self.x, self.y} больше некуда идти :(')
