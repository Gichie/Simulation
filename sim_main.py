import threading

from project.setting import Setting
from project.simulation.actions import Actions
from project.simulation.creating_objects import CreatingObjects
from project.simulation.creature_moves import CreatureMove
from project.simulation.map import Map
from project.simulation.render import Render


class Simulation:
    """
    A class that manages and runs the simulation, including initialization, control of simulation steps,
    and pausing and resuming the simulation process.

    This class sets up the simulation environment, initializes the map and creatures,
    and handles the main simulation loop. It also supports user commands to pause and resume the simulation.

    Attributes:
    -----------
    map : dict[tuple[int, int], Entity]
        A dictionary representing the simulation map, where keys are coordinates and values are entities (creatures, objects).
    render : Render
        The object responsible for rendering the map and displaying the simulation.
    creature_move : CreatureMove
        The object responsible for moving creatures on the map.
    pause_event : threading.Event
        A threading event used to pause and resume the simulation.

    Methods:
    --------
    __init__():
        Initializes the simulation, creates map objects, and sets up the initial display.

    start_simulation() -> None:
        Starts the main loop of the simulation, handling pausing, resuming, and moving creatures.

    next_step(num_steps=1) -> None:
        Simulates and renders one step or the specified number of steps for all moving creatures.

    pause() -> None:
        Pauses the simulation.

    resume() -> None:
        Resumes the simulation after it has been paused.

    wait_for_commands() -> None:
        Listens for user input to pause or resume the simulation.
    """

    def __init__(self):
        """
        Initializes the simulation, including creating map objects and setting up the simulation environment.

        This method sets up the simulation with default settings:
        - Creates the necessary creatures (Herbivores, Predators, etc.).
        - Initializes the map, renderer, and creature movement objects.
        - Sets up a pause event to control the flow of the simulation.
        """
        setting = Setting()
        Actions(setting).creature()

        self.map = Map()._map
        self.render = Render(setting.width, setting.height, self.map)
        self.creature_move = CreatureMove(self.map, self.render, setting)
        self.pause_event = threading.Event()  # Флаг для управления паузой
        self.render.display()

    def start_simulation(self) -> None:
        """
        Starts the main simulation loop, with the ability to pause and resume the simulation.

        This method:
        - Starts a thread to listen for user input commands ('pause' or 'resume').
        - Continues to run the simulation as long as there are moving creatures,
          processing each simulation step and updating the map display.
        """
        self.pause_event.set()  # Sets the event to allow the simulation to start

        # Start a thread to wait for commands (pause or resume)
        threading.Thread(target=self.wait_for_commands, daemon=True).start()

        while CreatingObjects.moving_creatures:
            self.pause_event.wait()  # Wait for the pause flag to be set
            self.next_step()

    def next_step(self, num_steps=1) -> None:
        """
        Advances the simulation by a specified number of steps, moving creatures and rendering the updated map.

        Parameters:
        -----------
        num_steps : int
            The number of steps to simulate. Defaults to 1.

        For each step, this method moves all creatures and updates the display.
        """
        for _ in range(num_steps):
            self.creature_move.moves()

    def pause(self) -> None:
        """
        Pauses the simulation, halting the movement of creatures and other actions.

        Prints a message to indicate that the simulation has been paused.
        """
        print("Simulation paused.")
        self.pause_event.clear()

    def resume(self) -> None:
        """
        Resumes the simulation after it has been paused.

        Prints a message to indicate that the simulation has been resumed.
        """
        print("Simulation resumed.")
        self.pause_event.set()

    def wait_for_commands(self) -> None:
        """
        Listens for user input to pause or resume the simulation.

        This method continuously listens for the 'pause' or 'resume' command and
        calls the appropriate methods to control the simulation state.
        """
        while True:
            command = input("Введите команду ('pause' или 'resume'): ").strip().lower()
            if command == "pause":
                self.pause()
            elif command == "resume":
                self.resume()
            else:
                print("Неизвестная команда. Попробуйте 'pause' или 'resume'.")


if __name__ == '__main__':
    sim = Simulation()
    sim.start_simulation()
