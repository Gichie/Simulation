from project.setting import Setting

class Render:
    def display(self, map):
        for i in range(Setting.height):
            for j in range(Setting.width):
                print(f'{map[(i, j)]:^5}', end='')
            print()

