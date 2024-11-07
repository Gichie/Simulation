from abc import ABC


class Entity(ABC):
    """
    Base class for all creatures and objects in the simulation.

    This class provides basic attributes and methods common to all entities in the game, including
    their position (x, y) and string representations.

    Attributes:
    -----------
    x : int
        The X-coordinate of the entity's position.
    y : int
        The Y-coordinate of the entity's position.

    Methods:
    --------
    __repr__:
        Returns a string representation of the entity, including its class name and position.
    __str__:
        Returns the name of the entity as a string (used for display purposes).
    """

    def __init__(self, x: int, y: int):
        """
        Initializes the Entity with the given coordinates.

        Parameters:
        -----------
        x : int
            The X-coordinate of the entity's position.
        y : int
            The Y-coordinate of the entity's position.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Provides a detailed string representation of the entity, including its class and position.

        Returns:
        --------
        str
            A string in the format: 'EntityName(x, y)'.
        """
        return f'{type(self).__name__}({self.x}, {self.y})'

    def __str__(self):
        """
        Returns the name of the entity as a string (to be displayed).

        Returns:
        --------
        str
            The name of the entity (usually defined in derived classes).
        """
        return self._name
