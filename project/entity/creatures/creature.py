from abc import abstractmethod

from project.entity.entity import Entity
from project.setting import Setting
from project.simulation.breadth_first_search import Bfs
from project.simulation.creating_objects import CreatingObjects
from project.simulation.map import Map


class Creature(Entity):
    """
    The Creature class serves as a base class for all moving entities in the simulation, such as herbivores and predators.
    It manages the creature's attributes, movement, health, and interaction with other entities on the map.

    Attributes:
    -----------
    _speed : int
        The movement speed of the creature, determining how many steps it can move.
    _full_hp : int
        The maximum health points (HP) the creature can have.
    _hp : int
        The current health points of the creature.
    _hungry : int
        The hunger level, affecting health reduction over time.
    _setting : Setting
        An instance of the Setting class, containing various simulation settings.
    _name : str or None
        The name of the creature, used to identify its type.

    Methods:
    --------
    make_move() -> None
        An abstract method that defines how the creature makes a move (to be implemented by subclasses).

    move(path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], 'Creature']) -> None
        Moves the creature along the specified path, updating the map as it changes position.

    _remove_creature(map: dict[tuple[int, int], 'Creature']) -> None
        Removes the creature from the map if it dies, and checks if new creatures of this type should spawn.

    spawn_new_creature(map: dict[tuple[int, int], 'Creature'], type_of_creature, strength: dict = None) -> None
        Spawns new creatures of this type if none remain in the simulation.

    is_creature_over() -> bool
        Checks if there are any creatures of the same type remaining on the map.

    eat_target(target, map: dict[tuple[int, int], 'Creature']) -> None
        Allows the creature to eat a target (e.g., Grass for Herbivores or Herbivore for Predators),
        restoring health and potentially triggering offspring creation.

    create_offspring(map: dict[tuple[int, int], 'Creature'], creature_class, can_spawn: bool = True) -> None
        Handles the spawning of offspring, if permitted and if there are available coordinates.

    _reduces_health() -> None
        Decreases the creature's health by its hunger level, simulating the effect of starvation.

    _is_starving() -> bool
        Checks if the creature's health has dropped to zero or below, indicating starvation.

    __str__() -> str
        Returns the creature's name as its string representation.
    """

    def __init__(self, x: int, y: int, speed: int, hp: int, hungry: int):
        """
        Initializes the Creature with specified coordinates, speed, health, and hunger level.

        Parameters:
        -----------
        x : int
            The X-coordinate of the creature.
        y : int
            The Y-coordinate of the creature.
        speed : int
            The movement speed of the creature.
        hp : int
            The initial and maximum health points of the creature.
        hungry : int
            The hunger level of the creature, determining how much health decreases over time.
        """
        super().__init__(x, y)
        self._speed = speed
        self._full_hp = hp
        self._hp = hp
        self._hungry = hungry
        self._setting = Setting()
        self._name = None

    @abstractmethod
    def make_move(self):
        """An abstract method that subclasses must implement to define creature movement logic."""
        pass

    def move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], 'Creature']) -> None:
        """
        Moves the creature towards the nearest target at a distance defined by its speed.

        Parameters:
        -----------
        path_of_animal : list[tuple[int, int]]
            A list of coordinates representing the path to the target.
        map : dict[tuple[int, int], 'Creature']
            A dictionary representing the map, with keys as coordinates and values as creatures.
        """
        target_index = min(self._speed, len(path_of_animal) - 2)
        target_position = path_of_animal[target_index]

        old_position = (self.x, self.y)
        self.x, self.y = target_position
        map[target_position] = self
        print(f'{self._name} походил {old_position} -> {self.x, self.y}')

        del map[old_position]

    def _remove_creature(self, map: dict[tuple[int, int], 'Creature']) -> None:
        """
        Removes the creature from the map, and spawns a new creature if the species is extinct.

        Parameters:
        -----------
        map : dict[tuple[int, int], 'Creature']
            The map of creatures, where the creature should be removed.
        """
        del map[(self.x, self.y)]
        CreatingObjects.remove_creature(self.x, self.y)
        print(f'{self}{self.x, self.y} is dead')
        if self.is_creature_over():
            self.spawn_new_creature(map, self.__class__,
                                    strength={'strength': self._setting.determines_strength(self._name)})

    def spawn_new_creature(self, map: dict[tuple[int, int], 'Creature'], type_of_creature,
                           strength: dict = None) -> None:
        """
        Spawns new creatures if no creatures of the same type remain.

        Parameters:
        -----------
        map : dict[tuple[int, int], 'Creature']
            The map of creatures where the new creatures will be added.
        type_of_creature : type
            The class of the creature to spawn.
        strength : dict, optional
            Extra parameters for creature attributes.
        """
        strength = strength or {}
        for _ in range(self._setting.count_creatures(self._name)):
            coordinates = Map.collects_free_coordinates(map)
            if coordinates:
                new_creature = type_of_creature(
                    *coordinates,
                    self._setting.determines_speed(),
                    self._setting.determines_health(self._name),
                    **strength
                )
                map[coordinates] = new_creature
                CreatingObjects.moving_creatures.append(new_creature)
                print(f'Появился новый {self._name} в {coordinates}')

    def is_creature_over(self) -> bool:
        """Checks if any creatures of this type remain."""
        return not any(isinstance(creature, type(self)) for creature in CreatingObjects.moving_creatures)

    def eat_target(self, target, map: dict[tuple[int, int], 'Creature']) -> None:
        """
        Allows a creature to consume a target, either by restoring health and spawning offspring if the conditions are met.
        For herbivores, there must be an empty space on the map, and for predators,
        there must be an empty space and a specified number of creatures consumed.

        Parameters:
        -----------
        target : Entity
            The target entity to be consumed.
        map : dict[tuple[int, int], 'Creature']
            The map of creatures and resources.
        """
        if self._name == 'Herb':
            print(f'{self}{self.x, self.y} съел Grass и восполнил здоровье')
            target.remove_and_spawn_grass(map)
            self._hp = self._full_hp
            # Создание нового травоядного (размножение)
            self.create_offspring(map, type(self))

        elif self._name == 'Pred':
            if self._attacks_target(target):
                print(f'{self}{self.x, self.y} съел {target} и набрался здоровья')
                target._remove_creature(map)
                self._hp = self._full_hp
                self._amount_eaten += 1
                if self._amount_eaten >= self._amount_eaten_for_offspring:
                    self.create_offspring(map, type(self), can_spawn=True)
                    self._amount_eaten = 0
            else:
                print(f'{self}{self.x, self.y} атакует {target}, осталось {target._hp} здоровья')

    def create_offspring(self, map: dict[tuple[int, int], 'Creature'], creature_class, can_spawn: bool = True) -> None:
        """Creates offspring if there are free coordinates available."""
        if not can_spawn:  # Если размножение не разрешено, прерываем метод
            return
        coordinates_for_spawn = Bfs((self.x, self.y), map, self._setting).bfs(type(None))
        if coordinates_for_spawn:
            coordinates_for_spawn = coordinates_for_spawn[-1]
            offspring = creature_class(
                *coordinates_for_spawn,
                self._setting.determines_speed(),
                self._setting.determines_health(self._name),
                strength=self._setting.determines_strength(self._name) if self._name == "Pred" else 0
            )
            map[coordinates_for_spawn] = offspring
            CreatingObjects.moving_creatures.append(offspring)
            print(f'{self._name} размножился {coordinates_for_spawn}')
        else:
            print('Размножиться не удалось')

    def _reduces_health(self):
        """Reduces the creature's health by its hunger level."""
        self._hp -= self._hungry

    def _is_starving(self) -> bool:
        """Checks if the creature's health has reached zero, indicating death from starvation."""
        return self._hp <= 0
