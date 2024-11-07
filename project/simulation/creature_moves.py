from project.entity.creatures.herbivore import Herbivore
from project.entity.static_objects.grass import Grass
from project.setting import Setting
from project.simulation.breadth_first_search import Bfs
from project.simulation.creating_objects import CreatingObjects
from project.simulation.move_counter import MoveCounter


class CreatureMove:
    """
    A class that manages the movement and actions of creatures in the simulation.

    This class controls the logic for creatures moving within the simulation, based on the current state of the map and their goals.
    It uses Breadth-First Search (BFS) to determine the best path to a goal and updates the state of creatures and the map accordingly.

    Attributes:
    -----------
    map : dict
        A dictionary representing the map, where keys are coordinates (x, y), and values are objects of type `Entity`.

    render : Render
        An instance of the `Render` class, which is used to visually update the simulation state after each move.

    setting : Setting
        An instance of the `Setting` class, which provides configuration options for the simulation, such as creature attributes.

    Methods:
    --------
    moves() -> None:
        Executes the movement for all creatures in the simulation. For each creature, it calculates the best path to its target,
        executes the move, and updates the visual representation of the simulation.
    """

    def __init__(self, map: dict[tuple[int, int]], render: 'Render', setting: Setting):
        """
        Initializes the CreatureMove instance with the given map, render, and setting.

        Parameters:
        -----------
        map : dict[tuple[int, int], Entity]
            A dictionary representing the map of the simulation.

        render : Render
            The render object that updates the simulation's visual output.

        setting : Setting
            The settings object containing the simulation's configuration.
        """
        self.map = map
        self.render = render
        self.setting = setting

    def moves(self) -> None:
        """
        Performs the movement actions for all creatures in the simulation. Each creature calculates its path towards a goal
        (either `Grass` for herbivores or `Herbivore` for predators) and executes its move.

        This method also calls the render object to update the display and prints the status of the creatures and the move counter.
        """
        # Mapping creature types to their goals (Herbivores to Grass, Predators to Herbivores)
        goals = {'Herb': Grass, 'Pred': Herbivore}

        # Iterate over all moving creatures and perform their moves
        for creature in CreatingObjects.moving_creatures:
            print()
            # Perform BFS to find the path to the target
            animal = Bfs((creature.x, creature.y), self.map, self.setting)
            # Get the path based on the creature's goal
            self.__path_of_animal = animal.bfs(goals[creature._name])
            # Execute the creature's move
            creature.make_move(self.__path_of_animal, self.map)
            # Update the visual state of the simulation
            self.render.display()
        # Print the current status of the simulation
        print(CreatingObjects.moving_creatures)  # List of currently moving creatures
        print(MoveCounter.move_counter())  # Print the move counter (the number of moves made in the simulation)
        print()
