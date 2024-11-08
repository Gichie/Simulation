from abc import ABC


class Entity(ABC):
    """
    Base class for all creatures and objects in the simulation.

    Attributes:
    -----------
    x : int
        The X-coordinate of the entity's position.
    y : int
        The Y-coordinate of the entity's position.
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

    def __repr__(self) -> str:
        """Provides a detailed string representation of the entity, including its class and position."""
        return f'{type(self).__name__}({self.x}, {self.y})'

    def __str__(self) -> str:
        """Returns the name of the entity as a string (to be displayed)."""
        return self._name
