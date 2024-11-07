class MoveCounter:
    """
    A class to count and track the number of moves made in the simulation.

    This class provides a static method for incrementing and displaying the move count during the simulation.

    Attributes:
    -----------
    counter : int
        A class-level attribute that stores the number of moves made in the simulation. It is initialized to 0.

    Methods:
    --------
    move_counter() -> str:
        Increments the move counter and returns the total number of moves made, formatted as a string.
    """

    counter = 0  # Class-level attribute to store the move count

    @staticmethod
    def move_counter() -> str:
        """
        Increments the move counter and returns a formatted string with the current number of moves.

        This method is static and can be called without an instance of the class.

        Returns:
        --------
        str
            A string containing the total number of moves made, in the format: 'Количество ходов: {counter}'
        """
        MoveCounter.counter += 1  # Increment the move counter by 1
        print()  # Prints a blank line for readability
        return f'Количество ходов: {MoveCounter.counter}'  # Returns the formatted move count as a string
