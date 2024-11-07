from colorama import Fore, Style

from project.entity.creatures.herbivore import Herbivore
from project.entity.creatures.predator import Predator
from project.entity.entity import Entity
from project.entity.static_objects.grass import Grass


class Render:
    """
    A class to render and display the game map, showing the positions of various entities (Herbivores, Predators, Grass, etc.) in a grid format.

    Attributes:
    -----------
    width : int
        The width of the map (in terms of the number of columns).
    height : int
        The height of the map (in terms of the number of rows).
    map : dict[tuple[int, int], Entity])
        A dictionary holding entities and their positions on the map.
        The keys are tuples representing coordinates (x, y), and the values are instances of Entity or its subclasses.

    Methods:
    --------
    __init__(self, width: int, height: int, map: dict[tuple[int, int], Entity]):
        Initializes the Render object with the width, height, and current map state.

    display(self) -> None:
        Displays the game map in a grid format with entities in their respective positions.
        The entities are color-coded as follows:
            - Herbivores: Yellow
            - Predators: Red
            - Grass: Green
        If a cell is empty, it will show a blank space.
    """

    def __init__(self, width: int, height: int, map: dict[tuple[int, int], Entity]):
        """
        Initializes the Render object.

        Args:
            width (int): The width of the map (number of columns).
            height (int): The height of the map (number of rows).
            map (dict[tuple[int, int], Entity]): A dictionary representing the current state of the map,
                                                 where keys are coordinates (x, y) and values are instances of Entity or its subclasses.
        """
        self.width = width
        self.height = height
        self.map = map

    def display(self) -> None:
        """
        Displays the game map in a grid format.

        Each cell in the grid represents a position on the map. The content of each cell is formatted as follows:
        - If the cell is empty, it shows a blank space.
        - If the cell contains a Herbivore, it will be displayed in yellow.
        - If the cell contains a Predator, it will be displayed in red.
        - If the cell contains Grass, it will be displayed in green.

        The grid rows are separated by horizontal lines for better readability.

        The output will look like a grid where each entity is displayed in a colored cell.
        """

        # Create an empty grid
        grid = []
        cell_width = 6  # Width of each cell (for consistent spacing)

        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Retrieve the entity at the current coordinate
                creature = self.map.get((x, y), None)

                if creature is None:
                    # If the cell is empty, show a blank space
                    cell_content = ' '.center(cell_width)
                elif isinstance(creature, Herbivore):
                    # If it's a Herbivore, display it with yellow color
                    cell_content = f"{Fore.YELLOW}{creature._name.center(cell_width)}{Style.RESET_ALL}"
                elif isinstance(creature, Grass):
                    # If it's Grass, display it with green color
                    cell_content = f"{Fore.GREEN}{creature._name.center(cell_width)}{Style.RESET_ALL}"
                elif isinstance(creature, Predator):
                    # If it's a Predator, display it with red color
                    cell_content = f"{Fore.RED}{creature._name.center(cell_width)}{Style.RESET_ALL}"
                else:
                    # For other types of entities, display their name centered
                    cell_content = self.map[(x, y)]._name.center(cell_width)
                row.append(cell_content)
            grid.append(" | ".join(row))  # Join the row with a separator

        # Print the map
        separator = "-" * (self.width * (cell_width + 3) - 1)  # Horizontal separator line
        for line in grid:
            print(line)
            print(separator)  # Print the separator after each row
