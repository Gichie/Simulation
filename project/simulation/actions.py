from random import shuffle

from project.entity.creatures.herbivore import Herbivore
from project.entity.creatures.predator import Predator
from project.entity.static_objects.grass import Grass
from project.entity.static_objects.rock import Rock
from project.entity.static_objects.tree import Tree
from project.setting import Setting
from project.simulation.creating_objects import CreatingObjects


class Actions:
    """
    A class that manages the actions to be performed before the start of the simulation.

    It handles the creation and distribution of entities (creatures and static objects) across the simulation map.

    Attributes:
    -----------
    setting : Setting
        An instance of the settings class containing various simulation parameters (e.g., entity counts).
    coords : list[tuple[int, int]]
        A list of randomly shuffled coordinates used for placing objects and creatures on the map.

    Methods:
    --------
    create_coords_creatures:
        Generates and shuffles coordinates to be used for object placement in the simulation.

    creature:
        Creates different types of creatures and static objects (grass, rock, tree, herbivores, and predators) based on the settings.

    create_object:
        Creates and places an object (e.g., grass, rock, tree, herbivore, or predator) on the map at a specified coordinate.
    """

    def __init__(self, setting: Setting):
        """
        Initializes the Actions class with the given settings.

        Parameters:
        -----------
        setting : Setting
            The settings object containing configuration for the simulation (e.g., counts of different entities).
        """
        self.setting = setting
        self.coords: list[tuple[int, int]] = self.create_coords_creatures()

    def create_coords_creatures(self) -> list[tuple[int, int]]:
        """
        Generates a shuffled list of coordinates to be used for placing entities on the map.

        Returns:
        --------
        list[tuple[int, int]]
            A list of shuffled coordinates (x, y) for placing creatures and objects on the map.
        """
        coords = [(i, j) for j in range(self.setting.height) for i in range(self.setting.width)]
        shuffle(coords)
        return coords

    def creature(self):
        """
        Creates and places the different types of creatures and static objects on the map based on the settings.

        This method will create the following:
        - Grass: Based on the count specified in the settings.
        - Rock: Based on the count specified in the settings.
        - Tree: Based on the count specified in the settings.
        - Herbivores: Based on the count specified in the settings.
        - Predators: Based on the count specified in the settings.
        """
        self.create_object('Grss', self.setting.count_grass)
        self.create_object('Rock', self.setting.count_rock)
        self.create_object('Tree', self.setting.count_tree)
        self.create_object('Herb', self.setting.count_herbivore)
        self.create_object('Pred', self.setting.count_predator)

    def create_object(self, object_type: str, count: int) -> None:
        """
        Creates and places a specified number of objects on the map based on the provided object type.

        Parameters:
        -----------
        object_type : str
            The type of object to create (e.g., 'Grss', 'Rock', 'Tree', 'Herb', 'Pred').
        count : int
            The number of objects to create of the specified type.
        """
        for i in range(count):
            x, y = self.coords.pop()  # Get the next available coordinate

            # Create the appropriate object based on the type
            if object_type == 'Grss':
                obj = Grass(x, y)
            elif object_type == 'Rock':
                obj = Rock(x, y)
            elif object_type == 'Tree':
                obj = Tree(x, y)
            elif object_type == 'Herb':
                speed = self.setting.determines_speed()
                hp = self.setting.determines_health(object_type)
                obj = Herbivore(x, y, speed, hp)
            elif object_type == 'Pred':
                speed = self.setting.determines_speed()
                hp = self.setting.determines_health(object_type)
                strengh = self.setting.determines_strength(object_type)
                obj = Predator(x, y, speed, hp, strengh)
            else:
                raise ValueError(f"Unknown object type: {object_type}")

            # Add the created object to the list of all objects
            CreatingObjects.creating_objects.append(obj)

            # If the object is a creature (herbivore or predator), add it to the moving creatures list
            if object_type in ['Herb', 'Pred']:
                CreatingObjects.moving_creatures.append(obj)
