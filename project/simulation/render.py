from project.setting import Setting

class Render:
    def display(self, map: dict):
        # Создаем пустую матрицу с нужным количеством строк и столбцов
        grid = []
        for y in range(Setting.height):
            row = []
            for x in range(Setting.width):
                row.append(map.get((x,y), '(..)' ))  # Получаем элемент или '(..)', если элемента нет
            grid.append(" ".join(row))  # Объединяем строку через пробел

        # Выводим карту
        for line in grid:
            print(line)

