from project.entity.entity import Entity


class Rock(Entity):
    """
    Rock is a static object that occupies a single cell on the map.
    Rocks cannot move and do not interact with other entities.
    A rock prevents moving creatures from moving.

    Attributes:
    -----------
    Inherits all attributes from the Entity base class.

    Methods:
    --------
    No additional methods. Rock only serves as a static obstacle.
    """

    def __init__(self, x: int, y: int):
        """
        Initializes a Rock object at the specified coordinates.

        Parameters:
        -----------
        x : int
            X-coordinate of the rock's position.
        y : int
            Y-coordinate of the rock's position.
        """
        super().__init__(x, y)
        self._name: str = 'Rock'
