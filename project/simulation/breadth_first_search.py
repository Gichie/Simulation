from collections import deque
from project.simulation.Map import Map
from project.simulation.actions import Actions
from project.setting import Setting
from project.simulation.render import Render


class Bfs:
    def __init__(self, start):
        self.queue = deque([start])
        self.visited = set()
        self.found_objects = dict()

    def bfs(self):
        while self.queue:
            current = self.queue.popleft()
            if current in self.visited:
                continue
            self.visited.add(current)

            entity = map.map.get(current)
            if entity and entity in ('Herb', 'Grss', 'Tree', 'Rock'):
                self.found_objects[current[::-1]] = entity

            for x,y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + x, current[1] + y)
                if neighbor in map.map and neighbor not in self.visited:
                    self.queue.append(neighbor)

        return self.found_objects


if __name__ == '__main__':
    Actions.creature()
    map = Map(Setting().width, Setting().height)
    Render.display(Map, map.create_map())
    b = Bfs((0,0))
    print(b.bfs())

    


