from project.entity.entity import Entity
from project.simulation.map import Map


class Grass(Entity):
    """
    The Grass class represents a food resource for herbivorous creatures (Herbivore) on the game map.
    Grass objects occupy specific coordinates and can be removed or respawned as needed.

    Attributes:
    -----------
    _name : str
        A default name for the grass object (set to 'Grss').

    Methods:
    --------
    create_grass(map: dict[tuple[int, int], Entity]) -> None
        Identifies all free coordinates and spawns grass at a random location on the map.

    remove_and_spawn_grass(map: dict[tuple[int, int], 'Grass']) -> None
        Removes the current grass object from the map and calls `create_grass` to spawn new grass at a free location.
    """

    def __init__(self, x: int, y: int):
        """
        Initializes a grass object at the given coordinates.

        Parameters:
        -----------
        x : int
           The X-coordinate of the grass object.
        y : int
           The Y-coordinate of the grass object.
        """
        super().__init__(x, y)
        self._name = 'Grss'

    def __str__(self):
        """
        Returns the string representation of the grass object.

        Returns:
        --------
        str
            The default name of the grass object.
        """
        return 'Grss'

    @classmethod
    def create_grass(cls, map: dict[tuple[int, int], Entity]) -> None:
        """
        Creates a new grass object at a random free position on the map, if one is available.

        Parameters:
        -----------
        map : dict[tuple[int, int], Entity]
            A dictionary representing the map, with keys as coordinate tuples and values as entities at those locations.
        """
        coords = Map.collects_free_coordinates(map)
        if coords:
            map[coords] = Grass(*coords)
            print(f'Трава выросла {coords}')

    def remove_and_spawn_grass(self, map: dict[tuple[int, int], 'Grass']) -> None:
        """
        Removes the current grass object from the map and respawns grass at a new random free location.

        Parameters:
        -----------
        map : dict[tuple[int, int], 'Grass']
            A dictionary representing the map, with keys as coordinate tuples and values as entities at those locations.
        """
        del map[(self.x, self.y)]
        self.create_grass(map)
