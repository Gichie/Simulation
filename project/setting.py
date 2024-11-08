from random import randint


class Setting:
    """
    A class to configure the simulation settings.

    This class manages the simulation parameters, including map dimensions, the number of creatures,
    and the ranges for attributes such as health, strength, and speed for different creature types.

    Attributes:
    -----------
    width : int
        The width of the simulation map (number of columns). Default is 15.
    height : int
        The height of the simulation map (number of rows). Default is 15.
    count_grass : int
        The number of Grass entities to place on the map. Default is 4.
    count_rock : int
        The number of Rock entities to place on the map. Default is 8.
    count_tree : int
        The number of Tree entities to place on the map. Default is equal to the count of Rocks.
    count_predator : int
        The number of Predator entities to place on the map. Default is 8.
    count_herbivore : int
        The number of Herbivore entities to place on the map. Default is equal to the number of Predators.
    speed_range : tuple[int, int]
        The range (min, max) for determining the speed of creatures. Default is (1, 2).
    herb_health : tuple[int, int]
        The range (min, max) for determining the health of Herbivores. Default is (7, 65).
    pred_health : tuple[int, int]
        The range (min, max) for determining the health of Predators. Default is (8, 22).
    pred_strength : tuple[int, int]
        The range (min, max) for determining the strength of Predators. Default is (8, 53).
    _amount_eaten_for_offspring : int
        The amount of food a Predator needs to consume to reproduce. Default is 8.

    Methods:
    --------
    determines_speed() -> int:
        Returns a random speed value for a creature based on the `speed_range`.

    determines_health(name_creature: str) -> int:
        Returns a random health value for the specified creature type ('Herb' or 'Pred').

    determines_strength(name_creature: str) -> int:
        Returns a random strength value for Predators, or `None` for other creature types.

    count_creatures(name_creature: str) -> int:
        Returns the number of creatures of the specified type ('Herb' or 'Pred').
    """

    def __init__(self):
        """
        Initializes the simulation settings with default values.

        Default Values:
            width = 15
            height = 15
            count_grass = 4
            count_rock = 8
            count_tree = count_rock
            count_predator = 8
            count_herbivore = count_predator * 1
            speed_range = (1, 2)
            herb_health = (7, 65)
            pred_health = (8, 22)
            pred_strength = (8, 53)
            _amount_eaten_for_offspring = 8
        """
        self.width = 16
        self.height = 15
        self.count_grass = 3
        self.count_rock = 9
        self.count_tree = self.count_rock
        self.count_predator = 9
        self.count_herbivore = self.count_predator * 1
        self.speed_range = (1, 2)
        self.herb_health = (6, 65)
        self.pred_health = (9, 22)
        self.pred_strength = (9, 53)
        self._amount_eaten_for_offspring = 7

    def determines_speed(self) -> int:
        """
        Returns a random speed for a creature within the defined `speed_range`.

        Returns:
        --------
        int:
            A randomly selected speed value within the range defined by `speed_range`.
        """
        return randint(*self.speed_range)

    def determines_health(self, name_creature: str) -> int:
        """
        Returns a random health value for a creature based on its type.

        Parameters:
        -----------
        name_creature : str
            The type of creature ('Herb' for Herbivores, 'Pred' for Predators).

        Returns:
        --------
        int:
            A randomly selected health value within the appropriate range for the creature type.

        Raises:
        -------
        TypeError:
            If the creature type is invalid or not recognized.
        """
        if name_creature == 'Herb':
            return randint(*self.herb_health)
        elif name_creature == 'Pred':
            return randint(*self.pred_health)
        raise TypeError(f"Неверный тип входных данных {name_creature}")

    def determines_strength(self, name_creature: str) -> int:
        """
        Returns a random strength value for a Predator, or `None` for other creature types.

        Parameters:
        -----------
        name_creature : str
            The type of creature ('Pred' for Predators).

        Returns:
        --------
        int or None:
            A randomly selected strength value within the range defined for Predators,
            or `None` for other creature types.
        """
        if name_creature == 'Pred':
            return randint(*self.pred_strength)
        return None

    def count_creatures(self, name_creature: str) -> int:
        """
        Returns the number of creatures of a specific type.

        Parameters:
        -----------
        name_creature : str
            The type of creature ('Herb' for Herbivores, 'Pred' for Predators).

        Returns:
        --------
        int:
            The number of creatures of the specified type.

        Raises:
        -------
        ValueError:
            If the creature type is invalid or not recognized.
        """
        if name_creature == 'Herb':
            return self.count_herbivore
        elif name_creature == 'Pred':
            return self.count_predator
