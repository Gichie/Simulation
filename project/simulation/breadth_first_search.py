from collections import deque
from project.simulation.Map import Map
from project.simulation.actions import Actions
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creatingObjects import CreatingObjects


class Bfs:
    def __init__(self, start, map):
        self.queue = deque([start])
        self.visited = set()
        self.found_objects = dict()
        self.parent = dict()
        self.start = start
        self.map = map

    def bfs(self, goal):

        while self.queue:
            current = self.queue.popleft()
            if current in self.visited:
                continue
            self.visited.add(current)

            if self.map.map.get(current) == goal:                               # Проверка на достижение цели
                return self.construct_path(self.start, current)                    # Построение пути

            for x,y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + x, current[1] + y)

                if neighbor in self.map.map and neighbor not in self.visited and self.map.map.get(neighbor) in ('(..)', goal):
                    self.queue.append(neighbor)
                    self.parent[neighbor] = current
        print('Невозможно проложить путь до цели')


    def construct_path(self, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = self.parent.get(current)
            if current is None:                              # Если мы не можем найти путь
                return None
        path.append(start)
        path.reverse()
        return path

'''if __name__ == '__main__':
    Actions.creature()
    print(CreatingObjects.creating_objects)
    herb = CreatingObjects.creating_objects[0]
    grass = CreatingObjects.creating_objects[3]
    map = Map(Setting.width, Setting.height)
    Render.display(Map, map.create_map())
    b = Bfs((herb.x, herb.y))
    b2 = Bfs((herb.x, herb.y))
    print(b.bfs((grass.x, grass.y)))'''





    


