from project.setting import Setting


class Render:
    def __init__(self, map):
        self.map = map

    def display(self, map: dict):
        # Создаем пустую матрицу с нужным количеством строк и столбцов
        grid = []
        cell_width = 4  # Ширина ячейки с отступами

        for y in range(Setting.height):
            row = []
            for x in range(Setting.width):
                # Получаем элемент или '(......)', если элемента нет, и форматируем его для ширины ячейки
                cell_content = str(map.get((x, y), '(......)')).center(cell_width)
                row.append(cell_content)
            grid.append(" | ".join(row))  # Объединяем строку через '|'

        # Выводим карту
        separator = "-" * (Setting.width * (cell_width + 3) - 1)  # Разделитель между строками
        for line in grid:
            print(line)
            print(separator)  # Выводим разделитель после каждой строки

