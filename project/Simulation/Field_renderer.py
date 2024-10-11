from project.Simulation.Map import Map

class FieldRenderer:
    def display(cls):
        m = Map(5, 5)
        for i in range(m.width):
            for j in range(m.height):
                print(m.map[(i, j)], end=' ')
            print()

if __name__ == '__main__':
    f = FieldRenderer()
    f.display()