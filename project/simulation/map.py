from random import shuffle

from project.entity.entity import Entity
from project.setting import Setting
from project.simulation.creating_objects import CreatingObjects


class Map:
    """
    A class representing the simulation map, which stores entities and their positions.

    The map is implemented as a hash table (dictionary) where each key is a tuple of coordinates (x, y), and the value is the entity (such as a creature or static object) at those coordinates.

    Attributes:
    -----------
    _setting : Setting
        A class-level attribute that holds the configuration settings for the map, such as width and height.

    Methods:
    --------
    _create_map() -> dict:
        Creates the initial map by populating it with entities and their coordinates.

    collects_free_coordinates(map: dict) -> tuple[int, int]:
        Collects and returns a random free coordinate (x, y) from the map, where no entity is present.

    remove_entity(x: int, y: int) -> None:
        Removes the entity located at the given coordinates (x, y) from the map.
    """

    _setting = Setting()

    def __init__(self):
        """Initializes the Map object by creating the map with entities."""
        self._map = self._create_map()

    def _create_map(self) -> dict[tuple[int, int], Entity]:
        """
        Creates the initial map by populating it with entities (both creatures and static objects) at their respective coordinates.

        Returns:
        --------
        dict[tuple[int, int], Entity]
            A dictionary representing the map, where the keys are tuples of coordinates (x, y), and the values are the corresponding entities.
        """
        game_map = {(el.x, el.y): el for el in CreatingObjects.creating_objects}
        return game_map

    @classmethod
    def collects_free_coordinates(cls, map: dict[tuple[int, int]]) -> tuple([int, int]):
        """
        Collects all empty (unoccupied) coordinates on the map, shuffles them, and returns a random free coordinate.

        Parameters:
        -----------
        map : dict[tuple[int, int], Entity]
            The current map with all entities.

        Returns:
        --------
        tuple[int, int] or None
            A tuple representing a random free coordinate (x, y) if available, or None if no free space is found.
        """
        # Collect all coordinates that are not occupied by any entity
        empty_coords = [(x, y) for x in range(cls._setting.width) for y in range(cls._setting.height) if
                        map.get((x, y), None) is None]
        if empty_coords:  # If there are empty coordinates
            shuffle(empty_coords)  # Shuffle to add randomness
            return empty_coords[0]  # Return the first random empty coordinate
        return None  # Return None if no empty coordinates are available

    def remove_entity(self, x: int, y: int) -> None:
        """
        Removes an entity from the map at the specified coordinates (x, y).

        Parameters:
        -----------
        x : int
            The x-coordinate of the entity to be removed.

        y : int
            The y-coordinate of the entity to be removed.
        """
        self._map.pop((x, y), None)  # Remove the entity from the map at the given coordinates
