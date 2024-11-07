class CreatingObjects:
    """
    A class to manage the creation and removal of creatures and objects in the simulation.

    This class is used to keep track of the created objects and the creatures that are moving in the simulation.
    It provides methods for adding creatures to the simulation, as well as removing them.

    Attributes:
    -----------
    creating_objects : list
        A list that holds all objects (creatures and static objects) created in the simulation.

    moving_creatures : list
        A list that holds all the creatures that are actively moving in the simulation.

    dct : dict
        A dictionary that maps the name of a creature type (e.g., 'Pred') to the list of moving creatures of that type.

    Methods:
    --------
    remove_creature(x: int, y: int, name='Pred'):
        Removes the creature of the specified type from the `moving_creatures` list if it is at the given position (x, y).
    """

    creating_objects = []
    moving_creatures = []

    dct = {'Pred': moving_creatures}

    @staticmethod
    def remove_creature(x: int, y: int, name='Pred'):
        """
        Removes a creature from the list of moving creatures if it is at the specified coordinates.

        This method searches through the list of moving creatures for a creature of the given type (`name`)
        that is located at the given (x, y) coordinates. If found, it removes the creature from the list.

        Parameters:
        -----------
        x : int
            The x-coordinate of the creature to remove.
        y : int
            The y-coordinate of the creature to remove.
        name : str
            The name of the creature type to remove (default is 'Pred' for predator creatures).
        """
        for creature in CreatingObjects.dct[name]:
            if creature.x == x and creature.y == y:
                CreatingObjects.dct[name].remove(creature)
                break
