from project.setting import Setting

class Render:
    def display(self, map: dict):
        for i in range(Setting.width):
            for j in range(Setting.height):
                print(f'{map[(i, j)]:^5}', end='')
            print()

