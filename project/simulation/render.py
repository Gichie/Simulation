from project.setting import Setting


class Render:
    '''def __init__(self, map):
        self.map = map'''

    def display(self):
        # Создаем пустую матрицу с нужным количеством строк и столбцов
        grid = []
        cell_width = 6  # Ширина ячейки с отступами

        for y in range(Setting.height):
            row = []
            for x in range(Setting.width):
                # Получаем элемент или '   ', если ключа нет, и форматируем его для ширины ячейки

                cell_content = self.map[(x,y)].name.center(cell_width)  #для себя с отображением координат ка нарте
                row.append(cell_content)
            grid.append(" | ".join(row))  # Объединяем строку через '|'

        # Выводим карту
        separator = "-" * (Setting.width * (cell_width + 3) - 1)  # Разделитель между строками
        for line in grid:
            print(line)
            print(separator)  # Выводим разделитель после каждой строки

