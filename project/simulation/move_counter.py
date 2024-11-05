class MoveCounter:
    counter = 0

    @staticmethod
    def move_counter() -> str:
        MoveCounter.counter += 1
        print()
        return f'Количество ходов: {MoveCounter.counter}'
