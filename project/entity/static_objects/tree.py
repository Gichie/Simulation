from project.entity.entity import Entity


class Tree(Entity):
    """
    Tree is a static object that occupies a single cell on the map.
    Trees cannot move or interact with other entities.
    Tree prevents moving creatures from moving.

    Attributes:
    -----------
    Inherits all attributes from the Entity base class.

    Methods:
    --------
    No additional methods. Tree only serves as a static obstacle.
    """

    def __init__(self, x: int, y: int):
        """
        Initializes a Tree object at the specified coordinates.

        Parameters:
        -----------
        x : int
            X-coordinate of the tree's position.
        y : int
            Y-coordinate of the tree's position.
        """
        super().__init__(x, y)
        self._name: str = 'Tree'
