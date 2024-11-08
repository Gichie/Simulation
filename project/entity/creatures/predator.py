from project.entity.creatures.creature import Creature
from project.entity.creatures.herbivore import Herbivore
from project.setting import Setting


class Predator(Creature):
    """
    Predator is a creature that hunts herbivores. Each turn, the predator can:
    - Move towards a nearby herbivore.
    - Attack a herbivore, reducing its HP by the predator's strength. If the herbivore's HP reaches zero, it is removed from the map.

    Attributes:
    -----------
    Inherits attributes from the Creature base class, with additional attributes for strength and hunger.

    Methods:
    --------
    make_move(path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None
        Executes the predator's behavior for its turn, either attacking a nearby herbivore or moving closer to it.

    _can_attack(path_of_animal: list[tuple[int, int]]) -> bool
        Checks if the target herbivore is within attack range.

    _attacks_target(target: Herbivore) -> bool
        Attempts to attack the target herbivore. If the predator's strength is sufficient to reduce the herbivore's HP to zero, the herbivore is defeated.
    """

    def __init__(self, x: int, y: int, speed: int, hp: int, strength: int, hungry: int = 1):
        """
        Initializes a Predator with the specified coordinates, speed, health, strength, and hunger level.

        Parameters:
        -----------
        @param x: int
            X-coordinate of the predator's initial position.
        @param y: int
            Y-coordinate of the predator's initial position.
        @param speed : int
            Movement speed of the predator.
        @param hp : int
            Maximum health points of the predator.
        @param strength : int
            Attack strength of the predator, used to decrease the HP of herbivores.
        @param hungry : int, optional
            Hunger level affecting health reduction over time (default is 1).
        """
        super().__init__(x, y, speed, hp, hungry)
        self._strength = strength
        self._name = "Pred"
        self._amount_eaten = 0
        self._setting: Setting
        self._amount_eaten_for_offspring = self._setting._amount_eaten_for_offspring

    def make_move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], Creature]) -> None:
        """
        Executes the predator's action for the turn, either attacking a nearby herbivore or moving closer to it.

        Parameters:
        -----------
        @param path_of_animal : list[tuple[int, int]]
            List of coordinates representing the path to the nearest herbivore.
        @param map : dict[tuple[int, int], Creature]
            Dictionary representing the map with coordinates as keys and creatures or resources as values.

        Notes:
        ------
        - If the predator's health reaches zero due to starvation, it is removed from the map.
        - If there is an adjacent herbivore, the predator will attack it; otherwise, it will move towards the herbivore.
        """
        print(
            f'Ходит {self}{self.x, self.y}, Скорость: {self._speed}, Здоровье: {self._hp}/{self._full_hp}, Сила: {self._strength}, Кол-во съеденных: {self._amount_eaten}'
        )

        if self._is_starving():
            self._remove_creature(map)
            return

        self._reduces_health()

        if path_of_animal:
            print(f'Его путь: {path_of_animal}')
            if self._can_attack(path_of_animal):
                self.eat_target(map[path_of_animal[1]], map)
            else:
                self.move(path_of_animal, map)
        else:
            print(f"{self}{self.x, self.y} больше некуда идти :(")

    def _can_attack(self, path_of_animal: list[tuple[int, int]]) -> bool:
        """
        Checks if the target herbivore is within attack range.

        Parameters:
        -----------
        @param path_of_animal : list[tuple[int, int]]
            List of coordinates representing the path to the target herbivore.

        Returns:
        --------
        bool
            True if the herbivore is adjacent and within attack range; False otherwise.
        """
        return len(path_of_animal) == 2

    def _attacks_target(self, target: Herbivore):
        """
        Attacks the target herbivore, reducing its HP by the predator's strength.

        Parameters:
        -----------
        @param target : Herbivore
            The target herbivore to attack.

        Returns:
        --------
        bool
            True if the predator's attack reduces the herbivore's HP to zero or below, resulting in its defeat; False otherwise.
        """
        if self._strength >= target._hp:
            return True
        else:
            target._hp -= self._strength
            return False
