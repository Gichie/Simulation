from collections import deque

from project.setting import Setting


class Bfs:
    """
    A class to perform the Breadth-First Search (BFS) algorithm to find the shortest path on the map.

    This class is used to find the shortest path from a starting point to a target object on the simulation map.

    Attributes:
    -----------
    queue : deque
        A queue used to hold the nodes to be explored, initialized with the starting point.
    visited : set
        A set to keep track of the visited nodes to avoid re-exploring.
    found_objects : dict
        A dictionary to store found objects along the path.
    parent : dict
        A dictionary to store the parent of each node, used to reconstruct the path.
    start : tuple[int, int]
        The starting point of the search.
    map : dict[tuple[int, int], 'Creature']
        The simulation map that contains the entities and obstacles.
    setting : Setting
        The settings object containing the simulation parameters like map width and height.

    Methods:
    --------
    bfs(goal):
        Performs the BFS algorithm to find the shortest path to the target object.

    construct_path(start: tuple[int, int], goal: tuple[int, int]) -> list[tuple[int, int]]:
        Reconstructs the path from the start to the goal using the parent dictionary.
    """

    def __init__(self, start: tuple[int, int], map: dict[tuple[int, int], 'Creature'], setting: Setting):
        """
        Initializes the BFS object with the given start position, map, and settings.

        Parameters:
        -----------
        start : tuple[int, int]
            The starting coordinate (x, y) on the map.
        map : dict[tuple[int, int], 'Creature']
            The map that holds the simulation entities (creatures, obstacles, etc.).
        setting : Setting
            The settings object with the simulation dimensions (width, height) and other parameters.
        """
        self.queue = deque([start])
        self.visited = set()
        self.found_objects = dict()
        self.parent = dict()
        self.start = start
        self.map = map
        self.setting = setting

    def bfs(self, goal):
        """
        Performs the Breadth-First Search (BFS) algorithm to find the shortest path to a goal object.

        The search explores the map by visiting each neighboring cell in four possible directions (down, left, up, right)
        and checks if the target object is found. Once the target is found, the path is reconstructed.

        Parameters:
        -----------
        goal : type
            The type of object we are searching for (e.g., Herbivore, Predator, Grass).

        Returns:
        --------
        list[tuple[int, int]] | None
            A list of coordinates representing the path from the start to the goal. Returns `None` if no path is found.
        """
        while self.queue:
            current = self.queue.popleft()
            if current in self.visited:
                continue
            self.visited.add(current)
            # Check if the goal has been reached
            if type(self.map.get(current, None)) == goal:
                # Construct the path from start to goal
                return self.construct_path(self.start, current)

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + x, current[1] + y)
                if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < self.setting.width and neighbor[1] < self.setting.height:
                    if neighbor not in self.visited and type(self.map.get(neighbor, None)) in (type(None), goal):
                        self.queue.append(neighbor)
                        self.parent[neighbor] = current

    def construct_path(self, start: tuple[int, int], goal: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Reconstructs the path from the start position to the goal position using the parent dictionary.

        This method traces back from the goal to the start using the parent references to build the path in reverse.

        Parameters:
        -----------
        start : tuple[int, int]
            The starting coordinate (x, y) on the map.
        goal : tuple[int, int]
            The target coordinate (x, y) where the goal was found.

        Returns:
        --------
        list[tuple[int, int]] | None
            A list of coordinates representing the shortest path from the start to the goal, or `None` if no path exists.
        """
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = self.parent.get(current)
            # No path found
            if current is None:
                return None
        path.append(start)
        path.reverse()
        return path
