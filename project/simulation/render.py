from colorama import Fore, Style
from project.entity.creatures.herbivore import Herbivore
from project.entity.creatures.predator import Predator
from project.entity.static_objects.grass import Grass


class Render:
    def __init__(self, width, height, map):
        self.width = width
        self.height = height
        self.map = map

    def display(self):
        # Создаем пустую матрицу с нужным количеством строк и столбцов
        grid = []
        cell_width = 6  # Ширина ячейки с отступами

        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Получаем существо из карты или '   ', если там пусто
                creature = self.map.get((x, y), None)

                if isinstance(creature, Herbivore):
                    # Если это Herbivore, добавляем зеленый цвет
                    cell_content = f"{Fore.YELLOW}{creature.name.center(cell_width)}{Style.RESET_ALL}"
                elif isinstance(creature, Grass):
                    cell_content =f"{Fore.GREEN}{creature.name.center(cell_width)}{Style.RESET_ALL}"
                elif isinstance(creature, Predator):
                    cell_content = f"{Fore.RED}{creature.name.center(cell_width)}{Style.RESET_ALL}"
                else:
                    cell_content = self.map[(x, y)].name.center(cell_width)  # для себя с отображением координат ка нарте
                row.append(cell_content)
            grid.append(" | ".join(row))  # Объединяем строку через '|'

        # Выводим карту
        separator = "-" * (self.width * (cell_width + 3) - 1)  # Разделитель между строками
        for line in grid:
            print(line)
            print(separator)  # Выводим разделитель после каждой строки
